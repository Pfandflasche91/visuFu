from typing import Optional
from PySide6.QtCore import Signal, QObject,QTimer
from PySide6.QtWidgets import QWidget
from ui_visuFu import Ui_MainWidget

import datetime
import serial
import serial.tools.list_ports
import threading
import time
import pyqtgraph
import numpy as np

#pyside6-uic visuFu.ui -o ui_visuFu.py
class serialCom(QObject):
    finished = Signal(str)

    def __init__(self):
        super().__init__()
        self.exit_event = threading.Event()
        self.connectionStatus = False
        self.comPort = None
    
    def disconnectComPort(self):
        self.connectionStatus = False
        self.ser.close()
        while self.ser.is_open:
            pass
        print("Serial Communication DISCONNECTED: "+ self.comPort)
        
            
    def connectComPort(self,Port):
        self.comPort = Port
        self.baudRate = 115200
        self.ser = serial.Serial(self.comPort,self.baudRate)
        if self.ser.is_open:
            print("Serial Communication CONNECTED: "+ self.comPort)
            print(self.ser)
            self.connectionStatus= True
               
    def readserialdata(self):
        print("Thread -readserialdata- starts")
        try:
            while not self.exit_event.is_set(): 
                if self.connectionStatus:
                    if self.ser.in_waiting > 0 :
                        data = self.ser.readline().decode()
                        self.finished.emit(str(data))
                    #if self.ser.inWaiting() > 0 :
                    #    data = self.ser.read_until() 
                else:
                    time.sleep(1)
                    
        except Exception as e:
            print(f"Error reading data: {e}")
            
        finally:
            print("finally readserialdata")
     
    def sendserialdata(self,text):
        self.ser.write(text.encode())       
            
class MainWindow(QWidget, Ui_MainWidget):
    def __init__(self):
        pyqtgraph.setConfigOption('background','w')
        super().__init__()
        self.setupUi(self)
        self.graphicsView.plotItem.showGrid(True, True, 0.7)
        self.setWindowTitle("Serial Com Window")
        self.btn_send.clicked.connect(self.send)
        self.btn_refreshCom.clicked.connect(self.refreshComPort)
        self.btn_connectCom.clicked.connect(self.toggle_connection)
        self.lineEdit_send.returnPressed.connect(self.send)
        self.worker_serial = serialCom()
        self.worker_serial.finished.connect(self.update_Textbox)
        self.data_thread = threading.Thread(target=self.worker_serial.readserialdata)
        self.data_thread.start()
        
    def update(self):
        t1=time.perf_counter()
        points=100 #number of data points
        X=np.arange(points)
        Y=np.sin(np.arange(points)/points*3*np.pi+time.perf_counter())
        C=pyqtgraph.hsvColor(time.perf_counter()/5%1,alpha=.5)
        pen=pyqtgraph.mkPen(color=C,width=10)
        self.graphicsView.plot(X,Y,pen=pen,clear=True)
        #print("update took %.02f ms"%((time.process_time()-t1)*1000))
        if True:
            QTimer.singleShot(1, self.update) # QUICKLY repeat
            
    def toggle_connection(self):
        if self.btn_connectCom.text() == "Connect":
            self.connectComPort()
            self.update()
            self.btn_connectCom.setText("Disconnect")
        else:
            self.disconnectComPort()
            self.btn_connectCom.setText("Connect")
            
    def quit_application(self):
        self.disconnectComPort()
        self.worker_serial.exit_event.set()
        while  self.data_thread.is_alive():
            self.data_thread.join()
        print("Thread -readserialdata- ends")
        print("App closed")
    
    def disconnectComPort(self):
        if self.worker_serial.connectionStatus:
            self.worker_serial.disconnectComPort()
            self.appendTextBrowser("Serial Communication DISCONNECTED: " + str(self.worker_serial.comPort),"SYSTEM","red")
     
    def connectComPort(self):
        self.worker_serial.connectComPort(self.comboBox_Ports.currentData())
        while not self.worker_serial.ser.is_open:
            pass
        self.appendTextBrowser("Serial Communication CONNECTED: " + str(self.worker_serial.comPort),"SYSTEM","green")
        
    def refreshComPort(self):
        self.comboBox_Ports.clear()
        for idx, port in enumerate(serial.tools.list_ports.comports()):
            self.comboBox_Ports.addItem(f"Port: {port.device}, Description: {port.description}")
            self.comboBox_Ports.setItemData(idx,port.device)
            
    def send(self):
        text = self.lineEdit_send.text()
        if any(char.isalpha() for char in text ):
            self.worker_serial.sendserialdata(text)
            self.appendTextBrowser(text,"visuFu")
        else:
            pass
        self.lineEdit_send.clear()
            
    def update_Textbox(self,text):
        self.appendTextBrowser(text,"Brom")
    
    def appendTextBrowser(self,text,device,color="black"):
        colors={"red": "#ff0000","black" : "#000000","blue": "#0000ff","green":"#00b300"}
        current_time= datetime.datetime.now().strftime("%H:%M:%S")
        text = "<span style=\" color:"+ colors[color]+" ;\">%s</span" % text
        self.textBrowser.append("<b>"+current_time+ "</b> " + " -"+device+"- :  " + text)
            

                
        
    
    
        
     
        
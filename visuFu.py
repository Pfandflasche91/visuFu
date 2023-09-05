from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget
from ui_visuFu import Ui_MainWidget

import datetime

#uic -g python abc.ui > ui_abc.py

class MainWindow(QWidget, Ui_MainWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("User data")
        self.btn_send.clicked.connect(self.send)
        self.lineEdit_send_text = ""
        self.lineEdit_send.returnPressed.connect(self.send)
        
    def send(self):
        text = self.lineEdit_send.text()
        
        if any(char.isalpha() for char in text ):
            time= datetime.datetime.now().strftime("%H:%M:%S")
            self.lineEdit_send_text = text
            self.textBrowser.append("<b>"+time+ "</b> " + " -visuFu- :  " + self.lineEdit_send_text)
        else:
            pass
        self.lineEdit_send.clear()
        
    
    
        
     
        
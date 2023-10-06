# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'visuFu.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLineEdit,
    QPushButton, QSizePolicy, QTextBrowser, QVBoxLayout,
    QWidget)

class Ui_MainWidget(object):
    def setupUi(self, MainWidget):
        if not MainWidget.objectName():
            MainWidget.setObjectName(u"MainWidget")
        MainWidget.resize(1134, 715)
        self.verticalLayout = QVBoxLayout(MainWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_connectCom = QPushButton(MainWidget)
        self.btn_connectCom.setObjectName(u"btn_connectCom")

        self.horizontalLayout_2.addWidget(self.btn_connectCom)

        self.comboBox_Ports = QComboBox(MainWidget)
        self.comboBox_Ports.setObjectName(u"comboBox_Ports")

        self.horizontalLayout_2.addWidget(self.comboBox_Ports)

        self.btn_refreshCom = QPushButton(MainWidget)
        self.btn_refreshCom.setObjectName(u"btn_refreshCom")

        self.horizontalLayout_2.addWidget(self.btn_refreshCom)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.textBrowser = QTextBrowser(MainWidget)
        self.textBrowser.setObjectName(u"textBrowser")

        self.verticalLayout_2.addWidget(self.textBrowser)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit_send = QLineEdit(MainWidget)
        self.lineEdit_send.setObjectName(u"lineEdit_send")

        self.horizontalLayout.addWidget(self.lineEdit_send)

        self.btn_send = QPushButton(MainWidget)
        self.btn_send.setObjectName(u"btn_send")

        self.horizontalLayout.addWidget(self.btn_send)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout.addLayout(self.verticalLayout_2)


        self.retranslateUi(MainWidget)

        QMetaObject.connectSlotsByName(MainWidget)
    # setupUi

    def retranslateUi(self, MainWidget):
        MainWidget.setWindowTitle(QCoreApplication.translate("MainWidget", u"Form", None))
        self.btn_connectCom.setText(QCoreApplication.translate("MainWidget", u"Connect", None))
        self.btn_refreshCom.setText(QCoreApplication.translate("MainWidget", u"Refresh", None))
        self.btn_send.setText(QCoreApplication.translate("MainWidget", u"PushButton", None))
    # retranslateUi


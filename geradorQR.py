# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'geradorQR.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(370, 225)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_gera = QtWidgets.QPushButton(self.centralwidget)
        self.btn_gera.setGeometry(QtCore.QRect(20, 110, 91, 23))
        self.btn_gera.setObjectName("btn_gera")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 91, 21))
        self.label.setObjectName("label")
        self.txt_link = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_link.setGeometry(QtCore.QRect(20, 40, 341, 20))
        self.txt_link.setObjectName("txt_link")
        self.txt_nome_arquvo = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_nome_arquvo.setGeometry(QtCore.QRect(20, 80, 341, 20))
        self.txt_nome_arquvo.setObjectName("txt_nome_arquvo")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 60, 91, 21))
        self.label_3.setObjectName("label_3")
        self.btn_myFiles = QtWidgets.QPushButton(self.centralwidget)
        self.btn_myFiles.setGeometry(QtCore.QRect(270, 110, 91, 23))
        self.btn_myFiles.setObjectName("btn_myFiles")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 370, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Gerador QrCode"))
        self.btn_gera.setText(_translate("MainWindow", "Gerar QRCode"))
        self.label.setText(_translate("MainWindow", "Insira Seu Link"))
        self.label_3.setText(_translate("MainWindow", "Nome Do arquivo"))
        self.btn_myFiles.setText(_translate("MainWindow", "Meus Arquivos"))

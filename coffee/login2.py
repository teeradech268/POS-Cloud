# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login2.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import connectDB
from PyQt5.QtWidgets import QMessageBox
from main2 import Ui_MainWindow


class Ui_Loginwindow(object):
    def setupUi(self, Loginwindow):
        self.Loginwindow = Loginwindow
        Loginwindow.setObjectName("Loginwindow")
        Loginwindow.resize(386, 271)
        self.centralwidget = QtWidgets.QWidget(Loginwindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 110, 61, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 150, 61, 21))
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 210, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(80, 0, 221, 111))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(120, 210, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(110, 110, 181, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(110, 150, 181, 20))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        Loginwindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Loginwindow)
        self.statusbar.setObjectName("statusbar")
        Loginwindow.setStatusBar(self.statusbar)

        self.pushButton_2.clicked.connect(self.Cancle)
        self.pushButton.clicked.connect(self.login)

        self.retranslateUi(Loginwindow)
        QtCore.QMetaObject.connectSlotsByName(Loginwindow)

    def retranslateUi(self, Loginwindow):
        _translate = QtCore.QCoreApplication.translate
        Loginwindow.setWindowTitle(_translate("Loginwindow", "TNI Coffee Cashier"))
        self.label.setText(_translate("Loginwindow", "Username : "))
        self.label_2.setText(_translate("Loginwindow", "Password :"))
        self.pushButton_2.setText(_translate("Loginwindow", "Cancel"))
        self.label_3.setText(_translate("Loginwindow", "TNI Coffee Cashier"))
        self.pushButton.setText(_translate("Loginwindow", "Login"))

    def Cancle(self):
        self.Loginwindow.close()

    def login(self):
        from connectDB import connectdb
        db = connectdb()
        rs = db.USER.find({})
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        for i in rs:
            if i['username'] == username and i["password"] == password:
                msg = QMessageBox()
                msg.setText("Login Success")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec()
                self.window = QtWidgets.QMainWindow()
                self.message = username
                self.ui = Ui_MainWindow(self.message)
                self.ui.setupUi(self.window)
                self.window.show()
                self.Loginwindow.hide()


            else:
                msg = QMessageBox()
                msg.setText("Username or Password Incorrect")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Loginwindow = QtWidgets.QMainWindow()
    ui = Ui_Loginwindow()
    ui.setupUi(Loginwindow)
    Loginwindow.show()
    sys.exit(app.exec_())

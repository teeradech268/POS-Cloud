# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'checklog.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from showlog import  Ui_showlogWindow
from PyQt5.QtWidgets import QMessageBox

class Ui_CheckLogwindow(object):
    insertdate = ""
    def __init__(self, message):
        self.message = message

    def setupUi(self, CheckLogwindow):
        self.CheckLogwindow = CheckLogwindow
        CheckLogwindow.setObjectName("CheckLogwindow")
        CheckLogwindow.resize(287, 161)
        self.centralwidget = QtWidgets.QWidget(CheckLogwindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btncheck = QtWidgets.QPushButton(self.centralwidget)
        self.btncheck.setGeometry(QtCore.QRect(110, 80, 51, 23))
        self.btncheck.setObjectName("btncheck")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 30, 81, 21))
        self.label.setObjectName("label")
        self.lineDate = QtWidgets.QLineEdit(self.centralwidget)
        self.lineDate.setGeometry(QtCore.QRect(110, 30, 113, 20))
        self.lineDate.setObjectName("lineDate")
        self.btnBack = QtWidgets.QPushButton(self.centralwidget)
        self.btnBack.setGeometry(QtCore.QRect(170, 80, 51, 23))
        self.btnBack.setObjectName("btnBack")
        CheckLogwindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(CheckLogwindow)
        self.statusbar.setObjectName("statusbar")
        CheckLogwindow.setStatusBar(self.statusbar)

        self.btncheck.clicked.connect(self.findlog)
        self.btnBack.clicked.connect(self.backtomain)

        self.retranslateUi(CheckLogwindow)
        QtCore.QMetaObject.connectSlotsByName(CheckLogwindow)

    def retranslateUi(self, CheckLogwindow):
        _translate = QtCore.QCoreApplication.translate
        CheckLogwindow.setWindowTitle(_translate("CheckLogwindow", "Check Log"))
        self.btncheck.setText(_translate("CheckLogwindow", "Check"))
        self.label.setText(_translate("CheckLogwindow", "Input Date :"))
        self.btnBack.setText(_translate("CheckLogwindow", "Back"))

    def findlog(self):

            self.insertdate = self.lineDate.text()
            from connectDB import connectdb
            db = connectdb()
            rs = db.LOG.find({'date':self.insertdate});
            data = []
            if rs.count() >1 :
                self.window = QtWidgets.QMainWindow()
                for e in rs:
                    #item = [str(e['total']), e['date']]
                    item = "            {}              {}".format(str(e['total']), e['date'])
                    data.append(item)
                username = self.message
                self.message = [username,data]
                self.ui = Ui_showlogWindow(self.message)
                self.ui.setupUi(self.window)
                self.window.show()
                self.CheckLogwindow.hide()
            else:
                msg = QMessageBox()
                msg.setText("Record not found")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec()

    def backtomain(self):
        try:
            from main2 import Ui_MainWindow
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_MainWindow(self.message)
            self.ui.setupUi(self.window)
            self.window.show()
            self.CheckLogwindow.hide()
        except Exception as e:
            print(e)
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CheckLogwindow = QtWidgets.QMainWindow()
    ui = Ui_CheckLogwindow()
    ui.setupUi(CheckLogwindow)
    CheckLogwindow.show()
    sys.exit(app.exec_())

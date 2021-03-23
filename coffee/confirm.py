# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'confirm.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import datetime
from PyQt5.QtWidgets import QMessageBox



class Ui_ConfirmWindow(object):
    def __init__(self,message):
        self.message = message

    def setupUi(self, ConfirmWindow):
        self.ConfirmWindow = ConfirmWindow
        ConfirmWindow.setObjectName("ConfirmWindow")
        ConfirmWindow.resize(389, 394)
        self.centralwidget = QtWidgets.QWidget(ConfirmWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(280, 270, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(280, 300, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(90, 290, 47, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(80, 270, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lbltotalCF = QtWidgets.QLabel(self.centralwidget)
        self.lbltotalCF.setGeometry(QtCore.QRect(210, 240, 47, 13))
        self.lbltotalCF.setObjectName("lbltotalCF")
        self.lblReceiveCF = QtWidgets.QLabel(self.centralwidget)
        self.lblReceiveCF.setGeometry(QtCore.QRect(210, 270, 47, 13))
        self.lblReceiveCF.setObjectName("lblReceiveCF")
        self.lblchangeCF = QtWidgets.QLabel(self.centralwidget)
        self.lblchangeCF.setGeometry(QtCore.QRect(210, 300, 47, 13))
        self.lblchangeCF.setObjectName("lblchangeCF")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 20, 261, 16))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(280, 240, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(100, 240, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.btnokCF = QtWidgets.QPushButton(self.centralwidget)
        self.btnokCF.setGeometry(QtCore.QRect(110, 330, 75, 23))
        self.btnokCF.setObjectName("btnokCF")
        self.btnBackCF = QtWidgets.QPushButton(self.centralwidget)
        self.btnBackCF.setGeometry(QtCore.QRect(210, 330, 75, 23))
        self.btnBackCF.setObjectName("btnBackCF")
        self.listWidgetCF = QtWidgets.QListWidget(self.centralwidget)
        self.listWidgetCF.setGeometry(QtCore.QRect(70, 40, 256, 192))
        self.listWidgetCF.setObjectName("listWidgetCF")
        ConfirmWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(ConfirmWindow)
        self.statusbar.setObjectName("statusbar")
        ConfirmWindow.setStatusBar(self.statusbar)

        try :
            for i in self.message[0]:
                self.listWidgetCF.addItem(i)
        except Exception as e:
            print(e)

        self.btnokCF.clicked.connect(self.keepDb)
        self.btnBackCF.clicked.connect(self.Btomain)


        self.retranslateUi(ConfirmWindow)
        QtCore.QMetaObject.connectSlotsByName(ConfirmWindow)

    def retranslateUi(self, ConfirmWindow):
        _translate = QtCore.QCoreApplication.translate
        ConfirmWindow.setWindowTitle(_translate("ConfirmWindow", "Confirm Order"))
        self.label_8.setText(_translate("ConfirmWindow", "Baht."))
        self.label_9.setText(_translate("ConfirmWindow", "Baht."))
        self.label_6.setText(_translate("ConfirmWindow", "Change"))
        self.label_5.setText(_translate("ConfirmWindow", "Received"))
        self.lbltotalCF.setText(_translate("ConfirmWindow", str(self.message[1])))
        self.lblReceiveCF.setText(_translate("ConfirmWindow", str(self.message[2])))
        self.lblchangeCF.setText(_translate("ConfirmWindow", str(self.message[3])))
        self.label_3.setText(_translate("ConfirmWindow", "menu                               Qty       Price"))
        self.label_7.setText(_translate("ConfirmWindow", "Baht."))
        self.label_4.setText(_translate("ConfirmWindow", "Total"))
        self.btnokCF.setText(_translate("ConfirmWindow", "OK"))
        self.btnBackCF.setText(_translate("ConfirmWindow", "Back"))

    def keepDb(self):
        try :
            from main2 import Ui_MainWindow
            from connectDB import connectdb
            db = connectdb()
            date = datetime.date.today()
            total = self.message[1]
            db.LOG.insert_one({'total':total,'date':str(date)})
            msg = QMessageBox()
            msg.setText("Record Success")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec()
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_MainWindow(self.message[4])
            self.ui.setupUi(self.window)
            self.window.show()
            self.ConfirmWindow.hide()
        except Exception as e:
            print(e)

    def Btomain(self):
        from main2 import Ui_MainWindow
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow(self.message[4])
        self.ui.setupUi(self.window)
        self.window.show()
        self.ConfirmWindow.hide()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ConfirmWindow = QtWidgets.QMainWindow()
    ui = Ui_ConfirmWindow()
    ui.setupUi(ConfirmWindow)
    ConfirmWindow.show()
    sys.exit(app.exec_())

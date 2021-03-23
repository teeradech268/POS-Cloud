# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'showlog.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_showlogWindow(object):
    def __init__(self, message):
        self.message = message

    def setupUi(self, showlogWindow):
        self.showlogWindow = showlogWindow
        showlogWindow.setObjectName("showlogWindow")
        showlogWindow.resize(226, 376)
        self.centralwidget = QtWidgets.QWidget(showlogWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnbackShowLog = QtWidgets.QPushButton(self.centralwidget)
        self.btnbackShowLog.setGeometry(QtCore.QRect(80, 310, 75, 23))
        self.btnbackShowLog.setObjectName("btnbackShowLog")
        self.listWidgetShowlog = QtWidgets.QListWidget(self.centralwidget)
        self.listWidgetShowlog.setGeometry(QtCore.QRect(30, 80, 171, 211))
        self.listWidgetShowlog.setObjectName("listWidgetShowlog")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 20, 47, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(60, 60, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(140, 60, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        showlogWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(showlogWindow)
        self.statusbar.setObjectName("statusbar")
        showlogWindow.setStatusBar(self.statusbar)

        try:
            for i in self.message[1]:
                self.listWidgetShowlog.addItem(i)
        except Exception as e:
            print(e)

        self.btnbackShowLog.clicked.connect(self.goback)

        self.retranslateUi(showlogWindow)
        QtCore.QMetaObject.connectSlotsByName(showlogWindow)

    def retranslateUi(self, showlogWindow):
        _translate = QtCore.QCoreApplication.translate
        showlogWindow.setWindowTitle(_translate("showlogWindow", "Sale History"))
        self.btnbackShowLog.setText(_translate("showlogWindow", "Back"))
        self.label.setText(_translate("showlogWindow", "Log"))
        self.label_4.setText(_translate("showlogWindow", "Total"))
        self.label_5.setText(_translate("showlogWindow", "Date"))


    def goback(self):
        from checklog import Ui_CheckLogwindow
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_CheckLogwindow(self.message[0])
        self.ui.setupUi(self.window)
        self.window.show()
        self.showlogWindow.hide()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    showlogWindow = QtWidgets.QMainWindow()
    ui = Ui_showlogWindow()
    ui.setupUi(showlogWindow)
    showlogWindow.show()
    sys.exit(app.exec_())

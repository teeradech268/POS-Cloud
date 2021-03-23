# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from confirm import Ui_ConfirmWindow
from checklog import Ui_CheckLogwindow


class Ui_MainWindow(object):
    total = 0
    received = 0
    change = 0
    reset = 0


    def __init__(self,message):
        self.message = message

    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(771, 541)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, -20, 221, 111))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(640, 10, 47, 13))
        self.label_2.setObjectName("label_2")
        self.userid = QtWidgets.QLabel(self.centralwidget)
        self.userid.setGeometry(QtCore.QRect(680, 10, 47, 13))
        self.userid.setObjectName("userid")
        self.logoutbtn = QtWidgets.QPushButton(self.centralwidget)
        self.logoutbtn.setGeometry(QtCore.QRect(640, 40, 75, 23))
        self.logoutbtn.setObjectName("logoutbtn")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 110, 431, 351))
        self.tabWidget.setObjectName("tabWidget")
        self.hotmenu = QtWidgets.QWidget()
        self.hotmenu.setObjectName("hotmenu")
        self.btnHotEs = QtWidgets.QPushButton(self.hotmenu)
        self.btnHotEs.setGeometry(QtCore.QRect(20, 20, 111, 61))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnHotEs.setFont(font)
        self.btnHotEs.setObjectName("btnHotEs")
        self.btnHotAme = QtWidgets.QPushButton(self.hotmenu)
        self.btnHotAme.setGeometry(QtCore.QRect(150, 20, 111, 61))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnHotAme.setFont(font)
        self.btnHotAme.setObjectName("btnHotAme")
        self.btnHotCappu = QtWidgets.QPushButton(self.hotmenu)
        self.btnHotCappu.setGeometry(QtCore.QRect(290, 20, 111, 61))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnHotCappu.setFont(font)
        self.btnHotCappu.setObjectName("btnHotCappu")
        self.btnHotMocha = QtWidgets.QPushButton(self.hotmenu)
        self.btnHotMocha.setGeometry(QtCore.QRect(150, 130, 111, 61))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnHotMocha.setFont(font)
        self.btnHotMocha.setObjectName("btnHotMocha")
        self.btnHotLatte = QtWidgets.QPushButton(self.hotmenu)
        self.btnHotLatte.setGeometry(QtCore.QRect(20, 130, 111, 61))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnHotLatte.setFont(font)
        self.btnHotLatte.setObjectName("btnHotLatte")
        self.btnHotmacchi = QtWidgets.QPushButton(self.hotmenu)
        self.btnHotmacchi.setGeometry(QtCore.QRect(290, 130, 111, 61))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnHotmacchi.setFont(font)
        self.btnHotmacchi.setObjectName("btnHotmacchi")
        self.btnHotCocoa = QtWidgets.QPushButton(self.hotmenu)
        self.btnHotCocoa.setGeometry(QtCore.QRect(150, 240, 111, 61))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnHotCocoa.setFont(font)
        self.btnHotCocoa.setObjectName("btnHotCocoa")
        self.btnHotChoco = QtWidgets.QPushButton(self.hotmenu)
        self.btnHotChoco.setGeometry(QtCore.QRect(20, 240, 111, 61))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnHotChoco.setFont(font)
        self.btnHotChoco.setObjectName("btnHotChoco")
        self.btnHotMilk = QtWidgets.QPushButton(self.hotmenu)
        self.btnHotMilk.setGeometry(QtCore.QRect(290, 240, 111, 61))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnHotMilk.setFont(font)
        self.btnHotMilk.setObjectName("btnHotMilk")
        self.tabWidget.addTab(self.hotmenu, "")
        self.coldmenu = QtWidgets.QWidget()
        self.coldmenu.setObjectName("coldmenu")
        self.btnColdAme = QtWidgets.QPushButton(self.coldmenu)
        self.btnColdAme.setGeometry(QtCore.QRect(150, 20, 111, 61))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnColdAme.setFont(font)
        self.btnColdAme.setObjectName("btnColdAme")
        self.btnColdMilk = QtWidgets.QPushButton(self.coldmenu)
        self.btnColdMilk.setGeometry(QtCore.QRect(290, 240, 111, 61))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnColdMilk.setFont(font)
        self.btnColdMilk.setObjectName("btnColdMilk")
        self.btnColdLatte = QtWidgets.QPushButton(self.coldmenu)
        self.btnColdLatte.setGeometry(QtCore.QRect(20, 130, 111, 61))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnColdLatte.setFont(font)
        self.btnColdLatte.setObjectName("btnColdLatte")
        self.btnColdEs = QtWidgets.QPushButton(self.coldmenu)
        self.btnColdEs.setGeometry(QtCore.QRect(20, 20, 111, 61))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnColdEs.setFont(font)
        self.btnColdEs.setObjectName("btnColdEs")
        self.btnColdCappu = QtWidgets.QPushButton(self.coldmenu)
        self.btnColdCappu.setGeometry(QtCore.QRect(290, 20, 111, 61))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnColdCappu.setFont(font)
        self.btnColdCappu.setObjectName("btnColdCappu")
        self.btnColdCocoa = QtWidgets.QPushButton(self.coldmenu)
        self.btnColdCocoa.setGeometry(QtCore.QRect(150, 240, 111, 61))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnColdCocoa.setFont(font)
        self.btnColdCocoa.setObjectName("btnColdCocoa")
        self.btnColdMocha = QtWidgets.QPushButton(self.coldmenu)
        self.btnColdMocha.setGeometry(QtCore.QRect(150, 130, 111, 61))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnColdMocha.setFont(font)
        self.btnColdMocha.setObjectName("btnColdMocha")
        self.btnColdChoco = QtWidgets.QPushButton(self.coldmenu)
        self.btnColdChoco.setGeometry(QtCore.QRect(20, 240, 111, 61))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnColdChoco.setFont(font)
        self.btnColdChoco.setObjectName("btnColdChoco")
        self.btnColdMacchi = QtWidgets.QPushButton(self.coldmenu)
        self.btnColdMacchi.setGeometry(QtCore.QRect(290, 130, 111, 61))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnColdMacchi.setFont(font)
        self.btnColdMacchi.setObjectName("btnColdMacchi")
        self.tabWidget.addTab(self.coldmenu, "")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(480, 110, 261, 16))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(500, 400, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(480, 430, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(490, 450, 47, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(680, 400, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(680, 430, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(680, 460, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.lbltotal = QtWidgets.QLabel(self.centralwidget)
        self.lbltotal.setGeometry(QtCore.QRect(610, 400, 47, 13))
        self.lbltotal.setObjectName("lbltotal")
        self.lblchange = QtWidgets.QLabel(self.centralwidget)
        self.lblchange.setGeometry(QtCore.QRect(610, 460, 47, 13))
        self.lblchange.setObjectName("lblchange")
        self.btnpaid = QtWidgets.QPushButton(self.centralwidget)
        self.btnpaid.setGeometry(QtCore.QRect(650, 490, 75, 23))
        self.btnpaid.setObjectName("btnpaid")
        self.btncancel = QtWidgets.QPushButton(self.centralwidget)
        self.btncancel.setGeometry(QtCore.QRect(540, 490, 75, 23))
        self.btncancel.setObjectName("btncancel")
        self.btnlog = QtWidgets.QPushButton(self.centralwidget)
        self.btnlog.setGeometry(QtCore.QRect(550, 40, 75, 23))
        self.btnlog.setObjectName("btnlog")
        self.listWidgetMain = QtWidgets.QListWidget(self.centralwidget)
        self.listWidgetMain.setGeometry(QtCore.QRect(470, 130, 261, 261))
        self.listWidgetMain.setObjectName("listWidgetMain")
        self.linereceiv = QtWidgets.QLineEdit(self.centralwidget)
        self.linereceiv.setGeometry(QtCore.QRect(550, 430, 113, 20))
        self.linereceiv.setObjectName("linereceiv")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.btnColdEs.clicked.connect(self.btnCoEs)
        self.btnColdAme.clicked.connect(self.btnCoAme)
        self.btnColdCappu.clicked.connect(self.btnCoCap)
        self.btnColdLatte.clicked.connect(self.btnCoLat)
        self.btnColdMocha.clicked.connect(self.btnCoMoc)
        self.btnColdMacchi.clicked.connect(self.btnCoMac)
        self.btnColdChoco.clicked.connect(self.btnCoChoc)
        self.btnColdCocoa.clicked.connect(self.btnCoCoa)
        self.btnColdMilk.clicked.connect(self.btnCoFM)
        self.btnHotEs.clicked.connect(self.btnHoEs)
        self.btnHotAme.clicked.connect(self.btnHoAme)
        self.btnHotCappu.clicked.connect(self.btnHoCap)
        self.btnHotLatte.clicked.connect(self.btnHoLat)
        self.btnHotMocha.clicked.connect(self.btnHoMoc)
        self.btnHotmacchi.clicked.connect(self.btnHoMac)
        self.btnHotChoco.clicked.connect(self.btnHoChoc)
        self.btnHotCocoa.clicked.connect(self.btnHoCoa)
        self.btnHotMilk.clicked.connect(self.btnHoFM)

        self.linereceiv.textChanged.connect(self.calculatechange)

        self.btnpaid.clicked.connect(self.paid)
        self.btncancel.clicked.connect(self.cancle)
        self.btnlog.clicked.connect(self.checklog)
        self.logoutbtn.clicked.connect(self.logout)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TNI Coffee Shop"))
        self.label.setText(_translate("MainWindow", "TNI Coffee Cashier"))
        self.label_2.setText(_translate("MainWindow", "User : "))
        self.userid.setText(_translate("MainWindow", self.message))
        self.logoutbtn.setText(_translate("MainWindow", "Log Out"))
        self.btnHotEs.setText(_translate("MainWindow", "Espresso/35฿"))
        self.btnHotAme.setText(_translate("MainWindow", "Americano/35฿"))
        self.btnHotCappu.setText(_translate("MainWindow", "Cappuccino/40฿"))
        self.btnHotMocha.setText(_translate("MainWindow", "Mocha/40฿"))
        self.btnHotLatte.setText(_translate("MainWindow", "Latte/40฿"))
        self.btnHotmacchi.setText(_translate("MainWindow", "Macchiato/45฿"))
        self.btnHotCocoa.setText(_translate("MainWindow", "Cocoa/40฿"))
        self.btnHotChoco.setText(_translate("MainWindow", "Chocolate/40฿"))
        self.btnHotMilk.setText(_translate("MainWindow", "Fresh Milk/35฿"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.hotmenu), _translate("MainWindow", "Hot Menu"))
        self.btnColdAme.setText(_translate("MainWindow", "Americano/40฿"))
        self.btnColdMilk.setText(_translate("MainWindow", "Fresh Milk/40฿"))
        self.btnColdLatte.setText(_translate("MainWindow", "Latte/45฿"))
        self.btnColdEs.setText(_translate("MainWindow", "Espresso/40฿"))
        self.btnColdCappu.setText(_translate("MainWindow", "Cappuccino/45฿"))
        self.btnColdCocoa.setText(_translate("MainWindow", "Cocoa/45฿"))
        self.btnColdMocha.setText(_translate("MainWindow", "Mocha/45฿"))
        self.btnColdChoco.setText(_translate("MainWindow", "Chocolate/45฿"))
        self.btnColdMacchi.setText(_translate("MainWindow", "Macchiato/50฿"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.coldmenu), _translate("MainWindow", "Cold Menu"))
        self.label_3.setText(_translate("MainWindow", "menu                               Qty       Price"))
        self.label_4.setText(_translate("MainWindow", "Total"))
        self.label_5.setText(_translate("MainWindow", "Received"))
        self.label_6.setText(_translate("MainWindow", "Change"))
        self.label_7.setText(_translate("MainWindow", "Baht."))
        self.label_8.setText(_translate("MainWindow", "Baht."))
        self.label_9.setText(_translate("MainWindow", "Baht."))
        self.lbltotal.setText(_translate("MainWindow", str(self.total)))
        self.lblchange.setText(_translate("MainWindow", str(self.change)))
        self.btnpaid.setText(_translate("MainWindow", "Paid"))
        self.btncancel.setText(_translate("MainWindow", "Cancel"))
        self.btnlog.setText(_translate("MainWindow", "Log"))



    def logout(self):
        from login2 import Ui_Loginwindow
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Loginwindow()
        self.ui.setupUi(self.window)
        self.window.show()
        self.MainWindow.hide()


    def checklog(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_CheckLogwindow(self.message)
        self.ui.setupUi(self.window)
        self.window.show()
        self.MainWindow.hide()

    def cancle(self):

        self.lbltotal.setText(str(self.reset))
        self.lblchange.setText(str(self.reset))
        self.linereceiv.clear()
        try:
            self.listWidgetMain.clear()
        except Exception as e:
            print(e)

    def paid(self):
        self.window = QtWidgets.QMainWindow()
        item = [str(self.listWidgetMain.item(i).text()) for i in range(self.listWidgetMain.count())]
        username = self.message
        self.message = [item,self.total,self.received,self.change,username]
        self.ui = Ui_ConfirmWindow(self.message)
        self.ui.setupUi(self.window)
        self.window.show()
        self.MainWindow.hide()

    def calculatechange(self):
        try:
            self.received = self.linereceiv.text()
            self.change = int(self.received) - int(self.total)
            self.lblchange.setText(str(self.change))
        except Exception as e:
            print(e)

    def btnCoEs(self):
        text = "Espresso (Cold)                                 1               40"
        self.listWidgetMain.addItem(text)
        self.total += 40
        self.lbltotal.setText(str(self.total))

    def btnCoAme(self):
        text = "Americano (Cold)                             1               40"
        self.listWidgetMain.addItem(text)
        self.total += 40
        self.lbltotal.setText(str(self.total))

    def btnCoCap(self):
        text = "Cappuccino (Cold)                           1               45"
        self.listWidgetMain.addItem(text)
        self.total += 45
        self.lbltotal.setText(str(self.total))

    def btnCoLat(self):
        text = "Latte (Cold)                                        1               45"
        self.listWidgetMain.addItem(text)
        self.total += 45
        self.lbltotal.setText(str(self.total))

    def btnCoMoc(self):
        text = "Mocha (Cold)                                    1               45"
        self.listWidgetMain.addItem(text)
        self.total += 45
        self.lbltotal.setText(str(self.total))

    def btnCoMac(self):
        text = "Macchiato (Cold)                             1               50"
        self.listWidgetMain.addItem(text)
        self.total += 50
        self.lbltotal.setText(str(self.total))

    def btnCoChoc(self):
        text = "Chocolate (Cold)                              1               45"
        self.listWidgetMain.addItem(text)
        self.total += 45
        self.lbltotal.setText(str(self.total))

    def btnCoCoa(self):
        text = "Cocoa (Cold)                                     1               45"
        self.listWidgetMain.addItem(text)
        self.total += 45
        self.lbltotal.setText(str(self.total))

    def btnCoFM(self):
        text = "Fresh Milk (Cold)                              1               40"
        self.listWidgetMain.addItem(text)
        self.total += 40
        self.lbltotal.setText(str(self.total))

    def btnHoEs(self):
        text = "Espresso (Hot)                                  1               35"
        self.listWidgetMain.addItem(text)
        self.total += 35
        self.lbltotal.setText(str(self.total))

    def btnHoAme(self):
        text = "Americano (Hot)                              1               35"
        self.listWidgetMain.addItem(text)
        self.total += 35
        self.lbltotal.setText(str(self.total))

    def btnHoCap(self):
        text = "Cappuccino (Hot)                            1               40"
        self.listWidgetMain.addItem(text)
        self.total += 40
        self.lbltotal.setText(str(self.total))

    def btnHoLat(self):
        text = "Latte (Hot)                                         1               40"
        self.listWidgetMain.addItem(text)
        self.total += 40
        self.lbltotal.setText(str(self.total))

    def btnHoMoc(self):
        text = "Mocha (Hot)                                     1               40"
        self.listWidgetMain.addItem(text)
        self.total += 40
        self.lbltotal.setText(str(self.total))

    def btnHoMac(self):
        text = "Macchiato (Hot)                              1               45"
        self.listWidgetMain.addItem(text)
        self.total += 45
        self.lbltotal.setText(str(self.total))

    def btnHoChoc(self):
        text = "Chocolate (Hot)                               1               40"
        self.listWidgetMain.addItem(text)
        self.total += 40
        self.lbltotal.setText(str(self.total))

    def btnHoCoa(self):
        text = "Cocoa (Hot)                                      1               40"
        self.listWidgetMain.addItem(text)
        self.total += 40
        self.lbltotal.setText(str(self.total))

    def btnHoFM(self):
        text = "Fresh Milk (Hot)                               1               35"
        self.listWidgetMain.addItem(text)
        self.total += 35
        self.lbltotal.setText(str(self.total))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

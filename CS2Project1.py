# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CS2Project1.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from Window2CS2Project1 import Ui_SecondWindow
from Window2CS2Project1 import *

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 700)
        MainWindow.setMinimumSize(QtCore.QSize(700, 700))
        MainWindow.setMaximumSize(QtCore.QSize(700, 700))
        MainWindow.setStyleSheet("background-color: rgb(172, 215, 255);\n"
"border-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.bank_label = QtWidgets.QLabel(self.centralwidget)
        self.bank_label.setGeometry(QtCore.QRect(190, 30, 321, 71))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.bank_label.setFont(font)
        self.bank_label.setAlignment(QtCore.Qt.AlignCenter)
        self.bank_label.setObjectName("bank_label")
        self.username_input = QtWidgets.QLineEdit(self.centralwidget)
        self.username_input.setGeometry(QtCore.QRect(130, 230, 171, 41))
        self.username_input.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.username_input.setObjectName("username_input")
        self.username_label = QtWidgets.QLabel(self.centralwidget)
        self.username_label.setGeometry(QtCore.QRect(140, 170, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.username_label.setFont(font)
        self.username_label.setObjectName("username_label")
        self.password_input = QtWidgets.QLineEdit(self.centralwidget)
        self.password_input.setGeometry(QtCore.QRect(380, 230, 171, 41))
        self.password_input.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.password_input.setObjectName("password_input")
        self.password_label = QtWidgets.QLabel(self.centralwidget)
        self.password_label.setGeometry(QtCore.QRect(400, 170, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.password_label.setFont(font)
        self.password_label.setObjectName("password_label")
        self.signin_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.openWindow())
        self.signin_button.setGeometry(QtCore.QRect(200, 310, 281, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.signin_button.setFont(font)
        self.signin_button.setStyleSheet("background-color: rgb(99, 159, 255);")
        self.signin_button.setObjectName("signin_button")
        self.errormessage_label = QtWidgets.QLabel(self.centralwidget)
        self.errormessage_label.setGeometry(QtCore.QRect(150, 410, 371, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.errormessage_label.setFont(font)
        self.errormessage_label.setText("")
        self.errormessage_label.setAlignment(QtCore.Qt.AlignCenter)
        self.errormessage_label.setObjectName("errormessage_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.bank_label.setText(_translate("MainWindow", "Bank Sign In"))
        self.username_label.setText(_translate("MainWindow", "Username"))
        self.password_label.setText(_translate("MainWindow", "Password"))
        self.signin_button.setText(_translate("MainWindow", "Sign In"))



    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_SecondWindow()
        with open('UserCredentials', 'r') as one:
            for line in one:
                if line.startswith(str(self.username_input.text())):
                    password = line.split()[1]
                    if password == str(self.password_input.text()):
                        #amount = line.split()[3]
                        #self.balancenumber_label.setText('$'+str(amount))
                        self.ui.setupUi(self.window)
                        self.window.show()
                    else:
                        self.errormessage_label.setText('Error2- Username and/or Password do not match.')
                else:
                    self.errormessage_label.setText('Error- Username and/or Password do not match.')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

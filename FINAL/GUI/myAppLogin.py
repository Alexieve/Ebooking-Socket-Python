# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginUi.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Login(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(602, 565)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(30, 30, 550, 500))
        self.widget.setStyleSheet("#loginButton, #regButton, #changeButton{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"#loginButton:hover, #regButton:hover, #changeButton:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"\n"
"#loginButton:pressed, #regButton:pressed, #changeButton:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}\n"
"\n"
"")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(40, 30, 280, 430))
        self.label.setStyleSheet("border-image: url(:/images/261029.jpg);\n"
"border-top-left-radius: 50px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(40, 30, 280, 430))
        self.label_2.setStyleSheet("background-color:rgba(0, 0, 0, 80);\n"
"border-top-left-radius: 50px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(270, 30, 240, 430))
        self.label_3.setStyleSheet("background-color:rgba(255, 255, 255, 255);\n"
"border-bottom-right-radius: 50px;")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setGeometry(QtCore.QRect(280, 70, 220, 391))
        self.widget_3.setObjectName("widget_3")
        self.label_9 = QtWidgets.QLabel(self.widget_3)
        self.label_9.setGeometry(QtCore.QRect(36, 10, 141, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color:rgba(0, 0, 0, 200);")
        self.label_9.setObjectName("label_9")
        self.userRegInput = QtWidgets.QLineEdit(self.widget_3)
        self.userRegInput.setGeometry(QtCore.QRect(15, 80, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.userRegInput.setFont(font)
        self.userRegInput.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.userRegInput.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.userRegInput.setObjectName("userRegInput")
        self.regButton = QtWidgets.QPushButton(self.widget_3)
        self.regButton.setGeometry(QtCore.QRect(15, 330, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.regButton.setFont(font)
        self.regButton.setObjectName("regButton")
        self.passRegInput = QtWidgets.QLineEdit(self.widget_3)
        self.passRegInput.setGeometry(QtCore.QRect(15, 145, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.passRegInput.setFont(font)
        self.passRegInput.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.passRegInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passRegInput.setObjectName("passRegInput")
        self.confirmInput = QtWidgets.QLineEdit(self.widget_3)
        self.confirmInput.setGeometry(QtCore.QRect(15, 210, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.confirmInput.setFont(font)
        self.confirmInput.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.confirmInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmInput.setObjectName("confirmInput")
        self.cardIDInput = QtWidgets.QLineEdit(self.widget_3)
        self.cardIDInput.setGeometry(QtCore.QRect(15, 275, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cardIDInput.setFont(font)
        self.cardIDInput.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.cardIDInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.cardIDInput.setObjectName("cardIDInput")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setGeometry(QtCore.QRect(280, 70, 220, 315))
        self.widget_2.setObjectName("widget_2")
        self.label_4 = QtWidgets.QLabel(self.widget_2)
        self.label_4.setGeometry(QtCore.QRect(50, 10, 111, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:rgba(0, 0, 0, 200);")
        self.label_4.setObjectName("label_4")
        self.passLoginInput = QtWidgets.QLineEdit(self.widget_2)
        self.passLoginInput.setGeometry(QtCore.QRect(15, 145, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.passLoginInput.setFont(font)
        self.passLoginInput.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.passLoginInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passLoginInput.setObjectName("passLoginInput")
        self.userLoginInput = QtWidgets.QLineEdit(self.widget_2)
        self.userLoginInput.setGeometry(QtCore.QRect(15, 80, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.userLoginInput.setFont(font)
        self.userLoginInput.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.userLoginInput.setObjectName("userLoginInput")
        self.loginButton = QtWidgets.QPushButton(self.widget_2)
        self.loginButton.setGeometry(QtCore.QRect(15, 225, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.loginButton.setFont(font)
        self.loginButton.setObjectName("loginButton")
        self.changeButton = QtWidgets.QPushButton(self.widget)
        self.changeButton.setGeometry(QtCore.QRect(270, 80, 30, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.changeButton.setFont(font)
        self.changeButton.setStyleSheet("border-radius:0px;\n"
"border-top-right-radius:15px;\n"
"border-bottom-right-radius:15px;")
        self.changeButton.setCheckable(True)
        self.changeButton.setObjectName("changeButton")
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setGeometry(QtCore.QRect(49, 180, 211, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color:rgba(255, 255, 255, 170);")
        self.label_8.setObjectName("label_8")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(40, 90, 221, 81))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color:rgba(255, 255, 255, 200);")
        self.label_7.setObjectName("label_7")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(40, 80, 230, 161))
        self.label_6.setStyleSheet("background-color:rgba(0, 0, 0, 75);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.userLoginInput, self.passLoginInput)
        Form.setTabOrder(self.passLoginInput, self.loginButton)
        Form.setTabOrder(self.loginButton, self.changeButton)
        Form.setTabOrder(self.changeButton, self.userRegInput)
        Form.setTabOrder(self.userRegInput, self.passRegInput)
        Form.setTabOrder(self.passRegInput, self.confirmInput)
        Form.setTabOrder(self.confirmInput, self.cardIDInput)
        Form.setTabOrder(self.cardIDInput, self.regButton)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_9.setText(_translate("Form", "Register"))
        self.userRegInput.setPlaceholderText(_translate("Form", "  User Name"))
        self.regButton.setText(_translate("Form", "R e g i s t e r"))
        self.passRegInput.setPlaceholderText(_translate("Form", "  Password"))
        self.confirmInput.setPlaceholderText(_translate("Form", "  Confirm Password"))
        self.cardIDInput.setPlaceholderText(_translate("Form", "  Card ID"))
        self.label_4.setText(_translate("Form", "Log In"))
        self.passLoginInput.setPlaceholderText(_translate("Form", "  Password"))
        self.userLoginInput.setPlaceholderText(_translate("Form", "  User Name"))
        self.loginButton.setText(_translate("Form", "L o g  I n"))
        self.changeButton.setText(_translate("Form", ">"))
        self.label_8.setText(_translate("Form", "Welcome to HCMUS\n"
"E-booking system"))
        self.label_7.setText(_translate("Form", "E-BOOKING\n"
"SYSTEM"))
from GUI import res_rc
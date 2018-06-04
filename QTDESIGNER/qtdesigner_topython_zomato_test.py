# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'zomato_test.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_GroupBox(object):
    def setupUi(self, GroupBox):
        GroupBox.setObjectName(_fromUtf8("GroupBox"))
        GroupBox.resize(400, 300)
        self.label = QtGui.QLabel(GroupBox)
        self.label.setGeometry(QtCore.QRect(110, 20, 161, 31))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.widget = QtGui.QWidget(GroupBox)
        self.widget.setGeometry(QtCore.QRect(10, 80, 371, 151))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.lineEdit = QtGui.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(170, 20, 171, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(20, 23, 131, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.radioButton = QtGui.QRadioButton(self.widget)
        self.radioButton.setGeometry(QtCore.QRect(20, 60, 98, 19))
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.radioButton_2 = QtGui.QRadioButton(self.widget)
        self.radioButton_2.setGeometry(QtCore.QRect(130, 60, 98, 19))
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.radioButton_3 = QtGui.QRadioButton(self.widget)
        self.radioButton_3.setGeometry(QtCore.QRect(250, 60, 98, 19))
        self.radioButton_3.setObjectName(_fromUtf8("radioButton_3"))
        self.pushButton = QtGui.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(100, 100, 161, 24))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.retranslateUi(GroupBox)
        QtCore.QMetaObject.connectSlotsByName(GroupBox)

    def retranslateUi(self, GroupBox):
        GroupBox.setWindowTitle(_translate("GroupBox", "GroupBox", None))
        GroupBox.setTitle(_translate("GroupBox", "GroupBox", None))
        self.label.setText(_translate("GroupBox", "ZOMATO APP", None))
        self.label_2.setText(_translate("GroupBox", "RESTAURANT NAME:-", None))
        self.radioButton.setText(_translate("GroupBox", "Bangalore", None))
        self.radioButton_2.setText(_translate("GroupBox", "Mumbai", None))
        self.radioButton_3.setText(_translate("GroupBox", "Chennai", None))
        self.pushButton.setText(_translate("GroupBox", "Submit", None))


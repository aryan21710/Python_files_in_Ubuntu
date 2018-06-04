# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'zomato.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
#!/usr/bin/python3
from PyQt4 import QtCore, QtGui
from pyzomato import Pyzomato
import traceback
import sys
import zomato_script
import inspect




class Ui_GroupBox(object):
    def setupUi(self, GroupBox):
        GroupBox.setObjectName("GroupBox")
        GroupBox.resize(434, 435)
        GroupBox.setStyleSheet("QGroupBox { background-color: rgb(100, 255,255); border:1px solid rgb(255, 170, 255); }")

        # ADD GRIDS
        self.gridLayout_9 = QtGui.QGridLayout(GroupBox)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_5 = QtGui.QGridLayout()
        self.gridLayout_6 = QtGui.QGridLayout()
        self.gridLayout_7 = QtGui.QGridLayout()
        self.gridLayout_8 = QtGui.QGridLayout()

        # ADD THE GRID TO THE LAYOUT USING ADDLAYOUT
        self.gridLayout.addLayout(self.gridLayout_6, 0, 0, 1, 1)
        self.gridLayout_9.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_7, 4, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_8, 3, 0, 1, 1)

        # SET ALL THE WIDGETS UNDER GROUPBOX
        self.label = QtGui.QLabel(GroupBox)
        self.label_2 = QtGui.QLabel(GroupBox)
        self.label_3 = QtGui.QLabel(GroupBox)
        self.pushButton = QtGui.QPushButton(GroupBox)
        self.lineEdit = QtGui.QLineEdit(GroupBox)
        self.lineEdit_2 = QtGui.QLineEdit(GroupBox)
        self.textEdit = QtGui.QTextEdit(GroupBox)


        # SET EXTRA PROPERTIES OF ALL WIDGETS NOW
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)

        # SET TITLE AND TEXT OF THE WIDGETS
        self.setTitleText(GroupBox)

        # ADD THE WIDGETS TO THE GRIDLAYOUT
        self.gridLayout_6.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.lineEdit, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.label_3, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.lineEdit_2, 0, 0, 1, 1)
        self.gridLayout_8.addWidget(self.pushButton, 0, 0, 1, 1)
        self.gridLayout_7.addWidget(self.textEdit, 0, 0, 1, 1)


        # SET THE HORIZONTAL LAYOUT
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout_2 = QtGui.QHBoxLayout()

        # ADD THE HORIZONTAL LAYOUT TO THE GRID 
        self.horizontalLayout.addLayout(self.gridLayout_2)
        self.horizontalLayout.addLayout(self.gridLayout_3)
        self.horizontalLayout_2.addLayout(self.gridLayout_4)
        self.horizontalLayout_2.addLayout(self.gridLayout_5)


        # CLUB THE GRID TOGETHER AND ADD IT IN INSIDE THE HORIZONTAL LAYOUT USING ADDLAYOUT
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)

        # MAKE ADDITIONAL LAYOUT PROPERTIES SIZEPOLICY,HOR/VERTICAL STRETCHES,MAXLENGTH,DRAGENABLE
        sizePolicy_label2 = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy_label2.setHorizontalStretch(0)
        sizePolicy_label2.setVerticalStretch(0)
        sizePolicy_label2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy_btn = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)

        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)

        # APPLY THE PROPERTIES TO THE WIDGETS
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        sizePolicy_btn.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())

        self.label_2.setSizePolicy(sizePolicy_label2)
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.pushButton.setSizePolicy(sizePolicy_btn)

        self.lineEdit.setMaxLength(32791)
        self.lineEdit.setFrame(True)
        self.lineEdit.setDragEnabled(True)

        # SIGNALS AND EVENTS OF THE WIDGETS
        sig1=QtCore.SIGNAL("textChanged(QString)")
        self.pushButton.clicked.connect(self.searchZomato)
        QtCore.QMetaObject.connectSlotsByName(GroupBox)

    def setTitleText(self, GroupBox):
        GroupBox.setWindowTitle("GroupBox")
        GroupBox.setTitle("GroupBox")
        self.label.setText(" MY ZOMATO APP")
        self.label_2.setText(" NAME OF THE CITY :-")
        self.label_3.setText(" NAME OF THE RESTAURANT/PUB :-")
        self.pushButton.setText("SUBMIT")

    def searchZomato(self):
        self.cityName=str(self.lineEdit.text())
        self.restName=str(self.lineEdit_2.text())
        self.mykey='7dcf7b79d4c7bdfd5ffe013ae7361388'
        self.p=Pyzomato(self.mykey)
        print (dir(self.p))
        print ('*' * 100)
        print ('\n\n')
        print ('INSIDE FUNCTION:-',inspect.stack()[0][3])
        print ('CITY NAME AND RESTAURANT NAME\'S ARE "-',self.cityName,self.restName)
        print ('THE ZOMATO API OBJECT:=',self.p)
        print ('SEARCHING THE DATABASE FOR YOUR QUERY')
        print ('\n\n')
        try:
           self.cityId=self.p.getCityDetails(q=self.cityName)
           l=self.cityId['location_suggestions']
           for d in l:
               for k,v in d.items():
                   if k=='id':
                      self.cityId=d[k]
                      print ('CITY ID:-',self.cityId)

           self.details=self.p.search(q=self.restName,city=self.cityName,count=10,entity_id=self.cityId, entity_type='city')
           print ('\n\n THE DETAILS OF THE RESTAURANT ARE AS FOLLOWS:-',self.details)
           self.output=zomato_script.searchRestaurant(self.details,self.restName.upper())
           self.processOutput(self.output)
        except Exception as exc:
           print ('INVALID DETAILS ENTERED:-',exc)
           print ('TRACEBACK :-',traceback.format_exc())

    def processOutput(self,output):
        f=open('zomato_rest_output.txt')
        a=f.read()
        self.textEdit.setText(a)
        f.close()


def main():
    app = QtGui.QApplication(sys.argv)
    GroupBox = QtGui.QGroupBox()
    ui = Ui_GroupBox()
    ui.setupUi(GroupBox)
    GroupBox.show()
    sys.exit(app.exec_())
    print ('ZOMATO API OBJECT CREATED:-',p)

if __name__ == "__main__":
   main()

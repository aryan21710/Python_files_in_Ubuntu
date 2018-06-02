from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
import os,os.path

print('PWD:-',os.getcwd())



class MainWindow(QMainWindow):

    def __init__(self,parent=None):
       super(MainWindow,self).__init__(parent)
       self.setGeometry(10,10,500,500)
       self.setWindowTitle('MY MESSAGE')
       if os.path.getsize('/home/ary/PycharmProjects/Python_files_in_Ubuntu/PyQt-Gui/pythonlogo.png') > 0:
          print ('SET THE ICON NOW...')
          self.setWindowIcon(QIcon('/home/ary/PycharmProjects/Python_files_in_Ubuntu/PyQt-Gui/pythonlogo.png'))


       btn=QPushButton(self)
       btn.setText('QUIT')
       btn.resize(50,50)
       btn.move(0,50)
       btn.clicked.connect(self.btnAction)

       s=self.statusBar()
       s.showMessage('MY STATUSBAR',0)
       bar=self.menuBar()
       # THE & SETS THE ALT+F AS THE SHORTCUT KEY
       file=bar.addMenu('&File')
       file.addAction('MessageBox')
       file.addAction('TextEditBox')
       edit=bar.addMenu('&Edit')
       view=bar.addMenu('&View')
       #file.addAction(self.myaction)
       file.triggered[QAction].connect(self.myaction)


       self.show()

    def btnAction(self):
        print ('CLOSING THE APP:-')
        sys.exit()


    def myaction(self,q):
        # Creating a main window without a central widget is not supported.
        # You must have a central widget even if it is just a placeholder.
        if q.text()=='MessageBox':
           self.msg=QMessageBox(self)
           self.setCentralWidget(self.msg)
           self.msg.move(50,50)
           self.msg.setWindowTitle('MSG BOX')
           self.msg.setText('YOU GOT A MESSAGE JAANU')
           self.msg.setInformativeText('PRESS SHOW_DETAILS TO C UR MSG :)')
           self.msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel | QMessageBox.Close)
           self.msg.setIcon(QMessageBox.Information)
           self.msg.setDetailedText('WHAT TIME I CAN FUCK U TONIGHT????')
           self.msg.exec_()
        elif q.text()=='TextEditBox':
           #self.inp=raw_input('ENTER THE TEXT YOU WANT TO ENTER:-')

           f=open('/home/ary/PycharmProjects/Python_files_in_Ubuntu/PyQt-Gui/tempTextEditFile')
           fileText=f.read()
           self.textEdit=QTextEdit(fileText,self)
           self.setCentralWidget(self.textEdit)
           self.textEdit.exec_()

           while(False):
               if 'EXIT' not in self.inp.upper():

                   self.textEdit=QTextEdit(fileText,self)
                   self.setCentralWidget(self.textEdit)
                   self.textEdit.exec_()
               else:
                   break


obj=QApplication(sys.argv)
Gui=MainWindow()
sys.exit(obj.exec_())

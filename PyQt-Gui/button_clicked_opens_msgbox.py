from PyQt4 import QtGui
import sys


def OpenMessageBox():
    m=QtGui.QMessageBox()
    m.move(300,300)
    m.setWindowTitle('MY MESSAGE BOX')
    m.setText('THIS IS MY MESSAGE BOX')
    m.setIcon(QtGui.QMessageBox.Information)
    m.setInformativeText('ADDITIONAL MESSAGE BOX OPTIONS')
    m.setStandardButtons(QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel | QtGui.QMessageBox.Save)
    m.setDefaultButton(QtGui.QMessageBox.Save)
    m.setDetailedText('MESSAGE BOX PROGRAM CONFIGURED AND CREATED USING PYQT4')
    m.buttonClicked.connect(OpenMsgBtn)
    retval=m.exec_()
    print ('VALUE OF PRESSED MSG BOX BTN:-',retval)

def OpenMsgBtn(i):
    print ('BUTTON PRESSED:-',i.text())

# SET THE APP FIRST.
app=QtGui.QApplication(sys.argv)

# SET THE OUTER WIDGET/CONTAINER, ITS DIMENSION and ITS TITLE .
w=QtGui.QWidget()
w.setGeometry(50,50,200,200)
w.setWindowTitle('TEST WIDGET')

# SET THE BUTTON, ITS DIMENSION AND FUNCTION IT WILL CALLED WHEN CLICKED
b=QtGui.QPushButton(w)
b.setText('BTN1')
b.move(50,50)
b.clicked.connect(OpenMessageBox)

# MAKE WIDGET APPEAR/VISIBLE ON THE SCREEN
w.show()

sys.exit(app.exec_())

from PyQt4 import QtGui
from PyQt4.QtCore import *

import sys

def OpenDialog():
    q=QtGui.QDialog()
    q.setWindowTitle('TEST DIALOG WINDOW')
    # WINDOW MODALITY IS MODAL OR MODELESS
    q.setWindowModality(Qt.ApplicationModal)
    #q.setGeometry(150,150,200,200)
    r=QtGui.QRadioButton(q)
    r.setText('RADIO BTN1')
    r.move(20,20)
    # NEEDED TO APPEAR THIS ON THE SCREEN
    q.exec_()


# LETS MAKE THE OUTER WIDGET/CONTAINER
app=QtGui.QApplication(sys.argv)
w=QtGui.QWidget()

# SET THE DIMENSION OF THE WIDGET
w.setGeometry(100,100,400,400)

# SET THE TITLE OF THE WIDGET

w.setWindowTitle('TEST WIDGET')
# CONFIGURE A BUTTON INSIDE THE WIDGET/CONTAINER.

b=QtGui.QPushButton(w)
b.setText('Button1')

# WHEN THE BUTTON IS CLICKED, IT WILL OPEN A DIALOG WINDOW.
b.clicked.connect(OpenDialog)

# LOCATION/DIMENSION OF THE BUTTON INSIDE THE WIDGET
b.move(30,30)

# TO MAKE THE WIDGET APPEAR ON THE SCREEN. CALL THE SHOW METHOD ON IT.
# THIS SHOULD BE THE LAST STATEMENT IN THE PROGRAM
w.show()

sys.exit(app.exec_())






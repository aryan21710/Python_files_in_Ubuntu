import sys
from PyQt4 import QtGui

def close():
    print ('CLOSING THE APP')
    sys.exit()

obj=QtGui.QApplication(sys.argv)

window=QtGui.QWidget()
btn=QtGui.QPushButton(window)
btn.setText('CLICK TO EXIT')
btn.resize(100,100)
btn.move(10,10)
btn.clicked.connect(close)

l=QtGui.QLabel(window)
l.setText('hello world')
l.move(100,120)

window.setGeometry(50,50,300,300)
window.setWindowTitle('MY 1ST PYQT APP')
window.show()

sys.exit(obj.exec_())
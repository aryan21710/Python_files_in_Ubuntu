

from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys


class MainWindow(QWidget):

	def __init__(self):
		super(MainWindow,self).__init__()
		self.setGeometry(10,10,200,200)
		self.setWindowTitle('HBOX & VBOX TOGETHER')

		grid=QGridLayout()
		grid.addWidget(QLabel('HBOX'),2,15)
		grid.addWidget(self.mylayout1(),6,10)
		grid.addWidget(self.mylayout1(),6,30)
		self.setLayout(grid)

	def mylayout1(self):
		grp=QGroupBox('VBOX')
		l1=QPushButton('BTN1')
		l2=QPushButton('BTN2')
		l3=QRadioButton('RDOBTN1')
		l3.setChecked(True)
		vbox=QVBoxLayout()
		vbox.addWidget(l1)
		vbox.addWidget(l2)
		vbox.addWidget(l3)
		vbox.addStretch(1)
		grp.setLayout(vbox)
		return grp


def main():
	app=QApplication(sys.argv)
	Gui=MainWindow()
	Gui.show()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()




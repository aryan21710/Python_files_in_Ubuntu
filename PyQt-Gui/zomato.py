from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys


class Mainwindow(QWidget):
	def __init__(self):
		super(Mainwindow,self).__init__()
		q=QGroupBox()
		self.q.setGeometry()
		self.q.setWindowTitle('MY ZOMATO APP')
		g=QGridLayout(self.q)

		l=QLabel(self.q)





def main():
	app=QApplication(sys.argv)
	Gui=Mainwindow()
	Gui.show()
	sys.exit(app.exec_())

if __name__=='__main__':
	main()
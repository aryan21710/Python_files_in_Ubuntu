from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys


class MainWindow(QWidget):


	def __init__(self,parent=None):
		super(MainWindow,self).__init__(parent)
		grid=QGridLayout()
		grid.addWidget(self.group1(),0,0)
		self.setLayout(grid)
		self.setGeometry(10,10,300,300)
		self.move(100,100)
		self.setWindowTitle('***MY ZOMATO APP***')
		self.setWindowIcon(QIcon('/home/ary/PycharmProjects/Python_files_in_Ubuntu/PyQt-Gui/pythonlogo.png')





	def group1(self):

		grp=QGroupBox('BIKES')
		rdo1= QRadioButton('DUCATI MULTISTRADA')
		rdo2= QRadioButton('TRIUMPH TIGER XCA')
		rdo3= QRadioButton('BMW GS')

		vbox=QVBoxLayout()
		vbox.addWidget(rdo1)
		vbox.addWidget(rdo2)
		vbox.addWidget(rdo2)

		vbox.addStretch(0)
		grp.setLayout(vbox)
		return grp






def main():
	app=QApplication(sys.argv)
	Gui=MainWindow()
	Gui.show()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()

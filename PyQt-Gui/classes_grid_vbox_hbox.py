from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys


class MainWindow(QWidget):


	def __init__(self,parent=None):
		super(MainWindow,self).__init__(parent)

		self.setGeometry(10,10,400,400)
		#self.move(100,100)
		self.setWindowTitle('***MY ZOMATO APP***')
		self.setWindowIcon(QIcon('/home/ary/PycharmProjects/Python_files_in_Ubuntu/PyQt-Gui/pythonlogo.png'))
		#self.resize(300,300)

		self.l1=QLabel('MODEL:')

		self.l4=QLineEdit()
		self.l4.setPlaceholderText('ENTER TEXT')

		grid=QGridLayout()
		#grid.setColumnStretch(1, 3)
		#grid.setColumnMinimumWidth(2,2)
		#grid.setColumnStretch(2, 2)
		grid.addWidget(self.l1,1,0)
		grid.addWidget(self.l4,1,1)
		grid.addWidget(self.createGroup1(),2,0)
		grid.addWidget(self.createGroup2(),3,0)
		self.setLayout(grid)



	def createGroup1(self):
		grp=QGroupBox('BIKES')
		rdo1= QRadioButton('&DUCATI MULTISTRADA')
		rdo2= QRadioButton('&TRIUMPH TIGER XCA')
		rdo3= QRadioButton('&BMW GS')
		rdo1.setChecked(True)

		hbox=QHBoxLayout()
		hbox.addWidget(rdo1)
		hbox.addWidget(rdo2)
		hbox.addWidget(rdo3)

		hbox.addStretch(1)
		grp.setLayout(hbox)
		return grp

	def createGroup2(self):

		grp1=QGroupBox('WATCHES')

		l1=QCheckBox('GEAR S3')
		l2=QPushButton('FOSSIL')
		l3=QRadioButton('KENNETH COLE')



		vbox=QVBoxLayout()
		vbox.addWidget(l1)
		vbox.addWidget(l2)
		vbox.addWidget(l3)
		vbox.addStretch(0)

		grp1.setLayout(vbox)
		return grp1


def main():
	app=QApplication(sys.argv)
	Gui=MainWindow()
	Gui.show()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()

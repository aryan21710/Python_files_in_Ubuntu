
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys

class Mainwindow(QWidget):
      def __init__(self):
          super(Mainwindow,self).__init__()
          self.q=QGroupBox()
          self.q.resize(400,300)
          self.setupUi()
          self.q.show()


      def setupUi(self):
          self.label=QLabel(self.q)
          self.label.setText('MY ZOMATO APP')
          self.label.setGeometry(QRect(110, 20, 161, 31))
          self.label.setAlignment(Qt.AlignCenter)

          self.widget=QWidget(self.q)
          self.widget.setGeometry(QRect(10,80,370,150))

          self.line=QLineEdit(self.widget)
          self.line.setGeometry(QRect(170,20,170,20))

          self.label2=QLabel(self.widget)
          self.label2.setText('RESTAURANT NAME')
          self.label2.setGeometry(QRect(20,25,170,20))

          self.rdo1=QRadioButton(self.widget)
          self.rdo1.setText('Bangalore')
          self.rdo1.setGeometry(QRect(20,60,98,19))
          self.rdo2=QRadioButton(self.widget)
          self.rdo2.setText('Mumbai')
          self.rdo2.setGeometry(QRect(130,60,98,19))

          self.rdo3=QRadioButton(self.widget)
          self.rdo3.setText('Chennai')
          self.rdo3.setGeometry(QRect(250,60,98,19))





def main():
    app = QApplication(sys.argv)
    ex = Mainwindow()
    #ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
   main()
import sys
import json
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

class MyWindow(QMainWindow):
	def __init__(self):
		super(MyWindow, self).__init__()

		self.setGeometry(200,200,600,600)
		self.setWindowTitle("Serial Dashboard")

		self.initUI()

	def initUI(self):
		self.label = QtWidgets.QLabel(self)
		self.label.setText("Hello World")
		self.label.move(50,50)

		self.connectButton = QtWidgets.QPushButton(self)
		self.connectButton.setText("Connect to device")
		self.connectButton.move(550,550)
		self.connectButton.clicked.connect(self.clicked)

	def clicked(self):
		self.label.setText("Connecting...")
		self.update()

	def update(self):
		self.label.adjustSize()


def window():
	app = QApplication(sys.argv)
	window = MyWindow()
	window.show()
	sys.exit(app.exec_())

window()

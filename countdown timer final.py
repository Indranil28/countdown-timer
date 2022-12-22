# importing important libraries
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class Window(QMainWindow):

	def __init__(self):
		super().__init__()

		# setting title,geometry,calling method and showing all the widgets
		self.setWindowTitle("timer")

		
		self.setGeometry(200, 200, 400, 600)

		
		self.UiComponents()

		
		self.show()

	# method for widgets
	def UiComponents(self):

		
		# count variable,adding flag,creating push button and setting geometry of the button
		self.count = 0

		
		self.start = False

		
		b = QPushButton("Set time", self)

		b.setGeometry(125, 100, 150, 50)

		b.clicked.connect(self.get_seconds)

		# creating label and setting its geometry
		self.label = QLabel("00", self)

		
		self.label.setGeometry(100, 200, 200, 50)

		# setting border to label and font to the label and setting alignment to the label
		self.label.setStyleSheet("border : 3px solid blue")

		
		self.label.setFont(QFont('Times', 15))

		
		self.label.setAlignment(Qt.AlignCenter)

		# creating start button,making its geometry and adding action to the button
		start = QPushButton("Start", self)

		
		start.setGeometry(125, 350, 150, 40)

		
		start.clicked.connect(self.start_action) 
        
       

        # creating pause button,making its geometry and adding action to the button
		pause = QPushButton("Pause", self)

		
		pause.setGeometry(125, 400, 150, 40)

		pause.clicked.connect(self.pause_action)
            
        
        
		# creating reset button,making its geometry and adding action to the button
		reset = QPushButton("Reset", self)

		reset.setGeometry(125, 450, 150, 40)

		
		reset.clicked.connect(self.reset_action)

		# creating a timer object,adding action to timer and updating timer every tenth second
		timer = QTimer(self)

		timer.timeout.connect(self.showTime)

		
		timer.start(100)

	


	# method called by the push button and making flag false 
	def get_seconds(self):

		
		self.start = False

		# getting seconds and flag, if flag is true then change the value of the count
		second, done = QInputDialog.getInt(self, 'Seconds', 'Enter in Seconds:')

		
		if done:
			
			self.count = second * 10

			# setting text to the label
			self.label.setText(str(second))

    #start and resume is done through same function
	def start_action(self):
		# making flag true
		self.start = True

		# count = 0
		if self.count == 0:
			self.start = False
            
    #def resume_action(self):
		# making flag true
	#	self.start = True

		# count = 0
	#	if self.count == 0:
	#		self.start = False

	def pause_action(self):

		# making flag false
		self.start = False

	def reset_action(self):

		# making flag false
		self.start = False

		# setting count value to 0
		self.count = 0

		# setting label text
		self.label.setText("00")
    # method called by timer
	def showTime(self):

		# checking if flag is true and incrementing the counter
		if self.start:
			
			self.count -= 1

			# timer is completed and flag is false
			if self.count == 0:

				
				self.start = False

				# setting text to the label
				self.label.setText("Completed !!!! ")

		if self.start:
			# getting text from count,and showing text
			text = str(self.count / 10) + " s"

			self.label.setText(text)


# create pyqt5 app,instance of the Window and starting the app
App = QApplication(sys.argv)


window = Window()


sys.exit(App.exec())

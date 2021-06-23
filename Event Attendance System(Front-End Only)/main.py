import sys
import platform
from more_itertools import unique_everseen

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import * 
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


from uS_splash import Ui_US_splash

from ui_main import Ui_MainWindow

from ui_functions import *



counter = 0


class MainWindow(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

		self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
		self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

		self.ui.tool_btn_close.clicked.connect(self.close)
		self.ui.tool_btn_min.clicked.connect(self.showMinimized)

		self.ui.tool_btn_scrn_adjust.clicked.connect(lambda: UIFunctions.windowMax(self))

		self.ui.home_search_bar.textChanged['QString'].connect(lambda: UIFunctions.homePageFunctions(self))

		self.ui.home_btn_clear.clicked.connect(lambda: UIFunctions.clearHomeFields(self))

		UIFunctions.center(self)

		
		self.ui.menu_btn_toggle.clicked.connect(lambda: UIFunctions.toggleMenu(self,250,True))

		def moveWindow(event):
			if UIFunctions.returnStatus() == 1:
				UIFunctions.windowMax(self)

			if event.buttons() == Qt.LeftButton:
				self.move(self.pos() + event.globalPos() - self.dragPos)
				self.dragPos = event.globalPos()
				event.accept()


		self.ui.frame_toolbar_label.mouseMoveEvent = moveWindow

		
		UIFunctions.pages(self)
		UIFunctions.dateTime(self)
		UIFunctions.graph(self)
		UIFunctions.homePageFunctions(self)




























	def mousePressEvent(self, event):
		self.dragPos = event.globalPos()
		if event.buttons() == Qt.LeftButton:
			print('Mouse click: LEFT CLICK')
		if event.buttons() == Qt.RightButton:
			print('Mouse click: RIGHT CLICK')
		if event.buttons() == Qt.MidButton:
			print('Mouse click: MIDDLE BUTTON')


	def keyPressEvent(self, event):
		print('Key: ' + str(event.key()) + ' | Text Press: ' + str(event.text()))

class splashScreen(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		self.ui = Ui_US_splash()
		self.ui.setupUi(self)


		self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
		self.setAttribute(QtCore.Qt.WA_TranslucentBackground)




		self.shadow = QGraphicsDropShadowEffect(self)
		self.shadow.setBlurRadius(100)
		self.shadow.setXOffset(5)
		self.shadow.setYOffset(5)
		self.shadow.setColor(QColor(0, 0, 0, 100))
		self.ui.frame.setGraphicsEffect(self.shadow)


		self.timer = QTimer()
		self.timer.timeout.connect(self.progress)

		## TIMER IN MILLISECONDS
		self.timer.start(15)

		self.show()

		## APP FUNCTIONS
	def progress(self):

		global counter

		## SET VALUE TO PROGRESSA BAR
		self.ui.progressBar.setValue(counter)


		## CLOSE SPLASH SCREEN AND OPEN APP
		if counter > 100:
			# STOP TIMER
			self.timer.stop()

			#Show app window
			self.main = MainWindow()
			self.main.show()

			## CLOSE SPLASH SCREEN
			self.close()

		## INCREASE COUNTER
		counter += 1








if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = splashScreen()
	sys.exit(app.exec_())
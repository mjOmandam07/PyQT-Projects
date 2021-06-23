from main import *

from backend_functions import *
from ui_graph import *
from datetime import datetime



full_screen_status = 0

class UIFunctions(MainWindow):

	###### TOGGLES THE BURGER MENU ############

	def toggleMenu(self, maxWidth, enable):
		_translate = QtCore.QCoreApplication.translate
		if enable:
			# GET WIDTH
			width = self.ui.frame_menu.width()
			maxExtend = maxWidth
			standard = 80
			# SET MAX WIDTH
			if width == 80:
				widthExtended = maxExtend
			else:
				widthExtended = standard
			# ANIMATION
			self.animation = QPropertyAnimation(self.ui.frame_menu, b"minimumWidth")
			self.animation.setDuration(300)
			self.animation.setStartValue(width)
			self.animation.setEndValue(widthExtended)
			self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
			self.animation.start()


	##### TIME AND DATE OF UI ########
	def dateTime(self):
		_translate = QtCore.QCoreApplication.translate
		date = datetime.today().strftime('%b %d, %Y')
		time = datetime.now().strftime("%I:%M %p")

		self.ui.top_label_time.setText(time)
		self.ui.top_label_date.setText(date)


	def graph(self):
		UIGraph.statBar(self)
		UIGraph.conCheckBar(self)




	###### CENTERS THE APP  ######

	def center(self):
		screen = QtGui.QGuiApplication.screenAt(QtGui.QCursor().pos())
		fg = self.frameGeometry()
		fg.moveCenter(screen.geometry().center())
		self.move(fg.topLeft())



	##### RETURNS THE CURRENT WINDOW SIZE STATUS #######

	def returnStatus():
		return full_screen_status





	##### WINDOW MAX OR NORMAL SIZE TOGGLE ######

	def windowMax(self):
		global full_screen_status
		status = full_screen_status

		if status == 0:
			self.showFullScreen()
			full_screen_status = 1
			icon1 = QtGui.QIcon()
			icon1.addPixmap(QtGui.QPixmap(":/newPrefix/images/cil-window-restore.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
			self.ui.tool_btn_scrn_adjust.setIcon(icon1)
		else:
			full_screen_status = 0
			self.showNormal()
			icon1 = QtGui.QIcon()
			icon1.addPixmap(QtGui.QPixmap(":/newPrefix/images/cil-window-maximize.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
			self.ui.tool_btn_scrn_adjust.setIcon(icon1)



	###### PAGES ON THE WIDGET ##########

	def pages(self):
		def page_one():
			self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
		def page_two():
			self.ui.stackedWidget.setCurrentWidget(self.ui.page_stat)
		def page_three():
			self.ui.stackedWidget.setCurrentWidget(self.ui.page_attndce_today)
		def page_four():
			self.ui.stackedWidget.setCurrentWidget(self.ui.page_conCheck)
		self.ui.menu_btn_home.clicked.connect(page_one)
		self.ui.menu_btn_stat.clicked.connect(page_two)
		self.ui.menu_btn_attndnce.clicked.connect(page_three)
		self.ui.menu_btn_conCheck.clicked.connect(page_four)

	def clearHomeFields(self):
		try:
			self.ui.home_lineEdit_firstName.clear()
			self.ui.home_lineEdit_LastName.clear()
			self.ui.home_search_bar.clear()
			self.ui.home_lineEdit_phoneNumber.setText("0")
			self.ui.home_lineEdit_birthday.setText("0001-01-01")
			self.ui.home_btn_delete.setDisabled(True)
			self.ui.home_btn_present.setDisabled(True)
		except Exception:
			raise Exception


	def homePageFunctions(self):
		backend_functions.homeFunctions(self)

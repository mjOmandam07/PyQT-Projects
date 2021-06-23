from main import *
from player_functions import *

full_screen_status = False
class UIFunctions(MainWindow):
	def windowMax(self):
		global full_screen_status
		status = full_screen_status

		if status == False:
			self.showFullScreen()
			full_screen_status = True
			icon = QtGui.QIcon()
			icon.addPixmap(QtGui.QPixmap("icons/16x16/cil-window-restore.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
			self.ui.btn_maximize_restore.setIcon(icon)
		else:
			full_screen_status = False
			self.showNormal()
			icon = QtGui.QIcon()
			icon.addPixmap(QtGui.QPixmap("icons/16x16/cil-window-maximize.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
			self.ui.btn_maximize_restore.setIcon(icon)

	def returnStatus(self):
		return full_screen_status
		
	def uiDefinitions(self):
		screen = QtGui.QGuiApplication.screenAt(QtGui.QCursor().pos())
		fg = self.frameGeometry()
		fg.moveCenter(screen.geometry().center())
		self.move(fg.topLeft())

		self.ui.btn_close.clicked.connect(self.close) 
		self.ui.btn_minimize.clicked.connect(self.showMinimized)
		self.ui.btn_maximize_restore.clicked.connect(lambda: UIFunctions.windowMax(self))

		self.sizegrip = QSizeGrip(self.ui.frame_9)
		self.sizegrip.setStyleSheet("width: 20px; height: 20px; margin 0px; padding: 0px; background-color:white;")

		self.ui.selectButton.clicked.connect(lambda: playerFunctions.open_file(self))


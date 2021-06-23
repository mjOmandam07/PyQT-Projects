import sys
import os
from os.path import expanduser
import platform
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import * 
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtMultimedia import *

from musicPlayer_ui import Ui_MainWindow
from appModules import *

class MainWindow(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

		self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
		self.setAttribute(QtCore.Qt.WA_TranslucentBackground)



		def moveWindow(event): # TO BE ABLE TO DRAG THE WINDOW
			if UIFunctions.returnStatus(self):
				UIFunctions.windowMax(self)

			if event.buttons() == Qt.LeftButton:
				self.move(self.pos() + event.globalPos() - self.dragPos)
				self.dragPos = event.globalPos()
				event.accept()


		self.ui.frame_label_top_btns.mouseMoveEvent = moveWindow
		UIFunctions.uiDefinitions(self)
		

		self.player = QMediaPlayer()
		self.playlist = QMediaPlaylist()
		self.player.setPlaylist(self.playlist)

		playerFunctions.songChanged(self)
		
		self.ui.playButton.clicked.connect(lambda: playerFunctions.play(self))
		self.ui.prevButton.clicked.connect(lambda: playerFunctions.previous(self))
		self.ui.nextButton.clicked.connect(lambda: playerFunctions.next(self))

		self.model = PlaylistModel(self.playlist)
		self.ui.playlistView.setModel(self.model)
		self.playlist.currentIndexChanged.connect(lambda: playerFunctions.playlist_position_changed(self, self.playlist.currentIndex()) )
		selection_model = self.ui.playlistView.selectionModel()
		selection_model.selectionChanged.connect(self.playlist_selection_changed)

		self.player.durationChanged.connect(self.update_duration)
		self.player.positionChanged.connect(self.update_position)
		self.ui.horizontalSlider.valueChanged.connect(self.player.setPosition)
		
		self.show()

	def playlist_selection_changed(self, index):
		i = index.indexes()[0].row()
		self.playlist.setCurrentIndex(i)
		playerFunctions.play(self)


	def update_duration(self, duration):
		self.ui.horizontalSlider.setMaximum(duration)
		if duration >= 0:
			self.ui.end_label.setText(playerFunctions.time(self, duration))

	def update_position(self, position):
		if position >= 0:
			self.ui.start_label.setText(playerFunctions.time(self, position))
		self.ui.horizontalSlider.blockSignals(True)
		self.ui.horizontalSlider.setValue(position)
		self.ui.horizontalSlider.blockSignals(False)


	def mousePressEvent(self, event):
		self.dragPos = event.globalPos()
		







if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = MainWindow()
	sys.exit(app.exec_())
from main import *



class PlaylistModel(QAbstractListModel):
    def __init__(self, playlist, *args, **kwargs):
        super(PlaylistModel, self).__init__(*args, **kwargs)
        self.playlist = playlist

    def data(self, index, role):
        if role == Qt.DisplayRole:
            media = self.playlist.media(index.row())

            return media.canonicalUrl().fileName()

    def rowCount(self, index):
        return self.playlist.mediaCount()



class playerFunctions(MainWindow):
	def time(self, ms):
		m, r = divmod(ms, 60000)
		s, _ = divmod(r, 1000)
		return ("%d:%02d" % (m,s))

	def playlist_position_changed(self, i):
		if i > -1:
			ix = self.model.index(i)
			self.ui.playlistView.setCurrentIndex(ix)

	def open_file(self):
		input_dir = QFileDialog.getExistingDirectory(None, 'Select a folder:', expanduser("~"))
		valid_file = 0
		if input_dir:
			for file in os.listdir(input_dir):
				if file.endswith(".mp3"):
					valid_file += 1
		else:
			pass
		if input_dir and valid_file > 0:
			self.player.stop()
			self.playlist.clear()
			for file in os.listdir(input_dir):
				if file.endswith(".mp3"):
					path = os.path.join(input_dir, file)
					self.playlist.addMedia(
						QMediaContent(
							QUrl.fromLocalFile(path)
							)
						)
			playerFunctions.play(self)
			self.model.layoutChanged.emit()
		elif input_dir and valid_file == 0:
			playerFunctions.messagePop(self)
		else:
			pass
		

	def togglePause(self):
		if self.player.state() == QMediaPlayer.PlayingState:
			icon = QtGui.QIcon()
			icon.addPixmap(QtGui.QPixmap("icons/24x24/cil-media-pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
			self.ui.playButton.setIcon(icon)
			self.ui.playButton.clicked.connect(lambda: playerFunctions.pause(self))
		else:
			icon = QtGui.QIcon()
			icon.addPixmap(QtGui.QPixmap("icons/24x24/cil-media-play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
			self.ui.playButton.setIcon(icon)
			self.ui.playButton.clicked.connect(lambda: playerFunctions.play(self))

	def songChanged(self):
		playing = self.playlist.currentMedia()
		if not playing.isNull():
			self.ui.songLabel.setText(playing.canonicalUrl().fileName())
		else:
			self.ui.songLabel.setText("Select Your favourite Music Directory to Start Listening")
			

	def indexCheck(self):
		if self.playlist.currentIndex() == (self.playlist.mediaCount() - 1):
			self.ui.nextButton.setDisabled(True)
			self.ui.prevButton.setDisabled(False)
		elif self.playlist.currentIndex() == 0:
			self.ui.prevButton.setDisabled(True)
			self.ui.nextButton.setDisabled(False)
		else:
			self.ui.nextButton.setDisabled(False)
			self.ui.prevButton.setDisabled(False)

	def play(self):
		self.player.play()
		playerFunctions.togglePause(self)
		playerFunctions.indexCheck(self)
		playerFunctions.songChanged(self)
			

	def pause(self):
		self.player.pause()
		playerFunctions.togglePause(self)
		playerFunctions.indexCheck(self)

	def next(self):
		self.playlist.next()
		playerFunctions.indexCheck(self)
		playerFunctions.songChanged(self)


	def previous(self):
		self.playlist.previous()
		playerFunctions.indexCheck(self)
		playerFunctions.songChanged(self)


	def messagePop(self):
		msg = QMessageBox()
		msg.setStyleSheet("""
			*{
				background-color:rgb(44, 42, 42);;
				color:white;
			}
			QPushButton{
				height:25px;
				width:50px;
				background-color:rgb(63, 60, 60);
				border-radius:5px;
			}

			QPushButton:hover{
				background-color:rgb(80, 77, 77);
			}
			""")
		#msg.setWindowIcon(self.error_icon)

		msg.setWindowTitle("Sorry Bruh!")
		msg.setText("Directory does not have any Song")
		msg.setIcon(QMessageBox.Critical)


		x = msg.exec_()


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'file_manager.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


import sys
import os
import glob
import images_qr

from os.path import expanduser

from datetime import datetime

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QFileDialog, QApplication, QMessageBox

date = datetime.today().strftime('%b %d, %Y')
time = datetime.now().strftime("%I:%M %p")


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        self.icon = QtGui.QIcon()
        self.icon.addPixmap(QtGui.QPixmap(":./Images/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.error_icon = QtGui.QIcon()
        self.error_icon.addPixmap(QtGui.QPixmap(":./Images/error.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(self.icon)
        MainWindow.setFixedSize(520, 398)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("*{\n"
                "    background-color: qlineargradient(spread:pad, x1:0.08, y1:0, x2:1, y2:0, stop:0.227273 rgba(41, 128, 185, 255), stop:0.647727 rgba(109, 213, 185, 250), stop:1 rgba(255, 255, 255, 255));\n"
                "}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mngBtn = QtWidgets.QPushButton(self.centralwidget)
        self.mngBtn.setGeometry(QtCore.QRect(160, 220, 181, 71))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(62)
        self.mngBtn.setFont(font)
        self.mngBtn.setAutoFillBackground(False)
        self.mngBtn.setStyleSheet("*{\n"
                "    background:none;\n"
                "    font-weight:500;\n"
                "    color:white;\n"
                "    border-radius:5px;\n"
                "     border:2px solid;\n"
                "    border-color: qlineargradient(spread:pad, x1:0.0795455, y1:0.131, x2:1, y2:1, stop:0.340909 rgba(85, 255, 241, 255), stop:1 rgba(170, 0, 255, 255));\n"
                "}\n"
                "\n"
                "*:hover{\n"
                "    color:black;\n"
                "    background-color: rgba(255, 255, 255, 0.7);    \n"
                "}")
        self.mngBtn.setObjectName("mngBtn")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(100, 160, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(8)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("*{\n"
                "    border-radius:2px;\n"
                "    background-color: rgb(255, 255, 255);\n"
                "}")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.browse_btn = QtWidgets.QPushButton(self.centralwidget)
        self.browse_btn.setGeometry(QtCore.QRect(350, 163, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.browse_btn.setFont(font)
        self.browse_btn.setStyleSheet("*{\n"
                "    border-radius:2px;\n"
                "    background-color: rgba(255, 255, 255, 0.7);    \n"
                "}\n"
                "\n"
                "*:hover{\n"
                "    background-color:white;\n"
                "}")
        self.browse_btn.setObjectName("browse_btn")
        self.brand_label = QtWidgets.QLabel(self.centralwidget)
        self.brand_label.setGeometry(QtCore.QRect(40, 50, 151, 61))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.brand_label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.brand_label.setFont(font)
        self.brand_label.setStyleSheet("*{\n"
                "    background:none;\n"
                "    color:white;\n"
                "}")
        self.brand_label.setLineWidth(1)
        self.brand_label.setTextFormat(QtCore.Qt.AutoText)
        self.brand_label.setScaledContents(True)
        self.brand_label.setAlignment(QtCore.Qt.AlignCenter)
        self.brand_label.setIndent(-1)
        self.brand_label.setObjectName("brand_label")
        self.brand_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.brand_label_2.setGeometry(QtCore.QRect(80, 80, 381, 61))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.brand_label_2.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(23)
        font.setBold(True)
        font.setWeight(75)
        self.brand_label_2.setFont(font)
        self.brand_label_2.setStyleSheet("*{\n"
                "    background:none;\n"
                "    color:white;\n"
                "}")
        self.brand_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.brand_label_2.setObjectName("brand_label_2")
        self.time_label = QtWidgets.QLabel(self.centralwidget)
        self.time_label.setGeometry(QtCore.QRect(380, 20, 141, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(61, 90, 241))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 90, 241))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 90, 241))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 90, 241))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 90, 241))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 90, 241))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 90, 241))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 90, 241))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 90, 241))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.time_label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.time_label.setFont(font)
        self.time_label.setStyleSheet("*{\n"
                "    background:none;\n"
                "    color: #3d5af1;\n"
                "}")
        self.time_label.setLineWidth(1)
        self.time_label.setTextFormat(QtCore.Qt.AutoText)
        self.time_label.setScaledContents(True)
        self.time_label.setAlignment(QtCore.Qt.AlignCenter)
        self.time_label.setIndent(-1)
        self.time_label.setObjectName("time_label")
        self.date_label = QtWidgets.QLabel(self.centralwidget)
        self.date_label.setGeometry(QtCore.QRect(374, 0, 151, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(61, 90, 241))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 90, 241))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 90, 241))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 90, 241))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 90, 241))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 90, 241))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 90, 241))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 90, 241))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 90, 241))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.date_label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.date_label.setFont(font)
        self.date_label.setStyleSheet("*{\n"
                "    background:none;\n"
                "    color: #3d5af1;\n"
                "}")
        self.date_label.setLineWidth(1)
        self.date_label.setTextFormat(QtCore.Qt.AutoText)
        self.date_label.setScaledContents(True)
        self.date_label.setAlignment(QtCore.Qt.AlignCenter)
        self.date_label.setIndent(-1)
        self.date_label.setObjectName("date_label")
        self.dev_label = QtWidgets.QLabel(self.centralwidget)
        self.dev_label.setGeometry(QtCore.QRect(-20, 357, 151, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.dev_label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.dev_label.setFont(font)
        self.dev_label.setStyleSheet("*{\n"
                "    background:none;\n"
                "    color:white;\n"
                "}")
        self.dev_label.setLineWidth(1)
        self.dev_label.setTextFormat(QtCore.Qt.AutoText)
        self.dev_label.setScaledContents(True)
        self.dev_label.setAlignment(QtCore.Qt.AlignCenter)
        self.dev_label.setIndent(-1)
        self.dev_label.setObjectName("dev_label")
        self.date_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.date_label_2.setGeometry(QtCore.QRect(10, 370, 221, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.date_label_2.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.date_label_2.setFont(font)
        self.date_label_2.setStyleSheet("*{\n"
                "    background:none;\n"
                "    color:white;\n"
                "}")
        self.date_label_2.setLineWidth(1)
        self.date_label_2.setTextFormat(QtCore.Qt.AutoText)
        self.date_label_2.setScaledContents(True)
        self.date_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.date_label_2.setIndent(-1)
        self.date_label_2.setObjectName("date_label_2")
        self.version_label = QtWidgets.QLabel(self.centralwidget)
        self.version_label.setGeometry(QtCore.QRect(450, 370, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.version_label.setFont(font)
        self.version_label.setStyleSheet("*{\n"
                "    background:none;\n"
                "    color: #3d5af1;\n"
                "}")
        self.version_label.setTextFormat(QtCore.Qt.AutoText)
        self.version_label.setScaledContents(True)
        self.version_label.setAlignment(QtCore.Qt.AlignCenter)
        self.version_label.setObjectName("version_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionStop_App = QtWidgets.QAction(MainWindow)
        self.actionStop_App.setVisible(True)
        self.actionStop_App.setIconVisibleInMenu(True)
        self.actionStop_App.setObjectName("actionStop_App")

       
        MainWindow.setCentralWidget(self.centralwidget)

        self.browse_btn.clicked.connect(self.browseFile)
        self.mngBtn.clicked.connect(self.setupDir)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Auto File Manager"))
        self.mngBtn.setText(_translate("MainWindow", "M A N A G E  F I L E S"))
        self.browse_btn.setText(_translate("MainWindow", "Browse"))
        self.brand_label.setText(_translate("MainWindow", "AUTO"))
        self.brand_label_2.setText(_translate("MainWindow", "F I L E  M A N A G E R"))
        self.time_label.setText(_translate("MainWindow",time))
        self.date_label.setText(_translate("MainWindow", date))
        self.dev_label.setText(_translate("MainWindow", "DEVELOPED BY:"))
        self.date_label_2.setText(_translate("MainWindow", "M A R K  J O S H U A  O M A N D A M"))
        self.version_label.setText(_translate("MainWindow", "V.1.0.0"))
        self.actionStop_App.setText(_translate("MainWindow", "Stop App"))

    def browseFile(self):
        input_dir = QFileDialog.getExistingDirectory(None, 'Select a folder:', expanduser("~"))
        self.lineEdit.setText(input_dir)

    def setupDir(self):
        try:
            current_directory = os.chdir(self.lineEdit.text())
            self.files = glob.glob('*')
            self.extension_set = set()
            for file in self.files:
                extension = os.path.splitext(file)
                try:
                   self.extension_set.add(extension[1])
                except Exception:
                   continue
            self.createDirs()
            self.transFiles()
            self.messagePop(1)
        except Exception:
            self.messagePop(2)

    def createDirs(self):
        for fileType in self.extension_set:
                fileType = fileType.lower()
                try:
                        if fileType == ".exe":
                                os.makedirs("Programs")
                        elif fileType in [".doc", ".docx", ".pdf", ".xls", ".ppt", ".pptx", ".txt", ".xlsx"]:
                                os.makedirs("Documents")
                        elif fileType in  [".zip", ".rar", ".arj", ".tar.gz", ".tgz"]:
                                os.makedirs("Compressed")
                        elif fileType in [".mp4", ".m4p",".webm", ".mkv", ".flv", ".mov", ".avi", ".wmv", ".mts", ".m2ts", ".ts", ".amv", ".rm", ".rmvb" ]:
                                os.makedirs("Videos")
                        elif fileType in [".jpg", ".jpeg", ".png", ".psd", ".gif", ".svg", ".webp", ".jpeg 2000"]:
                                os.makedirs("Images")
                        elif fileType == ".mp3":
                                os.makedirs("Music")
                        else:
                                if fileType == "":
                                        pass
                                else:
                                        os.makedirs("Others")
                except Exception:
                        continue

    def transFiles(self):
        for file in self.files:
                file_extnsion = os.path.splitext(file)
                fileType = file_extnsion[1].lower()
                try:
                        if fileType == ".exe":
                                os.rename(file,"Programs/" + file)
                        elif fileType in [".doc", ".docx", ".pdf", ".xls", ".ppt", ".pptx", ".txt", ".xlsx"]:
                                os.rename(file, "Documents/" + file)
                        elif fileType in  [".zip", ".rar", ".arj", ".tar.gz", ".tgz"]:
                                os.rename(file, "Compressed/" + file)
                        elif fileType in [".mp4", ".m4p",".webm", ".mkv", ".flv", ".mov", ".avi", ".wmv", ".mts", ".m2ts", ".ts", ".amv", ".rm", ".rmvb" ]:
                                os.rename(file, "Videos/" + file)
                        elif fileType in [".jpg", ".jpeg", ".png", ".psd", ".gif", ".svg", ".webp", ".jpeg 2000"]:
                                os.rename(file, "Images/" + file)
                        elif fileType == ".mp3":
                                os.rename(file, "Music/" + file)
                        else:
                                if fileType == "":
                                        pass 
                                else:
                                        os.rename(file, "Others/" + file)

                except Exception:
                        continue


    def messagePop(self, n):
        msg = QMessageBox()
        if n == 1:                      
                msg.setWindowIcon(self.icon)

                msg.setWindowTitle("Success!")
                msg.setText("File Managed Successfuly")
                msg.setIcon(QMessageBox.Information)
        elif n == 2:
                msg.setWindowIcon(self.error_icon)

                msg.setWindowTitle("Error!")
                msg.setText("Invalid Directory")
                msg.setIcon(QMessageBox.Critical)


        x = msg.exec_()




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())



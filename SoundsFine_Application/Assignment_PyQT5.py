# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Assignment_PyQT5.ui'

# Created by: PyQt5 UI code generator 5.15.10

# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from Assignment_Classes import *


class Ui_MainWindow(object):

    # -------------------- All Instances ------------------ #

    def __init__(self):

        self.genre1 = Jazz('Sing a Song of Song', '7:22', 'Kenny Garret', 'American', '70.00', True, 'Jazz', '17:00',
                           'Arena 1', 'J111111 / Se.A1 ')
        self.genre2 = Jazz('Gloomy Sunday', '12:44', 'Branford Marsalis', 'American', '00.00', False, 'Jazz', '18:00',
                           'Arena 1', 'J2222222 / Se.B2 ')
        self.genre3 = Jazz('Free', '12:22', 'Joey Caldarazzo', 'American', '40.00', True, 'Jazz', '19:00',
                           'Arena 1', 'J3333333 / Se.C3 ')
        self.genre4 = Jazz('I Love You', '2:47', 'Jacob Baron', 'American', '100.00', True, 'Jazz', '20:00',
                           'Arena 1', 'J4444444 / Se.D4 ')

        # ------------------------------------------------

        self.genre5 = Country('You Are Still The One', '7:22', 'Shania Twain', 'Canadian', '120.00', True, 'Country',
                              '17:00',
                              'Arena 2', 'C2222222 / Se.A1 ')
        self.genre6 = Country('Tudo Em Paz', '3:33', 'Jorge & Mateus', 'Brazilian', '40.00', True, 'Country', '18:00',
                              'Arena 2', 'F4444444 / Se.F7 ')
        self.genre7 = Country('Wasted On You', '2:58', 'Morgan Wallen', 'American', '70.00', True, 'Country', '19:00',
                              'Arena 2', 'C3333333 / Se.C3 ')
        self.genre8 = Country('God\'s Country', '3:25', 'Blake Shelton', 'American', '60.00', True, 'Country',
                              '20:00', 'Arena 2', 'D4444444 / Se.D4 ')
        self.genre9 = Country('Home', '4:05', 'Blake Shelton', 'American', '60.00', True, 'Country', '21:00',
                              'Arena 2', 'C5555555 / Se.E5 ')

        # ------------------------------------------------

        self.genre10 = Pop('Bad Habits', '3:47', 'Ed Sheeran', 'British', '100.00', True, 'Pop', '17:00',
                           'Arena 3', 'P111111 / Se.A1 ')
        self.genre11 = Pop('Easy On Me', '3:44', 'Adele', 'British', '200.00', True, 'Pop', '18:00',
                           'Arena 3', 'P2222222 / Se.B2 ')
        self.genre12 = Pop('Delicate', '3:51', 'Taylor Swift', 'American', '400.00', True, 'Pop', '19:00',
                           'Arena 3', 'P3333333 / Se.C3 ')
        self.genre13 = Pop('Claudia Leite', '3:59', 'Bola De Sabão', 'Brazilian', '40.00', True, 'Pop', '20:00',
                           'Arena 3', 'P4444444 / Se.D4 ')

        # ------------------------------------------------

        self.genre14 = Rock('I Dont Want To Miss A Thing', '4:57', 'Aerosmith', 'American', '200.00', True, 'Rock',
                            '17:00', 'Arena 4', 'R111111 / Se.A1 ')
        self.genre15 = Rock('Let It Be', '2:58', 'Beatles', 'British', '00.00', False, 'Rock', '18:00',
                            'Arena 4', 'R2222222 / Se.B2 ')
        self.genre16 = Rock('All The Small Things', '2:47', 'Blink 182', 'American', '70.00', True, 'Rock', '19:00',
                            'Arena 4', 'R3333333 / Se.C3 ')
        self.genre17 = Rock('It Is My Life', '3:35', 'Bon Jovi', 'American', '200.00', True, 'Rock', '20:00',
                            'Arena 4', 'R4444444/ Se.D4 ')

        # ------------------------------------------------

        self.genreList = [self.genre1, self.genre2, self.genre3, self.genre4,
                          self.genre5, self.genre6, self.genre7, self.genre8, self.genre9, self.genre10, self.genre11,
                          self.genre12, self.genre13, self.genre14, self.genre15, self.genre16, self.genre17]

        self.current = 0  # current genre

        self.genre = self.genreList[0]  # initialize to first genre

    # -------------------- Display Current Genre --------------------- #

    def display(self, index):
        self.genre = self.genreList[index]

        self.lineEditMusicTitle.setText(str(self.genre.readSongName()))
        self.lineEditSingerName.setText(str(self.genre.readSingerName()))
        self.lineEditSingerNationality.setText(str(self.genre.readSingerNationality()))
        self.lineEditSongTrackTime.setText(str(self.genre.readSongTrackTime()))

        genre = self.genre.readGenreName()
        self.comboBoxGenre.setCurrentText(genre)
        availableConcert = self.genre.readAvailableConcert()

        if (availableConcert == True):

            self.checkBoxConcert.setChecked(True)
            self.buttonBuyTicket.setDisabled(False)
            self.buttonPay.setDisabled(False)

        else:

            self.checkBoxConcert.setChecked(False)
            self.buttonBuyTicket.setDisabled(True)
            self.buttonPay.setDisabled(True)

    # ------------------------- Event Handlers ------------------------ #

    def firstEvent(self):

        self.current = 0
        self.display(self.current)

        self.checkBoxLike.setChecked(False)
        self.lineEditDetail1.setText('')
        self.lineEditDetail2.setText('')
        self.lineEditDetail3.setText('')
        self.lineEditTotal.setText('')
        self.lineEditPay.setText('')

    def lastEvent(self):

        self.current = len(self.genreList) - 1
        self.display(self.current)

        self.checkBoxLike.setChecked(False)
        self.lineEditDetail1.setText('')
        self.lineEditDetail2.setText('')
        self.lineEditDetail3.setText('')
        self.lineEditTotal.setText('')
        self.lineEditPay.setText('')

    @staticmethod
    def exitEvent():
        exit()

    def playPauseEvent(self):

        if (self.buttonPlayPause.text() == 'Play'):
            self.buttonPlayPause.setText('Playing...')

        elif (self.buttonPlayPause.text() == 'Playing...'):
            self.buttonPlayPause.setText('Paused')

        elif (self.buttonPlayPause.text() == 'Paused'):
            self.buttonPlayPause.setText('Playing...')

    def previousEvent(self):

        if (self.current > 0):
            self.current -= 1
            self.display(self.current)

        self.checkBoxLike.setChecked(False)
        self.lineEditDetail1.setText('')
        self.lineEditDetail2.setText('')
        self.lineEditDetail3.setText('')
        self.lineEditTotal.setText('')
        self.lineEditPay.setText('')

    def nextEvent(self):

        if (self.current < (len(self.genreList) - 1)):
            self.current += 1
            self.display(self.current)

        self.checkBoxLike.setChecked(False)
        self.lineEditDetail1.setText('')
        self.lineEditDetail2.setText('')
        self.lineEditDetail3.setText('')
        self.lineEditTotal.setText('')
        self.lineEditPay.setText('')

    def stopEvent(self):

        if (self.current < (len(self.genreList) - 1)):
            self.current += 1
            self.display(self.current)

        self.lineEditMusicTitle.setText('')
        self.lineEditSingerName.setText('')
        self.lineEditSingerNationality.setText('')
        self.lineEditSongTrackTime.setText('')
        self.lineEditTotal.setText('')
        self.lineEditPay.setText('')
        self.comboBoxGenre.setCurrentText('Jazz')
        self.checkBoxConcert.setChecked(False)
        self.lineEditDetail1.setText('')
        self.lineEditDetail2.setText('')
        self.lineEditDetail3.setText('')
        self.buttonPay.setDisabled(True)
        self.buttonBuyTicket.setDisabled(True)
        self.buttonPlayPause.setText('Play')
        self.lineEditVolume.setText('0')
        self.checkBoxLike.setChecked(False)

    def addGenreEvent(self):

        song = self.lineEditMusicTitle.text()
        singer = self.lineEditSingerName.text()
        singerNati = self.lineEditSingerNationality.text()
        songTime = self.lineEditSongTrackTime.text()
        price = self.lineEditTotal.text()
        available = self.checkBoxConcert.checkState()

        detail1 = self.lineEditDetail1.text()
        detail2 = self.lineEditDetail2.text()
        detail3 = self.lineEditDetail3.text()

        newSong = self.comboBoxGenre.currentText()

        if (newSong == 'Jazz'):
            newGenre = Jazz(song, songTime, singer, singerNati, price, available, newSong, detail1, detail2, detail3)
            self.genreList.append(newGenre)

        elif (newSong == 'Country'):
            newGenre = Country(song, songTime, singer, singerNati, price, available, newSong, detail1, detail2, detail3)
            self.genreList.append(newGenre)

        elif (newSong == 'Pop'):
            newGenre = Pop(song, songTime, singer, singerNati, price, available, newSong, detail1, detail2, detail3)
            self.genreList.append(newGenre)

        elif (newSong == 'Rock'):
            newGenre = Rock(song, songTime, singer, singerNati, price, available, newSong, detail1, detail2, detail3)
            self.genreList.append(newGenre)

        self.display(len(self.genreList) - 1)

    def buyTicketEvent(self):

        self.lineEditTotal.setText(str(self.genre.readPriceConcert()))

    def payEvent(self):

        if self.lineEditPay.text() == '' or self.lineEditPay.text() == 'No Value':
            self.lineEditPay.setText('No Value')

        else:
            paid = float(self.lineEditPay.text())
            concertPrice = float(self.lineEditTotal.text())

            if paid == concertPrice:

                self.lineEditPay.setText(' Success!!!!')
                self.lineEditTotal.setText('0.00')

                self.lineEditDetail1.setText(str(self.genre.readDetails1()))
                self.lineEditDetail2.setText(str(self.genre.readDetails2()))
                self.lineEditDetail3.setText(str(self.genre.readDetails3()))

            elif paid < concertPrice:
                self.lineEditPay.setText('Under')

            elif paid > concertPrice:
                self.lineEditPay.setText('Over')

    def volumeDecr(self):

        if self.lineEditVolume.text() == '1' or self.lineEditVolume.text() == 'Mute':

            result = 'Mute'

        elif self.lineEditVolume.text() == 'Max.':

            result = '10'

        else:
            result = int(self.lineEditVolume.text()) - 1

        self.lineEditVolume.setText(str(result))

    def volumeIncr(self):

        if self.lineEditVolume.text() == '10' or self.lineEditVolume.text() == 'Max.':

            result = 'Max.'

        elif self.lineEditVolume.text() == 'Mute':

            self.lineEditVolume.setText('0')

            result = int(self.lineEditVolume.text()) + 1


        else:

            result = int(self.lineEditVolume.text()) + 1

        self.lineEditVolume.setText(str(result))

    def like(self):

        self.checkBoxLike.setChecked(True)

    # ------------------------- PYQT5 Generated Code ------------------------- #

    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(822, 806)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.labelMainTitle = QtWidgets.QLabel(self.centralwidget)
        self.labelMainTitle.setGeometry(QtCore.QRect(210, 0, 371, 41))

        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)

        self.labelMainTitle.setFont(font)
        self.labelMainTitle.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labelMainTitle.setStyleSheet("")
        self.labelMainTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.labelMainTitle.setObjectName("labelMainTitle")

        self.labelMusicTitle = QtWidgets.QLabel(self.centralwidget)
        self.labelMusicTitle.setGeometry(QtCore.QRect(220, 100, 91, 21))

        font = QtGui.QFont()
        font.setPointSize(16)

        self.labelMusicTitle.setFont(font)
        self.labelMusicTitle.setObjectName("labelMusicTitle")

        self.labelSingerName = QtWidgets.QLabel(self.centralwidget)
        self.labelSingerName.setGeometry(QtCore.QRect(220, 170, 101, 21))

        font = QtGui.QFont()
        font.setPointSize(16)

        self.labelSingerName.setFont(font)
        self.labelSingerName.setObjectName("labelSingerName")

        self.labelSingerNationality = QtWidgets.QLabel(self.centralwidget)
        self.labelSingerNationality.setGeometry(QtCore.QRect(220, 200, 151, 31))

        font = QtGui.QFont()
        font.setPointSize(16)

        self.labelSingerNationality.setFont(font)
        self.labelSingerNationality.setObjectName("labelSingerNationality")
        self.labelSongTrackTime = QtWidgets.QLabel(self.centralwidget)
        self.labelSongTrackTime.setGeometry(QtCore.QRect(220, 130, 151, 31))

        font = QtGui.QFont()
        font.setPointSize(16)

        self.labelSongTrackTime.setFont(font)
        self.labelSongTrackTime.setObjectName("labelSongTrackTime")
        self.labelSingerName_4 = QtWidgets.QLabel(self.centralwidget)
        self.labelSingerName_4.setGeometry(QtCore.QRect(220, 60, 151, 31))

        font = QtGui.QFont()
        font.setPointSize(16)

        self.labelSingerName_4.setFont(font)
        self.labelSingerName_4.setObjectName("labelSingerName_4")

        self.buttonPlayPause = QtWidgets.QPushButton(self.centralwidget)
        self.buttonPlayPause.setGeometry(QtCore.QRect(220, 310, 101, 25))
        self.buttonPlayPause.setStyleSheet("background-color: rgb(21, 175, 255);\n"
                                           "border-radius:10px;border-radius:10px;")
        self.buttonPlayPause.setObjectName("buttonPlayPause")

        self.buttonStop = QtWidgets.QPushButton(self.centralwidget)
        self.buttonStop.setGeometry(QtCore.QRect(210, 350, 113, 32))
        self.buttonStop.setObjectName("buttonStop")

        self.buttonExit = QtWidgets.QPushButton(self.centralwidget)
        self.buttonExit.setGeometry(QtCore.QRect(450, 350, 113, 32))
        self.buttonExit.setObjectName("buttonExit")

        self.buttonAddGenre = QtWidgets.QPushButton(self.centralwidget)
        self.buttonAddGenre.setGeometry(QtCore.QRect(330, 350, 113, 32))
        self.buttonAddGenre.setObjectName("buttonAddGenre")

        self.buttonPrevious = QtWidgets.QPushButton(self.centralwidget)
        self.buttonPrevious.setGeometry(QtCore.QRect(330, 310, 113, 32))
        self.buttonPrevious.setObjectName("buttonPrevious")

        self.buttonNext = QtWidgets.QPushButton(self.centralwidget)
        self.buttonNext.setGeometry(QtCore.QRect(450, 310, 113, 32))
        self.buttonNext.setObjectName("buttonNext")

        self.lineEditMusicTitle = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditMusicTitle.setGeometry(QtCore.QRect(370, 100, 191, 21))
        self.lineEditMusicTitle.setObjectName("lineEditMusicTitle")

        self.lineEditSingerName = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditSingerName.setGeometry(QtCore.QRect(370, 170, 191, 21))
        self.lineEditSingerName.setObjectName("lineEditSingerName")

        self.lineEditSingerNationality = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditSingerNationality.setGeometry(QtCore.QRect(370, 210, 191, 21))
        self.lineEditSingerNationality.setObjectName("lineEditSingerNationality")

        self.lineEditSongTrackTime = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditSongTrackTime.setGeometry(QtCore.QRect(370, 130, 191, 21))
        self.lineEditSongTrackTime.setObjectName("lineEditSongTrackTime")

        self.labelSeparator = QtWidgets.QLabel(self.centralwidget)
        self.labelSeparator.setGeometry(QtCore.QRect(220, 390, 341, 21))

        font = QtGui.QFont()
        font.setPointSize(16)

        self.labelSeparator.setFont(font)
        self.labelSeparator.setObjectName("labelSeparator")

        self.comboBoxGenre = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxGenre.setGeometry(QtCore.QRect(370, 50, 191, 41))
        self.comboBoxGenre.setObjectName("comboBoxGenre")
        self.comboBoxGenre.addItem("")
        self.comboBoxGenre.addItem("")
        self.comboBoxGenre.addItem("")
        self.comboBoxGenre.addItem("")

        self.checkBoxConcert = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxConcert.setGeometry(QtCore.QRect(220, 430, 151, 21))

        font = QtGui.QFont()
        font.setPointSize(16)

        self.checkBoxConcert.setFont(font)
        self.checkBoxConcert.setObjectName("checkBoxConcert")

        self.buttonBuyTicket = QtWidgets.QPushButton(self.centralwidget)
        self.buttonBuyTicket.setGeometry(QtCore.QRect(390, 420, 141, 41))

        font = QtGui.QFont()
        font.setPointSize(16)

        self.buttonBuyTicket.setFont(font)
        self.buttonBuyTicket.setStyleSheet("background-color: rgb(21, 175, 255);\n"
                                           "border-radius:10px;border-radius:10px;")
        self.buttonBuyTicket.setObjectName("buttonBuyTicket")
        self.buttonBuyTicket.setDisabled(True)

        self.labelTotal = QtWidgets.QLabel(self.centralwidget)
        self.labelTotal.setGeometry(QtCore.QRect(220, 500, 51, 41))

        font = QtGui.QFont()
        font.setPointSize(20)

        self.labelTotal.setFont(font)
        self.labelTotal.setObjectName("labelTotal")

        self.lineEditTotal = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditTotal.setGeometry(QtCore.QRect(280, 500, 90, 41))

        font = QtGui.QFont()
        font.setPointSize(16)

        self.lineEditTotal.setFont(font)
        self.lineEditTotal.setObjectName("lineEditTotal")

        self.lineEditPay = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditPay.setGeometry(QtCore.QRect(450, 500, 90, 41))

        font = QtGui.QFont()
        font.setPointSize(16)

        self.lineEditPay.setFont(font)
        self.lineEditPay.setObjectName("lineEditPay")

        self.buttonPay = QtWidgets.QPushButton(self.centralwidget)
        self.buttonPay.setGeometry(QtCore.QRect(380, 500, 61, 41))

        font = QtGui.QFont()
        font.setPointSize(16)

        self.buttonPay.setFont(font)
        self.buttonPay.setStyleSheet("background-color: rgb(21, 175, 255);\n"
                                     "border-radius:10px;border-radius:10px;")
        self.buttonPay.setObjectName("buttonPay")
        self.buttonPay.setDisabled(True)

        self.labelConcertDetails = QtWidgets.QLabel(self.centralwidget)
        self.labelConcertDetails.setGeometry(QtCore.QRect(220, 570, 131, 31))

        font = QtGui.QFont()
        font.setPointSize(16)

        self.labelConcertDetails.setFont(font)
        self.labelConcertDetails.setObjectName("labelConcertDetails")

        self.lineEditDetail1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditDetail1.setGeometry(QtCore.QRect(220, 600, 331, 21))
        self.lineEditDetail1.setObjectName("lineEditDetail1")

        self.lineEditDetail2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditDetail2.setGeometry(QtCore.QRect(220, 630, 331, 21))
        self.lineEditDetail2.setObjectName("lineEditDetail2")

        self.lineEditDetail3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditDetail3.setGeometry(QtCore.QRect(220, 660, 331, 21))
        self.lineEditDetail3.setObjectName("lineEditDetail3")

        self.buttonVolumeIncrease = QtWidgets.QPushButton(self.centralwidget)
        self.buttonVolumeIncrease.setGeometry(QtCore.QRect(320, 260, 61, 31))
        self.buttonVolumeIncrease.setStyleSheet("")
        self.buttonVolumeIncrease.setObjectName("buttonVolumeIncrease")

        self.buttonVolumeDecrease = QtWidgets.QPushButton(self.centralwidget)
        self.buttonVolumeDecrease.setGeometry(QtCore.QRect(210, 260, 61, 31))
        self.buttonVolumeDecrease.setStyleSheet("")
        self.buttonVolumeDecrease.setObjectName("buttonVolumeDecrease")

        self.lineEditVolume = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditVolume.setGeometry(QtCore.QRect(270, 260, 51, 31))
        self.lineEditVolume.setObjectName("lineEditVolume")
        self.lineEditVolume.setText('0')
        font = QtGui.QFont()

        self.lineEditVolume.setAlignment(QtCore.Qt.AlignCenter)

        self.buttonLike = QtWidgets.QPushButton(self.centralwidget)
        self.buttonLike.setGeometry(QtCore.QRect(410, 260, 71, 31))

        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)

        self.buttonLike.setFont(font)
        self.buttonLike.setStyleSheet("background-color:rgb(130, 255, 9);\n"
                                      "border-radius:10px;")
        self.buttonLike.setObjectName("buttonLike")

        self.checkBoxLike = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxLike.setGeometry(QtCore.QRect(500, 260, 21, 21))

        font = QtGui.QFont()
        font.setPointSize(16)
        font.setStrikeOut(False)

        self.checkBoxLike.setFont(font)
        self.checkBoxLike.setText("")
        self.checkBoxLike.setObjectName("checkBoxLike")

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 822, 24))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")

        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)

        self.actionFirst = QtWidgets.QAction(MainWindow)
        self.actionFirst.setObjectName("actionFirst")

        self.actionLast = QtWidgets.QAction(MainWindow)
        self.actionLast.setObjectName("actionLast")

        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")

        self.menuMenu.addAction(self.actionFirst)
        self.menuMenu.addAction(self.actionLast)
        self.menuMenu.addAction(self.actionExit)

        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)

        self.actionFirst.triggered.connect(self.firstEvent)  # type: ignore
        self.actionLast.triggered.connect(self.lastEvent)  # type: ignore
        self.actionExit.triggered.connect(self.exitEvent)  # type: ignore

        self.buttonPlayPause.pressed.connect(self.playPauseEvent)  # type: ignore
        self.buttonPrevious.pressed.connect(self.previousEvent)  # type: ignore
        self.buttonNext.pressed.connect(self.nextEvent)  # type: ignore
        self.buttonStop.pressed.connect(self.stopEvent)  # type: ignore
        self.buttonAddGenre.pressed.connect(self.addGenreEvent)  # type: ignore
        self.buttonExit.pressed.connect(self.exitEvent)  # type: ignore
        self.buttonBuyTicket.pressed.connect(self.buyTicketEvent)  # type: ignore
        self.buttonPay.pressed.connect(self.payEvent)  # type: ignore
        self.buttonVolumeDecrease.pressed.connect(self.volumeDecr)  # type: ignore
        self.buttonVolumeIncrease.pressed.connect(self.volumeIncr)  # type: ignore
        self.buttonLike.pressed.connect(self.like)  # type: ignore

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):

        _translate = QtCore.QCoreApplication.translate

        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        self.labelMainTitle.setText(_translate("MainWindow", "SoundsFine Music Application"))
        self.labelMusicTitle.setText(_translate("MainWindow", "Song Title: "))

        self.labelSingerName.setText(_translate("MainWindow", "Singer Name: "))
        self.labelSingerNationality.setText(_translate("MainWindow", "Singer Nationality: "))

        self.labelSongTrackTime.setText(_translate("MainWindow", "Song Time: "))
        self.labelSingerName_4.setText(_translate("MainWindow", "Genre: "))

        self.buttonPlayPause.setText(_translate("MainWindow", "Play"))

        self.buttonStop.setText(_translate("MainWindow", "Stop"))

        self.buttonExit.setText(_translate("MainWindow", "Exit"))

        self.buttonAddGenre.setText(_translate("MainWindow", "Add Genre"))

        self.buttonPrevious.setText(_translate("MainWindow", "Previous"))

        self.buttonNext.setText(_translate("MainWindow", "Next"))

        self.labelSeparator.setText(_translate("MainWindow", "-----------------------------------------------"))

        self.comboBoxGenre.setItemText(0, _translate("MainWindow", "Jazz"))
        self.comboBoxGenre.setItemText(1, _translate("MainWindow", "Country"))
        self.comboBoxGenre.setItemText(2, _translate("MainWindow", "Pop"))
        self.comboBoxGenre.setItemText(3, _translate("MainWindow", "Rock"))

        self.checkBoxConcert.setText(_translate("MainWindow", "Concert Available"))

        self.buttonBuyTicket.setText(_translate("MainWindow", "Buy Ticket"))

        self.labelTotal.setText(_translate("MainWindow", "Total:"))

        self.buttonPay.setText(_translate("MainWindow", "Pay"))

        self.labelConcertDetails.setText(_translate("MainWindow", "Concert  Details:"))

        self.buttonVolumeIncrease.setText(_translate("MainWindow", "Vol +"))

        self.buttonVolumeDecrease.setText(_translate("MainWindow", "Vol -"))

        self.buttonLike.setText(_translate("MainWindow", "LIKE"))

        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))

        self.actionFirst.setText(_translate("MainWindow", "First"))
        self.actionLast.setText(_translate("MainWindow", "Last"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))

        # ------------------------------------------------ // ---------------------------------------------------- #

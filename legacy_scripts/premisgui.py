# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'premisgui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(877, 638)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 10, 411, 471))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.scanningTab = QtGui.QWidget()
        self.scanningTab.setObjectName(_fromUtf8("scanningTab"))
        self.filmCaptureInterventionsListBox = QtGui.QListWidget(self.scanningTab)
        self.filmCaptureInterventionsListBox.setGeometry(QtCore.QRect(10, 50, 281, 171))
        self.filmCaptureInterventionsListBox.setAlternatingRowColors(False)
        self.filmCaptureInterventionsListBox.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.filmCaptureInterventionsListBox.setObjectName(_fromUtf8("filmCaptureInterventionsListBox"))
        item = QtGui.QListWidgetItem()
        self.filmCaptureInterventionsListBox.addItem(item)
        item = QtGui.QListWidgetItem()
        self.filmCaptureInterventionsListBox.addItem(item)
        item = QtGui.QListWidgetItem()
        self.filmCaptureInterventionsListBox.addItem(item)
        item = QtGui.QListWidgetItem()
        self.filmCaptureInterventionsListBox.addItem(item)
        item = QtGui.QListWidgetItem()
        self.filmCaptureInterventionsListBox.addItem(item)
        self.lineEdit = QtGui.QLineEdit(self.scanningTab)
        self.lineEdit.setGeometry(QtCore.QRect(10, 20, 161, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.filmPreparationListBox = QtGui.QListWidget(self.scanningTab)
        self.filmPreparationListBox.setGeometry(QtCore.QRect(10, 270, 281, 141))
        self.filmPreparationListBox.setAlternatingRowColors(False)
        self.filmPreparationListBox.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.filmPreparationListBox.setObjectName(_fromUtf8("filmPreparationListBox"))
        item = QtGui.QListWidgetItem()
        self.filmPreparationListBox.addItem(item)
        item = QtGui.QListWidgetItem()
        self.filmPreparationListBox.addItem(item)
        item = QtGui.QListWidgetItem()
        self.filmPreparationListBox.addItem(item)
        item = QtGui.QListWidgetItem()
        self.filmPreparationListBox.addItem(item)
        item = QtGui.QListWidgetItem()
        self.filmPreparationListBox.addItem(item)
        item = QtGui.QListWidgetItem()
        self.filmPreparationListBox.addItem(item)
        item = QtGui.QListWidgetItem()
        self.filmPreparationListBox.addItem(item)
        self.lineEdit_2 = QtGui.QLineEdit(self.scanningTab)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 240, 141, 20))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.tabWidget.addTab(self.scanningTab, _fromUtf8(""))
        self.tapeTab = QtGui.QWidget()
        self.tapeTab.setObjectName(_fromUtf8("tapeTab"))
        self.tapeDeckList = QtGui.QListWidget(self.tapeTab)
        self.tapeDeckList.setGeometry(QtCore.QRect(10, 110, 256, 192))
        self.tapeDeckList.setObjectName(_fromUtf8("tapeDeckList"))
        item = QtGui.QListWidgetItem()
        self.tapeDeckList.addItem(item)
        item = QtGui.QListWidgetItem()
        self.tapeDeckList.addItem(item)
        item = QtGui.QListWidgetItem()
        self.tapeDeckList.addItem(item)
        item = QtGui.QListWidgetItem()
        self.tapeDeckList.addItem(item)
        item = QtGui.QListWidgetItem()
        self.tapeDeckList.addItem(item)
        item = QtGui.QListWidgetItem()
        self.tapeDeckList.addItem(item)
        self.tapeFormatComboBox = QtGui.QComboBox(self.tapeTab)
        self.tapeFormatComboBox.setGeometry(QtCore.QRect(10, 30, 191, 26))
        self.tapeFormatComboBox.setObjectName(_fromUtf8("tapeFormatComboBox"))
        self.tapeFormatComboBox.addItem(_fromUtf8(""))
        self.tapeFormatComboBox.addItem(_fromUtf8(""))
        self.tapeFormatComboBox.addItem(_fromUtf8(""))
        self.tapeFormatComboBox.addItem(_fromUtf8(""))
        self.tapeWorkstationComboBox = QtGui.QComboBox(self.tapeTab)
        self.tapeWorkstationComboBox.setGeometry(QtCore.QRect(10, 60, 191, 26))
        self.tapeWorkstationComboBox.setObjectName(_fromUtf8("tapeWorkstationComboBox"))
        self.tapeWorkstationComboBox.addItem(_fromUtf8(""))
        self.tapeWorkstationComboBox.addItem(_fromUtf8(""))
        self.tapeWorkstationComboBox.addItem(_fromUtf8(""))
        self.tapeWorkstationComboBox.addItem(_fromUtf8(""))
        self.tapeWorkstationComboBox.addItem(_fromUtf8(""))
        self.tapeWorkstationComboBox.addItem(_fromUtf8(""))
        self.ffv1CheckBox = QtGui.QCheckBox(self.tapeTab)
        self.ffv1CheckBox.setGeometry(QtCore.QRect(40, 340, 231, 20))
        self.ffv1CheckBox.setObjectName(_fromUtf8("ffv1CheckBox"))
        self.tabWidget.addTab(self.tapeTab, _fromUtf8(""))
        self.rawAudioTab = QtGui.QWidget()
        self.rawAudioTab.setObjectName(_fromUtf8("rawAudioTab"))
        self.rawAudioInterventions = QtGui.QListWidget(self.rawAudioTab)
        self.rawAudioInterventions.setGeometry(QtCore.QRect(10, 0, 256, 251))
        self.rawAudioInterventions.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.rawAudioInterventions.setObjectName(_fromUtf8("rawAudioInterventions"))
        item = QtGui.QListWidgetItem()
        self.rawAudioInterventions.addItem(item)
        item = QtGui.QListWidgetItem()
        self.rawAudioInterventions.addItem(item)
        item = QtGui.QListWidgetItem()
        self.rawAudioInterventions.addItem(item)
        item = QtGui.QListWidgetItem()
        self.rawAudioInterventions.addItem(item)
        item = QtGui.QListWidgetItem()
        self.rawAudioInterventions.addItem(item)
        item = QtGui.QListWidgetItem()
        self.rawAudioInterventions.addItem(item)
        item = QtGui.QListWidgetItem()
        self.rawAudioInterventions.addItem(item)
        item = QtGui.QListWidgetItem()
        self.rawAudioInterventions.addItem(item)
        item = QtGui.QListWidgetItem()
        self.rawAudioInterventions.addItem(item)
        item = QtGui.QListWidgetItem()
        self.rawAudioInterventions.addItem(item)
        item = QtGui.QListWidgetItem()
        self.rawAudioInterventions.addItem(item)
        item = QtGui.QListWidgetItem()
        self.rawAudioInterventions.addItem(item)
        item = QtGui.QListWidgetItem()
        self.rawAudioInterventions.addItem(item)
        item = QtGui.QListWidgetItem()
        self.rawAudioInterventions.addItem(item)
        self.tabWidget.addTab(self.rawAudioTab, _fromUtf8(""))
        self.gradeTab = QtGui.QWidget()
        self.gradeTab.setObjectName(_fromUtf8("gradeTab"))
        self.listWidget = QtGui.QListWidget(self.gradeTab)
        self.listWidget.setGeometry(QtCore.QRect(10, 10, 391, 341))
        self.listWidget.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        item = QtGui.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidget.addItem(item)
        self.tabWidget.addTab(self.gradeTab, _fromUtf8(""))
        self.userComboBox = QtGui.QComboBox(self.centralwidget)
        self.userComboBox.setGeometry(QtCore.QRect(560, 20, 111, 22))
        self.userComboBox.setObjectName(_fromUtf8("userComboBox"))
        self.userComboBox.addItem(_fromUtf8(""))
        self.userComboBox.addItem(_fromUtf8(""))
        self.userComboBox.addItem(_fromUtf8(""))
        self.userComboBox.addItem(_fromUtf8(""))
        self.userComboBox.addItem(_fromUtf8(""))
        self.userComboBox.addItem(_fromUtf8(""))
        self.userComboBox.addItem(_fromUtf8(""))
        self.lineEdit_3 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(440, 20, 113, 20))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.oeTextBox = QtGui.QPlainTextEdit(self.centralwidget)
        self.oeTextBox.setGeometry(QtCore.QRect(440, 80, 291, 41))
        self.oeTextBox.setInputMethodHints(QtCore.Qt.ImhNone)
        self.oeTextBox.setObjectName(_fromUtf8("oeTextBox"))
        self.FilmographicTextBox = QtGui.QPlainTextEdit(self.centralwidget)
        self.FilmographicTextBox.setGeometry(QtCore.QRect(440, 160, 291, 41))
        self.FilmographicTextBox.setObjectName(_fromUtf8("FilmographicTextBox"))
        self.sourceAccessionTextBox = QtGui.QPlainTextEdit(self.centralwidget)
        self.sourceAccessionTextBox.setGeometry(QtCore.QRect(440, 230, 291, 41))
        self.sourceAccessionTextBox.setObjectName(_fromUtf8("sourceAccessionTextBox"))
        self.lineEdit_4 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(440, 60, 291, 20))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.lineEdit_5 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(440, 140, 291, 20))
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.lineEdit_6 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(440, 210, 291, 20))
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.processButton = QtGui.QCommandLinkButton(self.centralwidget)
        self.processButton.setGeometry(QtCore.QRect(450, 370, 188, 41))
        self.processButton.setObjectName(_fromUtf8("processButton"))
        self.userComboBox.raise_()
        self.lineEdit_3.raise_()
        self.oeTextBox.raise_()
        self.FilmographicTextBox.raise_()
        self.sourceAccessionTextBox.raise_()
        self.lineEdit_4.raise_()
        self.lineEdit_5.raise_()
        self.lineEdit_6.raise_()
        self.processButton.raise_()
        self.tabWidget.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 877, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "IFI Irish Film Archive Post Digitisation Tool", None))
        self.filmCaptureInterventionsListBox.setSortingEnabled(False)
        __sortingEnabled = self.filmCaptureInterventionsListBox.isSortingEnabled()
        self.filmCaptureInterventionsListBox.setSortingEnabled(False)
        item = self.filmCaptureInterventionsListBox.item(0)
        item.setText(_translate("MainWindow", "Overscanning of image to capture optical track", None))
        item = self.filmCaptureInterventionsListBox.item(1)
        item.setText(_translate("MainWindow", "Monochrome setting enabled", None))
        item = self.filmCaptureInterventionsListBox.item(2)
        item.setText(_translate("MainWindow", "Spacing between reels not captured                      ", None))
        item = self.filmCaptureInterventionsListBox.item(3)
        item.setText(_translate("MainWindow", "Negative to positive", None))
        item = self.filmCaptureInterventionsListBox.item(4)
        item.setText(_translate("MainWindow", "White reference taken from frame", None))
        self.filmCaptureInterventionsListBox.setSortingEnabled(__sortingEnabled)
        self.lineEdit.setText(_translate("MainWindow", "Capture Interventions", None))
        __sortingEnabled = self.filmPreparationListBox.isSortingEnabled()
        self.filmPreparationListBox.setSortingEnabled(False)
        item = self.filmPreparationListBox.item(0)
        item.setText(_translate("MainWindow", "Splice and perforation assessment", None))
        item = self.filmPreparationListBox.item(1)
        item.setText(_translate("MainWindow", "Splice repairs", None))
        item = self.filmPreparationListBox.item(2)
        item.setText(_translate("MainWindow", "Leader added", None))
        item = self.filmPreparationListBox.item(3)
        item.setText(_translate("MainWindow", "Perforation repairs", None))
        item = self.filmPreparationListBox.item(4)
        item.setText(_translate("MainWindow", "Recanned", None))
        item = self.filmPreparationListBox.item(5)
        item.setText(_translate("MainWindow", "Cleaning", None))
        item = self.filmPreparationListBox.item(6)
        item.setText(_translate("MainWindow", "Mould removal", None))
        self.filmPreparationListBox.setSortingEnabled(__sortingEnabled)
        self.lineEdit_2.setText(_translate("MainWindow", "Preparation Actions", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.scanningTab), _translate("MainWindow", "Scanning", None))
        __sortingEnabled = self.tapeDeckList.isSortingEnabled()
        self.tapeDeckList.setSortingEnabled(False)
        item = self.tapeDeckList.item(0)
        item.setText(_translate("MainWindow", "Basement - DVW-500P", None))
        item = self.tapeDeckList.item(1)
        item.setText(_translate("MainWindow", "Basement - UVW something", None))
        item = self.tapeDeckList.item(2)
        item.setText(_translate("MainWindow", "Basement - J30", None))
        item = self.tapeDeckList.item(3)
        item.setText(_translate("MainWindow", "Basement - JH3", None))
        item = self.tapeDeckList.item(4)
        item.setText(_translate("MainWindow", "Edit Suite - JH3", None))
        item = self.tapeDeckList.item(5)
        item.setText(_translate("MainWindow", "Edit Suite - UVW", None))
        self.tapeDeckList.setSortingEnabled(__sortingEnabled)
        self.tapeFormatComboBox.setItemText(0, _translate("MainWindow", "Source Format", None))
        self.tapeFormatComboBox.setItemText(1, _translate("MainWindow", "Betacam SP", None))
        self.tapeFormatComboBox.setItemText(2, _translate("MainWindow", "Digital Betacam", None))
        self.tapeFormatComboBox.setItemText(3, _translate("MainWindow", "Mini DV", None))
        self.tapeWorkstationComboBox.setItemText(0, _translate("MainWindow", "Select Workstation", None))
        self.tapeWorkstationComboBox.setItemText(1, _translate("MainWindow", "Edit Suite 1", None))
        self.tapeWorkstationComboBox.setItemText(2, _translate("MainWindow", "Edit Suite 2", None))
        self.tapeWorkstationComboBox.setItemText(3, _translate("MainWindow", "Edit suite 3", None))
        self.tapeWorkstationComboBox.setItemText(4, _translate("MainWindow", "Ingest Station 1", None))
        self.tapeWorkstationComboBox.setItemText(5, _translate("MainWindow", "Ingest Station 2", None))
        self.ffv1CheckBox.setText(_translate("MainWindow", "Transcoded to FFV1/MKV?", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tapeTab), _translate("MainWindow", "Tape", None))
        __sortingEnabled = self.rawAudioInterventions.isSortingEnabled()
        self.rawAudioInterventions.setSortingEnabled(False)
        item = self.rawAudioInterventions.item(0)
        item.setText(_translate("MainWindow", "De-Noise", None))
        item = self.rawAudioInterventions.item(1)
        item.setText(_translate("MainWindow", "De-Click", None))
        item = self.rawAudioInterventions.item(2)
        item.setText(_translate("MainWindow", "De-Crackle", None))
        item = self.rawAudioInterventions.item(3)
        item.setText(_translate("MainWindow", "Spectral Repair", None))
        item = self.rawAudioInterventions.item(4)
        item.setText(_translate("MainWindow", "Phase Correction", None))
        item = self.rawAudioInterventions.item(5)
        item.setText(_translate("MainWindow", "Master Gain Adjustment", None))
        item = self.rawAudioInterventions.item(6)
        item.setText(_translate("MainWindow", "Gain Automation", None))
        item = self.rawAudioInterventions.item(7)
        item.setText(_translate("MainWindow", "EQ Adjustment", None))
        item = self.rawAudioInterventions.item(8)
        item.setText(_translate("MainWindow", "Dither", None))
        item = self.rawAudioInterventions.item(9)
        item.setText(_translate("MainWindow", "Resample to 48khz", None))
        item = self.rawAudioInterventions.item(10)
        item.setText(_translate("MainWindow", "Sync edit and consolidation", None))
        item = self.rawAudioInterventions.item(11)
        item.setText(_translate("MainWindow", "Fade added at head", None))
        item = self.rawAudioInterventions.item(12)
        item.setText(_translate("MainWindow", "Fade added at tail", None))
        item = self.rawAudioInterventions.item(13)
        item.setText(_translate("MainWindow", "Other", None))
        self.rawAudioInterventions.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.rawAudioTab), _translate("MainWindow", "Raw Audio", None))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "Rescale via Frameflex", None))
        item = self.listWidget.item(1)
        item.setText(_translate("MainWindow", "Rescale via Baselight", None))
        item = self.listWidget.item(2)
        item.setText(_translate("MainWindow", "Set reference black and white via Baselight", None))
        item = self.listWidget.item(3)
        item.setText(_translate("MainWindow", "Set reference black and white via Baselight colour correction", None))
        item = self.listWidget.item(4)
        item.setText(_translate("MainWindow", "Local Scaling via Baselight", None))
        item = self.listWidget.item(5)
        item.setText(_translate("MainWindow", "Contrast Curve adjustment via Baselight", None))
        item = self.listWidget.item(6)
        item.setText(_translate("MainWindow", "Saturation adjustment via Baselight Hue Shift", None))
        item = self.listWidget.item(7)
        item.setText(_translate("MainWindow", "Hue Shift via Baselight Hue Shift", None))
        item = self.listWidget.item(8)
        item.setText(_translate("MainWindow", "Image Stabilisation via Avid No active image area lost", None))
        item = self.listWidget.item(9)
        item.setText(_translate("MainWindow", "Image Stabilisation via Avid but active image area lost", None))
        item = self.listWidget.item(10)
        item.setText(_translate("MainWindow", "Horizontal flipping", None))
        item = self.listWidget.item(11)
        item.setText(_translate("MainWindow", "Vertical flipping", None))
        item = self.listWidget.item(12)
        item.setText(_translate("MainWindow", "Damage removal via Paint effect", None))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.gradeTab), _translate("MainWindow", "Grade", None))
        self.userComboBox.setItemText(0, _translate("MainWindow", "Select User", None))
        self.userComboBox.setItemText(1, _translate("MainWindow", "Kieran O\'Leary", None))
        self.userComboBox.setItemText(2, _translate("MainWindow", "Brian Cash", None))
        self.userComboBox.setItemText(3, _translate("MainWindow", "Gavin Martin", None))
        self.userComboBox.setItemText(4, _translate("MainWindow", "Raelene Casey", None))
        self.userComboBox.setItemText(5, _translate("MainWindow", "Aaron Healy", None))
        self.userComboBox.setItemText(6, _translate("MainWindow", "Dean Kavanagh", None))
        self.lineEdit_3.setText(_translate("MainWindow", "User", None))
        self.oeTextBox.setStatusTip(_translate("MainWindow", "a", None))
        self.oeTextBox.setWhatsThis(_translate("MainWindow", "b", None))
        self.lineEdit_4.setText(_translate("MainWindow", "Object Entry Number eg OE6789", None))
        self.lineEdit_5.setText(_translate("MainWindow", "Filmographic Reference Number eg AF6789", None))
        self.lineEdit_6.setText(_translate("MainWindow", "Source Accession Number eg IFA-2010-1234", None))
        self.processButton.setText(_translate("MainWindow", "Process!", None))


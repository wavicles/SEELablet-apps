# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calibrator.ui'
#
# Created: Sat May  7 23:52:11 2016
#      by: PyQt4 UI code generator 4.11.3
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
        MainWindow.resize(838, 586)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_3 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_3.setMargin(0)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.widgetFrameOuter = QtGui.QFrame(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widgetFrameOuter.sizePolicy().hasHeightForWidth())
        self.widgetFrameOuter.setSizePolicy(sizePolicy)
        self.widgetFrameOuter.setStyleSheet(_fromUtf8(""))
        self.widgetFrameOuter.setFrameShape(QtGui.QFrame.StyledPanel)
        self.widgetFrameOuter.setFrameShadow(QtGui.QFrame.Raised)
        self.widgetFrameOuter.setObjectName(_fromUtf8("widgetFrameOuter"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.widgetFrameOuter)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setContentsMargins(0, 5, 0, 0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.frame = QtGui.QFrame(self.widgetFrameOuter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(0, 80))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout = QtGui.QGridLayout(self.frame)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.pushButton_2 = QtGui.QPushButton(self.frame)
        self.pushButton_2.setMinimumSize(QtCore.QSize(200, 0))
        self.pushButton_2.setMaximumSize(QtCore.QSize(200, 16777215))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout.addWidget(self.pushButton_2, 0, 0, 1, 1)
        self.progressBar = QtGui.QProgressBar(self.frame)
        self.progressBar.setMinimumSize(QtCore.QSize(0, 0))
        self.progressBar.setMaximumSize(QtCore.QSize(200, 16777215))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.gridLayout.addWidget(self.progressBar, 1, 0, 1, 1)
        self.pushButton_3 = QtGui.QPushButton(self.frame)
        self.pushButton_3.setMinimumSize(QtCore.QSize(120, 0))
        self.pushButton_3.setMaximumSize(QtCore.QSize(80, 16777215))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.gridLayout.addWidget(self.pushButton_3, 3, 4, 1, 1)
        self.comboBox = QtGui.QComboBox(self.frame)
        self.comboBox.setMaximumSize(QtCore.QSize(150, 16777215))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.comboBox, 1, 4, 1, 1)
        self.pushButton = QtGui.QPushButton(self.frame)
        self.pushButton.setMinimumSize(QtCore.QSize(94, 30))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 3, 0, 1, 4)
        self.msg = QtGui.QLabel(self.frame)
        self.msg.setObjectName(_fromUtf8("msg"))
        self.gridLayout.addWidget(self.msg, 1, 1, 1, 3)
        self.label = QtGui.QLabel(self.frame)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 4, 1, 1)
        self.dirnameLabel = QtGui.QLabel(self.frame)
        self.dirnameLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.dirnameLabel.setObjectName(_fromUtf8("dirnameLabel"))
        self.gridLayout.addWidget(self.dirnameLabel, 0, 1, 1, 3)
        self.verticalLayout_3.addWidget(self.frame)
        self.frame_2 = QtGui.QFrame(self.widgetFrameOuter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.frame_2)
        self.gridLayout_2.setMargin(2)
        self.gridLayout_2.setHorizontalSpacing(2)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.listWidget = QtGui.QListWidget(self.frame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.listWidget.setMaximumSize(QtCore.QSize(130, 16777215))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.gridLayout_2.addWidget(self.listWidget, 1, 1, 1, 1)
        self.frame_4 = QtGui.QFrame(self.frame_2)
        self.frame_4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName(_fromUtf8("frame_4"))
        self.verticalLayout = QtGui.QVBoxLayout(self.frame_4)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.Button480pF = QtGui.QPushButton(self.frame_4)
        self.Button480pF.setObjectName(_fromUtf8("Button480pF"))
        self.verticalLayout.addWidget(self.Button480pF)
        self.Button1uF = QtGui.QPushButton(self.frame_4)
        self.Button1uF.setObjectName(_fromUtf8("Button1uF"))
        self.verticalLayout.addWidget(self.Button1uF)
        self.Button100uF = QtGui.QPushButton(self.frame_4)
        self.Button100uF.setObjectName(_fromUtf8("Button100uF"))
        self.verticalLayout.addWidget(self.Button100uF)
        self.ButtonCCS = QtGui.QPushButton(self.frame_4)
        self.ButtonCCS.setObjectName(_fromUtf8("ButtonCCS"))
        self.verticalLayout.addWidget(self.ButtonCCS)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.gridLayout_2.addWidget(self.frame_4, 1, 2, 1, 1)
        self.deviceBox = QtGui.QComboBox(self.frame_2)
        self.deviceBox.setObjectName(_fromUtf8("deviceBox"))
        self.gridLayout_2.addWidget(self.deviceBox, 2, 1, 1, 2)
        self.pushButton_4 = QtGui.QPushButton(self.frame_2)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.gridLayout_2.addWidget(self.pushButton_4, 3, 1, 1, 2)
        self.scrollArea = QtGui.QScrollArea(self.frame_2)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 607, 425))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.gridLayout_4 = QtGui.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_4.setMargin(2)
        self.gridLayout_4.setSpacing(2)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.plot_area = QtGui.QGridLayout()
        self.plot_area.setObjectName(_fromUtf8("plot_area"))
        self.gridLayout_4.addLayout(self.plot_area, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.scrollArea, 1, 0, 3, 1)
        self.verticalLayout_3.addWidget(self.frame_2)
        self.gridLayout_3.addWidget(self.widgetFrameOuter, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 838, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.selectDir)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.startCalibration)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.saveData)
        QtCore.QObject.connect(self.Button480pF, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.cap480)
        QtCore.QObject.connect(self.Button1uF, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.cap1)
        QtCore.QObject.connect(self.Button100uF, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.cap100)
        QtCore.QObject.connect(self.ButtonCCS, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.ccs)
        QtCore.QObject.connect(self.pushButton_4, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.setDifferentAD7718)
        QtCore.QObject.connect(self.comboBox, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(QString)")), MainWindow.setINL_CHANNEL)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.widgetFrameOuter.setProperty("class", _translate("MainWindow", "PeripheralCollection", None))
        self.frame.setProperty("class", _translate("MainWindow", "PeripheralCollectionInner", None))
        self.pushButton_2.setText(_translate("MainWindow", "Select Directory", None))
        self.pushButton_3.setText(_translate("MainWindow", "Save Data", None))
        self.comboBox.setItemText(0, _translate("MainWindow", "AN8", None))
        self.comboBox.setItemText(1, _translate("MainWindow", "CAP", None))
        self.pushButton.setText(_translate("MainWindow", "Start Calibration", None))
        self.msg.setText(_translate("MainWindow", "msg", None))
        self.label.setText(_translate("MainWindow", "INL Channel", None))
        self.dirnameLabel.setText(_translate("MainWindow", ":calibration_data", None))
        self.frame_2.setProperty("class", _translate("MainWindow", "PeripheralCollectionInner", None))
        self.Button480pF.setText(_translate("MainWindow", "480pF", None))
        self.Button1uF.setText(_translate("MainWindow", "1uF", None))
        self.Button100uF.setText(_translate("MainWindow", "100uF", None))
        self.ButtonCCS.setText(_translate("MainWindow", "CCS", None))
        self.pushButton_4.setToolTip(_translate("MainWindow", "Select different device for 24-bit ADC", None))
        self.pushButton_4.setText(_translate("MainWindow", "Select precision ADC", None))


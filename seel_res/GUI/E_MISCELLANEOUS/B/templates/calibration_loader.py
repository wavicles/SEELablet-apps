# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'seel_res/GUI/E_MISCELLANEOUS/B/templates/calibration_loader.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(832, 519)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.West)
        self.tabWidget.setObjectName("tabWidget")
        self.T1 = QtWidgets.QWidget()
        self.T1.setObjectName("T1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.T1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widgetFrameOuter = QtWidgets.QFrame(self.T1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widgetFrameOuter.sizePolicy().hasHeightForWidth())
        self.widgetFrameOuter.setSizePolicy(sizePolicy)
        self.widgetFrameOuter.setStyleSheet("")
        self.widgetFrameOuter.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.widgetFrameOuter.setFrameShadow(QtWidgets.QFrame.Raised)
        self.widgetFrameOuter.setObjectName("widgetFrameOuter")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widgetFrameOuter)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.widgetFrameOuter)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.WidgetLayout = QtWidgets.QHBoxLayout()
        self.WidgetLayout.setObjectName("WidgetLayout")
        self.verticalLayout.addLayout(self.WidgetLayout)
        self.verticalLayout_2.addWidget(self.frame)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_2 = QtWidgets.QFrame(self.widgetFrameOuter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_2.setContentsMargins(2, 2, 2, 2)
        self.gridLayout_2.setHorizontalSpacing(2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(self.frame_2)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 655, 450))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_4.setContentsMargins(2, 2, 2, 2)
        self.gridLayout_4.setSpacing(2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.plot_area = QtWidgets.QGridLayout()
        self.plot_area.setObjectName("plot_area")
        self.gridLayout_4.addLayout(self.plot_area, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.scrollArea, 1, 0, 1, 1)
        self.horizontalLayout.addWidget(self.frame_2)
        self.LegendFrame = QtWidgets.QFrame(self.widgetFrameOuter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LegendFrame.sizePolicy().hasHeightForWidth())
        self.LegendFrame.setSizePolicy(sizePolicy)
        self.LegendFrame.setMinimumSize(QtCore.QSize(100, 0))
        self.LegendFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LegendFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.LegendFrame.setObjectName("LegendFrame")
        self.LegendLayout = QtWidgets.QVBoxLayout(self.LegendFrame)
        self.LegendLayout.setContentsMargins(2, 2, 2, 2)
        self.LegendLayout.setSpacing(2)
        self.LegendLayout.setObjectName("LegendLayout")
        self.listWidget = QtWidgets.QListWidget(self.LegendFrame)
        self.listWidget.setMaximumSize(QtCore.QSize(120, 16777215))
        self.listWidget.setObjectName("listWidget")
        self.LegendLayout.addWidget(self.listWidget)
        self.pushButton = QtWidgets.QPushButton(self.LegendFrame)
        self.pushButton.setObjectName("pushButton")
        self.LegendLayout.addWidget(self.pushButton)
        self.horizontalLayout.addWidget(self.LegendFrame)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addWidget(self.widgetFrameOuter)
        self.tabWidget.addTab(self.T1, "")
        self.T2 = QtWidgets.QWidget()
        self.T2.setObjectName("T2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.T2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_7 = QtWidgets.QFrame(self.T2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setMaximumSize(QtCore.QSize(650, 16777215))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_7)
        self.gridLayout.setContentsMargins(0, 5, 0, 2)
        self.gridLayout.setObjectName("gridLayout")
        self.Frame_4 = QtWidgets.QFrame(self.frame_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Frame_4.sizePolicy().hasHeightForWidth())
        self.Frame_4.setSizePolicy(sizePolicy)
        self.Frame_4.setProperty("PeripheralCollectionInner", "")
        self.Frame_4.setObjectName("Frame_4")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.Frame_4)
        self.gridLayout_5.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.line = QtWidgets.QFrame(self.Frame_4)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_5.addWidget(self.line, 0, 0, 1, 2)
        self.tableLayout = QtWidgets.QVBoxLayout()
        self.tableLayout.setObjectName("tableLayout")
        self.gridLayout_5.addLayout(self.tableLayout, 1, 0, 1, 2)
        self.gridLayout.addWidget(self.Frame_4, 0, 1, 1, 1)
        self.frame_4 = QtWidgets.QFrame(self.frame_7)
        self.frame_4.setMaximumSize(QtCore.QSize(120, 16777215))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.frame_4)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.ButtonSock = QtWidgets.QPushButton(self.frame_4)
        self.ButtonSock.setObjectName("ButtonSock")
        self.verticalLayout_4.addWidget(self.ButtonSock)
        self.Button330 = QtWidgets.QPushButton(self.frame_4)
        self.Button330.setObjectName("Button330")
        self.verticalLayout_4.addWidget(self.Button330)
        self.Button680 = QtWidgets.QPushButton(self.frame_4)
        self.Button680.setObjectName("Button680")
        self.verticalLayout_4.addWidget(self.Button680)
        self.Button2220 = QtWidgets.QPushButton(self.frame_4)
        self.Button2220.setObjectName("Button2220")
        self.verticalLayout_4.addWidget(self.Button2220)
        self.label_2 = QtWidgets.QLabel(self.frame_4)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.ButtonPCS = QtWidgets.QPushButton(self.frame_4)
        self.ButtonPCS.setObjectName("ButtonPCS")
        self.verticalLayout_4.addWidget(self.ButtonPCS)
        self.resistance = QtWidgets.QDoubleSpinBox(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.resistance.setFont(font)
        self.resistance.setMinimum(50.0)
        self.resistance.setMaximum(10000.0)
        self.resistance.setProperty("value", 1000.0)
        self.resistance.setObjectName("resistance")
        self.verticalLayout_4.addWidget(self.resistance)
        self.label_3 = QtWidgets.QLabel(self.frame_4)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.ButtonPCS_2 = QtWidgets.QPushButton(self.frame_4)
        self.ButtonPCS_2.setObjectName("ButtonPCS_2")
        self.verticalLayout_4.addWidget(self.ButtonPCS_2)
        self.resistance_SEN = QtWidgets.QDoubleSpinBox(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.resistance_SEN.setFont(font)
        self.resistance_SEN.setMinimum(50.0)
        self.resistance_SEN.setMaximum(10000.0)
        self.resistance_SEN.setProperty("value", 1000.0)
        self.resistance_SEN.setObjectName("resistance_SEN")
        self.verticalLayout_4.addWidget(self.resistance_SEN)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.ButtonReset = QtWidgets.QPushButton(self.frame_4)
        self.ButtonReset.setObjectName("ButtonReset")
        self.verticalLayout_4.addWidget(self.ButtonReset)
        self.gridLayout.addWidget(self.frame_4, 0, 0, 1, 1)
        self.widgetLayout = QtWidgets.QHBoxLayout()
        self.widgetLayout.setObjectName("widgetLayout")
        self.pushButton_9 = QtWidgets.QPushButton(self.frame_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy)
        self.pushButton_9.setMaximumSize(QtCore.QSize(70, 16777215))
        self.pushButton_9.setObjectName("pushButton_9")
        self.widgetLayout.addWidget(self.pushButton_9)
        self.pushButton_8 = QtWidgets.QPushButton(self.frame_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy)
        self.pushButton_8.setMaximumSize(QtCore.QSize(70, 16777215))
        self.pushButton_8.setObjectName("pushButton_8")
        self.widgetLayout.addWidget(self.pushButton_8)
        self.gridLayout.addLayout(self.widgetLayout, 1, 0, 1, 2)
        self.horizontalLayout_3.addWidget(self.frame_7)
        self.tabWidget.addTab(self.T2, "")
        self.gridLayout_3.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 832, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.listWidget.currentTextChanged['QString'].connect(MainWindow.selected)
        self.pushButton.clicked.connect(MainWindow.crop)
        self.pushButton_9.clicked.connect(MainWindow.recover)
        self.pushButton_8.clicked.connect(MainWindow.upload)
        self.ButtonReset.clicked.connect(MainWindow.reset)
        self.ButtonSock.clicked.connect(MainWindow.calSock)
        self.Button330.clicked.connect(MainWindow.cal330)
        self.Button680.clicked.connect(MainWindow.cal680)
        self.Button2220.clicked.connect(MainWindow.cal2220)
        self.ButtonPCS.clicked.connect(MainWindow.calPCS)
        self.ButtonPCS_2.clicked.connect(MainWindow.calSEN)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.widgetFrameOuter.setProperty("class", _translate("MainWindow", "PeripheralCollection"))
        self.frame_2.setProperty("class", _translate("MainWindow", "PeripheralCollectionInner"))
        self.LegendFrame.setProperty("class", _translate("MainWindow", "PeripheralCollectionInner"))
        self.pushButton.setText(_translate("MainWindow", "Crop"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.T1), _translate("MainWindow", "ADC, DAC and INL"))
        self.frame_7.setProperty("class", _translate("MainWindow", "PeripheralCollection"))
        self.Frame_4.setProperty("class", _translate("MainWindow", "PeripheralCollectionInner"))
        self.label.setText(_translate("MainWindow", "Click to Calibrate"))
        self.ButtonSock.setText(_translate("MainWindow", "Socket Cap"))
        self.Button330.setText(_translate("MainWindow", "330pF"))
        self.Button680.setText(_translate("MainWindow", "680pF"))
        self.Button2220.setText(_translate("MainWindow", "2220pF"))
        self.ButtonPCS.setText(_translate("MainWindow", "PCS(0.5,1,1.5mA)"))
        self.resistance.setSuffix(_translate("MainWindow", " Ohms"))
        self.ButtonPCS_2.setText(_translate("MainWindow", "SEN"))
        self.resistance_SEN.setSuffix(_translate("MainWindow", " Ohms"))
        self.ButtonReset.setText(_translate("MainWindow", "Reset Calibration"))
        self.pushButton_9.setText(_translate("MainWindow", "RECOVER"))
        self.pushButton_8.setText(_translate("MainWindow", "UPLOAD"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.T2), _translate("MainWindow", "CAP, PCS, SEN"))

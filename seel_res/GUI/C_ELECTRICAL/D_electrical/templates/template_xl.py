# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'seel_res/GUI/C_ELECTRICAL/D_electrical/templates/template_xl.ui'
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
        self.widgetFrameOuter = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widgetFrameOuter.sizePolicy().hasHeightForWidth())
        self.widgetFrameOuter.setSizePolicy(sizePolicy)
        self.widgetFrameOuter.setStyleSheet("")
        self.widgetFrameOuter.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.widgetFrameOuter.setFrameShadow(QtWidgets.QFrame.Raised)
        self.widgetFrameOuter.setObjectName("widgetFrameOuter")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widgetFrameOuter)
        self.verticalLayout_3.setContentsMargins(0, 5, 0, 0)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame = QtWidgets.QFrame(self.widgetFrameOuter)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setVerticalSpacing(3)
        self.gridLayout.setObjectName("gridLayout")
        self.resistanceInductor = QtWidgets.QDoubleSpinBox(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.resistanceInductor.sizePolicy().hasHeightForWidth())
        self.resistanceInductor.setSizePolicy(sizePolicy)
        self.resistanceInductor.setMaximumSize(QtCore.QSize(200, 16777215))
        self.resistanceInductor.setMaximum(10000.0)
        self.resistanceInductor.setProperty("value", 500.0)
        self.resistanceInductor.setObjectName("resistanceInductor")
        self.gridLayout.addWidget(self.resistanceInductor, 1, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setMinimumSize(QtCore.QSize(80, 0))
        self.pushButton_3.setMaximumSize(QtCore.QSize(80, 16777215))
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 1, 4, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 3, 1, 1)
        self.analysisLabel = QtWidgets.QLabel(self.frame)
        self.analysisLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.analysisLabel.setObjectName("analysisLabel")
        self.gridLayout.addWidget(self.analysisLabel, 0, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 1, 1, 1)
        self.resistance = QtWidgets.QDoubleSpinBox(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.resistance.sizePolicy().hasHeightForWidth())
        self.resistance.setSizePolicy(sizePolicy)
        self.resistance.setMaximumSize(QtCore.QSize(200, 16777215))
        self.resistance.setMaximum(10000.0)
        self.resistance.setProperty("value", 1000.0)
        self.resistance.setObjectName("resistance")
        self.gridLayout.addWidget(self.resistance, 1, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 2, 1, 1)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_4.setObjectName("frame_4")
        self.WidgetLayout = QtWidgets.QHBoxLayout(self.frame_4)
        self.WidgetLayout.setContentsMargins(0, 0, 0, 0)
        self.WidgetLayout.setSpacing(2)
        self.WidgetLayout.setObjectName("WidgetLayout")
        self.gridLayout.addWidget(self.frame_4, 0, 0, 2, 1)
        self.analysisLabel_2 = QtWidgets.QLabel(self.frame)
        self.analysisLabel_2.setAlignment(QtCore.Qt.AlignCenter)
        self.analysisLabel_2.setObjectName("analysisLabel_2")
        self.gridLayout.addWidget(self.analysisLabel_2, 0, 4, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.verticalLayout_3.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.widgetFrameOuter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.splitter = QtWidgets.QSplitter(self.frame_2)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.frame_3 = QtWidgets.QFrame(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMinimumSize(QtCore.QSize(300, 0))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.resultsTable = QtWidgets.QTableWidget(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.resultsTable.sizePolicy().hasHeightForWidth())
        self.resultsTable.setSizePolicy(sizePolicy)
        self.resultsTable.setAutoScrollMargin(10)
        self.resultsTable.setTextElideMode(QtCore.Qt.ElideRight)
        self.resultsTable.setGridStyle(QtCore.Qt.DashLine)
        self.resultsTable.setRowCount(50)
        self.resultsTable.setColumnCount(4)
        self.resultsTable.setObjectName("resultsTable")
        self.resultsTable.horizontalHeader().setCascadingSectionResizes(True)
        self.resultsTable.horizontalHeader().setDefaultSectionSize(70)
        self.resultsTable.horizontalHeader().setMinimumSectionSize(70)
        self.resultsTable.horizontalHeader().setSortIndicatorShown(False)
        self.resultsTable.horizontalHeader().setStretchLastSection(True)
        self.resultsTable.verticalHeader().setStretchLastSection(True)
        self.verticalLayout_2.addWidget(self.resultsTable)
        self.frame_6 = QtWidgets.QFrame(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.frame_6)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.plotAButton = QtWidgets.QPushButton(self.frame_6)
        self.plotAButton.setText("")
        self.plotAButton.setObjectName("plotAButton")
        self.horizontalLayout_3.addWidget(self.plotAButton)
        self.plotBButton = QtWidgets.QPushButton(self.frame_6)
        self.plotBButton.setText("")
        self.plotBButton.setObjectName("plotBButton")
        self.horizontalLayout_3.addWidget(self.plotBButton)
        self.verticalLayout_2.addWidget(self.frame_6)
        self.scrollArea = QtWidgets.QScrollArea(self.splitter)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 76, 429))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_4.setContentsMargins(2, 2, 2, 2)
        self.gridLayout_4.setSpacing(2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.plot_area = QtWidgets.QGridLayout()
        self.plot_area.setObjectName("plot_area")
        self.gridLayout_4.addLayout(self.plot_area, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_2.addWidget(self.splitter)
        self.verticalLayout_3.addWidget(self.frame_2)
        self.gridLayout_3.addWidget(self.widgetFrameOuter, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 832, 25))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.actionSave_as = QtWidgets.QAction(MainWindow)
        self.actionSave_as.setAutoRepeat(False)
        self.actionSave_as.setObjectName("actionSave_as")
        self.menuFile.addAction(self.actionSave_as)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.plotAButton.clicked.connect(MainWindow.plotA)
        self.plotBButton.clicked.connect(MainWindow.plotB)
        self.pushButton.clicked.connect(MainWindow.fit)
        self.actionSave_as.triggered.connect(MainWindow.saveFile)
        self.pushButton_3.clicked.connect(MainWindow.savePlot)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.widgetFrameOuter.setProperty("class", _translate("MainWindow", "PeripheralCollection"))
        self.resistanceInductor.setToolTip(_translate("MainWindow", "The Voltage drop measured across the inductor is a function of\n"
"both XL(Freq dependent ), and R.\n"
" Ohmic Voltage drop due to R must therefore be subtracted"))
        self.resistanceInductor.setSuffix(_translate("MainWindow", " Ohms"))
        self.pushButton_3.setText(_translate("MainWindow", "Save Data"))
        self.pushButton.setText(_translate("MainWindow", "Fit Curves"))
        self.analysisLabel.setText(_translate("MainWindow", "Analyze"))
        self.label_4.setToolTip(_translate("MainWindow", "The Voltage drop measured across the inductor is a function of\n"
"both XL(Freq dependent ), and R.\n"
" Ohmic Voltage drop due to R must therefore be subtracted"))
        self.label_4.setText(_translate("MainWindow", "DC Resistance of The Inductor"))
        self.resistance.setSuffix(_translate("MainWindow", " Ohms"))
        self.label.setText(_translate("MainWindow", "Load Resistance"))
        self.analysisLabel_2.setText(_translate("MainWindow", "Save"))
        self.frame_2.setProperty("class", _translate("MainWindow", "PeripheralCollectionInner"))
        self.resultsTable.setSortingEnabled(False)
        self.label_3.setText(_translate("MainWindow", "Plot:"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionSave_as.setText(_translate("MainWindow", "save as"))
        self.actionSave_as.setToolTip(_translate("MainWindow", "save data contained in the table"))
        self.actionSave_as.setShortcut(_translate("MainWindow", "Ctrl+S"))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'outputs.ui'
#
# Created: Sun Nov 15 17:06:51 2015
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
        MainWindow.resize(332, 499)
        MainWindow.setMouseTracking(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../../../../usr/share/pixmaps/cubeview48.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setToolTip(_fromUtf8(""))
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(_fromUtf8("QPushButton {\n"
"color: #333;\n"
"border: 2px solid #555;\n"
"border-radius: 11px;\n"
"padding: 5px;\n"
"background: qradialgradient(cx: 0.3, cy: -0.4,\n"
"fx: 0.3, fy: -0.4,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #888);\n"
"min-width: 80px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background: qradialgradient(cx: 0.4, cy: -0.1,\n"
"fx: 0.4, fy: -0.1,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #ddd);\n"
"}\n"
"\n"
"QFrame.PeripheralCollection{\n"
"border-top-left-radius: 5px;\n"
"border-top-right-radius: 5px;\n"
"border: 1px solid black;\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"stop: 0 #6af, stop: 0.1 #689);\n"
"}\n"
"QFrame.PeripheralCollection QLabel {\n"
"color: white;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QFrame.PeripheralCollectionInner {\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"stop: 0 #abe, stop: 0.7 #aba);\n"
"border: none;\n"
"border-top: 1px solid black;\n"
"}\n"
"\n"
"QFrame.PeripheralCollectionInner QLabel{\n"
"color: black;\n"
"}\n"
"\n"
"\n"
""))
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setTabShape(QtGui.QTabWidget.Rounded)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_3 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_3.setContentsMargins(2, 9, 3, 3)
        self.gridLayout_3.setHorizontalSpacing(3)
        self.gridLayout_3.setVerticalSpacing(9)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.frame_3 = QtGui.QFrame(self.centralwidget)
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setContentsMargins(0, 5, 0, 0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label = QtGui.QLabel(self.frame_3)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_2.addWidget(self.label)
        self.Frame = QtGui.QFrame(self.frame_3)
        self.Frame.setProperty("PeripheralCollectionInner", _fromUtf8(""))
        self.Frame.setObjectName(_fromUtf8("Frame"))
        self.gridLayout = QtGui.QGridLayout(self.Frame)
        self.gridLayout.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.PV3_LABEL = QtGui.QLabel(self.Frame)
        self.PV3_LABEL.setObjectName(_fromUtf8("PV3_LABEL"))
        self.gridLayout.addWidget(self.PV3_LABEL, 2, 1, 1, 1)
        self.sinebox2 = QtGui.QDoubleSpinBox(self.Frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sinebox2.sizePolicy().hasHeightForWidth())
        self.sinebox2.setSizePolicy(sizePolicy)
        self.sinebox2.setMaximum(1000000.0)
        self.sinebox2.setObjectName(_fromUtf8("sinebox2"))
        self.gridLayout.addWidget(self.sinebox2, 4, 2, 1, 1)
        self.PV2_LABEL = QtGui.QLabel(self.Frame)
        self.PV2_LABEL.setObjectName(_fromUtf8("PV2_LABEL"))
        self.gridLayout.addWidget(self.PV2_LABEL, 1, 1, 1, 1)
        self.label_24 = QtGui.QLabel(self.Frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.gridLayout.addWidget(self.label_24, 6, 0, 1, 1)
        self.sinebox1 = QtGui.QDoubleSpinBox(self.Frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sinebox1.sizePolicy().hasHeightForWidth())
        self.sinebox1.setSizePolicy(sizePolicy)
        self.sinebox1.setMaximum(1000000.0)
        self.sinebox1.setObjectName(_fromUtf8("sinebox1"))
        self.gridLayout.addWidget(self.sinebox1, 5, 2, 1, 1)
        self.WAVE2_FREQ = QtGui.QLabel(self.Frame)
        self.WAVE2_FREQ.setObjectName(_fromUtf8("WAVE2_FREQ"))
        self.gridLayout.addWidget(self.WAVE2_FREQ, 5, 1, 1, 1)
        self.horizontalSlider = QtGui.QSlider(self.Frame)
        self.horizontalSlider.setMaximum(4095)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName(_fromUtf8("horizontalSlider"))
        self.gridLayout.addWidget(self.horizontalSlider, 0, 2, 1, 1)
        self.sinePhase_phase = QtGui.QDoubleSpinBox(self.Frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sinePhase_phase.sizePolicy().hasHeightForWidth())
        self.sinePhase_phase.setSizePolicy(sizePolicy)
        self.sinePhase_phase.setDecimals(1)
        self.sinePhase_phase.setMaximum(359.0)
        self.sinePhase_phase.setObjectName(_fromUtf8("sinePhase_phase"))
        self.gridLayout.addWidget(self.sinePhase_phase, 7, 1, 1, 1)
        self.label_22 = QtGui.QLabel(self.Frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.gridLayout.addWidget(self.label_22, 5, 0, 1, 1)
        self.horizontalSlider_4 = QtGui.QSlider(self.Frame)
        self.horizontalSlider_4.setMaximum(4095)
        self.horizontalSlider_4.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_4.setObjectName(_fromUtf8("horizontalSlider_4"))
        self.gridLayout.addWidget(self.horizontalSlider_4, 3, 2, 1, 1)
        self.horizontalSlider_3 = QtGui.QSlider(self.Frame)
        self.horizontalSlider_3.setMaximum(4095)
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3.setObjectName(_fromUtf8("horizontalSlider_3"))
        self.gridLayout.addWidget(self.horizontalSlider_3, 2, 2, 1, 1)
        self.label_8 = QtGui.QLabel(self.Frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 3, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.Frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.horizontalSlider_2 = QtGui.QSlider(self.Frame)
        self.horizontalSlider_2.setMaximum(4095)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName(_fromUtf8("horizontalSlider_2"))
        self.gridLayout.addWidget(self.horizontalSlider_2, 1, 2, 1, 1)
        self.WAVE1_FREQ = QtGui.QLabel(self.Frame)
        self.WAVE1_FREQ.setObjectName(_fromUtf8("WAVE1_FREQ"))
        self.gridLayout.addWidget(self.WAVE1_FREQ, 4, 1, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(self.Frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout.addWidget(self.pushButton_2, 6, 2, 2, 1)
        self.PV1_LABEL = QtGui.QLabel(self.Frame)
        self.PV1_LABEL.setObjectName(_fromUtf8("PV1_LABEL"))
        self.gridLayout.addWidget(self.PV1_LABEL, 0, 1, 1, 1)
        self.label_15 = QtGui.QLabel(self.Frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.gridLayout.addWidget(self.label_15, 4, 0, 1, 1)
        self.label_6 = QtGui.QLabel(self.Frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1)
        self.PCS_LABEL = QtGui.QLabel(self.Frame)
        self.PCS_LABEL.setObjectName(_fromUtf8("PCS_LABEL"))
        self.gridLayout.addWidget(self.PCS_LABEL, 3, 1, 1, 1)
        self.sinePhase_freq = QtGui.QDoubleSpinBox(self.Frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sinePhase_freq.sizePolicy().hasHeightForWidth())
        self.sinePhase_freq.setSizePolicy(sizePolicy)
        self.sinePhase_freq.setMinimum(5.0)
        self.sinePhase_freq.setMaximum(5000.0)
        self.sinePhase_freq.setObjectName(_fromUtf8("sinePhase_freq"))
        self.gridLayout.addWidget(self.sinePhase_freq, 7, 0, 1, 1)
        self.label_25 = QtGui.QLabel(self.Frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.gridLayout.addWidget(self.label_25, 6, 1, 1, 1)
        self.label_7 = QtGui.QLabel(self.Frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 1, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.Frame)
        self.gridLayout_3.addWidget(self.frame_3, 0, 0, 1, 1)
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setStyleSheet(_fromUtf8(""))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.verticalLayout = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setContentsMargins(0, 5, 0, 0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_2 = QtGui.QLabel(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.Frame2 = QtGui.QFrame(self.frame)
        self.Frame2.setObjectName(_fromUtf8("Frame2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.Frame2)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_3 = QtGui.QLabel(self.Frame2)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.SQR_FREQ = QtGui.QSpinBox(self.Frame2)
        self.SQR_FREQ.setMinimum(1)
        self.SQR_FREQ.setMaximum(1000000)
        self.SQR_FREQ.setProperty("value", 500)
        self.SQR_FREQ.setObjectName(_fromUtf8("SQR_FREQ"))
        self.gridLayout_2.addWidget(self.SQR_FREQ, 0, 1, 1, 2)
        self.label_18 = QtGui.QLabel(self.Frame2)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.gridLayout_2.addWidget(self.label_18, 1, 0, 1, 1)
        self.label_20 = QtGui.QLabel(self.Frame2)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.gridLayout_2.addWidget(self.label_20, 1, 1, 1, 1)
        self.label_21 = QtGui.QLabel(self.Frame2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.gridLayout_2.addWidget(self.label_21, 1, 2, 1, 1)
        self.SQR_NM = QtGui.QComboBox(self.Frame2)
        self.SQR_NM.setObjectName(_fromUtf8("SQR_NM"))
        self.SQR_NM.addItem(_fromUtf8(""))
        self.SQR_NM.addItem(_fromUtf8(""))
        self.SQR_NM.addItem(_fromUtf8(""))
        self.SQR_NM.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.SQR_NM, 2, 0, 1, 1)
        self.SQR_PH = QtGui.QSpinBox(self.Frame2)
        self.SQR_PH.setMaximum(360)
        self.SQR_PH.setObjectName(_fromUtf8("SQR_PH"))
        self.gridLayout_2.addWidget(self.SQR_PH, 2, 1, 1, 1)
        self.SQR_DC = QtGui.QSpinBox(self.Frame2)
        self.SQR_DC.setMaximum(100)
        self.SQR_DC.setProperty("value", 50)
        self.SQR_DC.setObjectName(_fromUtf8("SQR_DC"))
        self.gridLayout_2.addWidget(self.SQR_DC, 2, 2, 1, 1)
        self.pushButton_7 = QtGui.QPushButton(self.Frame2)
        self.pushButton_7.setMaximumSize(QtCore.QSize(16777215, 25))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.gridLayout_2.addWidget(self.pushButton_7, 3, 0, 1, 3)
        self.verticalLayout.addWidget(self.Frame2)
        self.gridLayout_3.addWidget(self.frame, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionSave_as = QtGui.QAction(MainWindow)
        self.actionSave_as.setObjectName(_fromUtf8("actionSave_as"))

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.horizontalSlider, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), MainWindow.setPV1)
        QtCore.QObject.connect(self.horizontalSlider_2, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), MainWindow.setPV2)
        QtCore.QObject.connect(self.horizontalSlider_3, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), MainWindow.setPV3)
        QtCore.QObject.connect(self.horizontalSlider_4, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), MainWindow.setPCS)
        QtCore.QObject.connect(self.sinebox2, QtCore.SIGNAL(_fromUtf8("valueChanged(double)")), MainWindow.setSINE1)
        QtCore.QObject.connect(self.sinebox1, QtCore.SIGNAL(_fromUtf8("valueChanged(double)")), MainWindow.setSINE2)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.setSinePhase)
        QtCore.QObject.connect(self.pushButton_7, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.sqr_update)
        QtCore.QObject.connect(self.SQR_PH, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), MainWindow.sqr_phase)
        QtCore.QObject.connect(self.SQR_DC, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), MainWindow.sqr_dc)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Control various outputs", None))
        self.frame_3.setProperty("class", _translate("MainWindow", "PeripheralCollection", None))
        self.label.setText(_translate("MainWindow", "Outputs", None))
        self.Frame.setProperty("class", _translate("MainWindow", "PeripheralCollectionInner", None))
        self.PV3_LABEL.setText(_translate("MainWindow", "0 - 3.3V", None))
        self.PV2_LABEL.setText(_translate("MainWindow", "-3.3 to 3.3V", None))
        self.label_24.setText(_translate("MainWindow", "Frequency", None))
        self.WAVE2_FREQ.setText(_translate("MainWindow", "10Hz to 5KHz", None))
        self.label_22.setText(_translate("MainWindow", "Wave 2", None))
        self.label_8.setText(_translate("MainWindow", "PCS", None))
        self.label_5.setText(_translate("MainWindow", "PV3", None))
        self.WAVE1_FREQ.setText(_translate("MainWindow", "10Hz to 5KHz", None))
        self.pushButton_2.setText(_translate("MainWindow", "SET PHASE", None))
        self.PV1_LABEL.setText(_translate("MainWindow", "-5 to 5V", None))
        self.label_15.setText(_translate("MainWindow", "Wave 1", None))
        self.label_6.setText(_translate("MainWindow", "PV1 ", None))
        self.PCS_LABEL.setText(_translate("MainWindow", "0-3.3mA", None))
        self.label_25.setText(_translate("MainWindow", "phase", None))
        self.label_7.setText(_translate("MainWindow", "PV2 ", None))
        self.frame.setProperty("class", _translate("MainWindow", "PeripheralCollection", None))
        self.label_2.setText(_translate("MainWindow", "Phase Correlated Square Waves", None))
        self.Frame2.setProperty("class", _translate("MainWindow", "PeripheralCollectionInner", None))
        self.label_3.setText(_translate("MainWindow", "Frequency", None))
        self.label_18.setText(_translate("MainWindow", "Output", None))
        self.label_20.setText(_translate("MainWindow", "Phase", None))
        self.label_21.setText(_translate("MainWindow", "Duty Cycle", None))
        self.SQR_NM.setItemText(0, _translate("MainWindow", "SQ1", None))
        self.SQR_NM.setItemText(1, _translate("MainWindow", "SQ2", None))
        self.SQR_NM.setItemText(2, _translate("MainWindow", "OD1", None))
        self.SQR_NM.setItemText(3, _translate("MainWindow", "OD2", None))
        self.SQR_DC.setSuffix(_translate("MainWindow", "%", None))
        self.pushButton_7.setText(_translate("MainWindow", "UPDATE", None))
        self.actionSave_as.setText(_translate("MainWindow", "Save as", None))


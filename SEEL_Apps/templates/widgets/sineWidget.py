# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sineWidget.ui'
#
# Created: Wed May  4 12:48:03 2016
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(336, 161)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.frame_4 = QtGui.QFrame(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setMaximumSize(QtCore.QSize(400, 16777215))
        self.frame_4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName(_fromUtf8("frame_4"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setSpacing(5)
        self.verticalLayout_4.setContentsMargins(0, 5, 0, 0)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.frame = QtGui.QFrame(self.frame_4)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_3 = QtGui.QLabel(self.frame)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        self.commandLinkButton = QtGui.QCommandLinkButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.commandLinkButton.sizePolicy().hasHeightForWidth())
        self.commandLinkButton.setSizePolicy(sizePolicy)
        self.commandLinkButton.setMinimumSize(QtCore.QSize(94, 0))
        self.commandLinkButton.setMaximumSize(QtCore.QSize(30, 30))
        self.commandLinkButton.setObjectName(_fromUtf8("commandLinkButton"))
        self.horizontalLayout_2.addWidget(self.commandLinkButton)
        self.verticalLayout_4.addWidget(self.frame)
        self.Frame_3 = QtGui.QFrame(self.frame_4)
        self.Frame_3.setProperty("PeripheralCollectionInner", _fromUtf8(""))
        self.Frame_3.setObjectName(_fromUtf8("Frame_3"))
        self.gridLayout_3 = QtGui.QGridLayout(self.Frame_3)
        self.gridLayout_3.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label_30 = QtGui.QLabel(self.Frame_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_30.sizePolicy().hasHeightForWidth())
        self.label_30.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_30.setFont(font)
        self.label_30.setObjectName(_fromUtf8("label_30"))
        self.gridLayout_3.addWidget(self.label_30, 3, 0, 1, 1)
        self.SINE1BOX = QtGui.QDoubleSpinBox(self.Frame_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SINE1BOX.sizePolicy().hasHeightForWidth())
        self.SINE1BOX.setSizePolicy(sizePolicy)
        self.SINE1BOX.setMinimum(0.2)
        self.SINE1BOX.setMaximum(5000.0)
        self.SINE1BOX.setProperty("value", 500.0)
        self.SINE1BOX.setObjectName(_fromUtf8("SINE1BOX"))
        self.gridLayout_3.addWidget(self.SINE1BOX, 0, 2, 1, 1)
        self.WAVE2_FREQ = QtGui.QLabel(self.Frame_3)
        self.WAVE2_FREQ.setObjectName(_fromUtf8("WAVE2_FREQ"))
        self.gridLayout_3.addWidget(self.WAVE2_FREQ, 1, 1, 1, 1)
        self.label_29 = QtGui.QLabel(self.Frame_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_29.sizePolicy().hasHeightForWidth())
        self.label_29.setSizePolicy(sizePolicy)
        self.label_29.setObjectName(_fromUtf8("label_29"))
        self.gridLayout_3.addWidget(self.label_29, 1, 0, 1, 1)
        self.SINE2BOX = QtGui.QDoubleSpinBox(self.Frame_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SINE2BOX.sizePolicy().hasHeightForWidth())
        self.SINE2BOX.setSizePolicy(sizePolicy)
        self.SINE2BOX.setMinimum(0.2)
        self.SINE2BOX.setMaximum(5000.0)
        self.SINE2BOX.setProperty("value", 500.0)
        self.SINE2BOX.setObjectName(_fromUtf8("SINE2BOX"))
        self.gridLayout_3.addWidget(self.SINE2BOX, 1, 2, 1, 1)
        self.WAVE1_FREQ = QtGui.QLabel(self.Frame_3)
        self.WAVE1_FREQ.setObjectName(_fromUtf8("WAVE1_FREQ"))
        self.gridLayout_3.addWidget(self.WAVE1_FREQ, 0, 1, 1, 1)
        self.label_17 = QtGui.QLabel(self.Frame_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.gridLayout_3.addWidget(self.label_17, 0, 0, 1, 1)
        self.comboBox = QtGui.QComboBox(self.Frame_3)
        self.comboBox.setMaximumSize(QtCore.QSize(70, 16777215))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.gridLayout_3.addWidget(self.comboBox, 0, 3, 1, 1)
        self.comboBox_2 = QtGui.QComboBox(self.Frame_3)
        self.comboBox_2.setMaximumSize(QtCore.QSize(70, 16777215))
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.gridLayout_3.addWidget(self.comboBox_2, 1, 3, 1, 1)
        self.SINEPHASE = QtGui.QDoubleSpinBox(self.Frame_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SINEPHASE.sizePolicy().hasHeightForWidth())
        self.SINEPHASE.setSizePolicy(sizePolicy)
        self.SINEPHASE.setDecimals(1)
        self.SINEPHASE.setMaximum(359.0)
        self.SINEPHASE.setObjectName(_fromUtf8("SINEPHASE"))
        self.gridLayout_3.addWidget(self.SINEPHASE, 3, 1, 1, 1)
        self.pushButton_4 = QtGui.QPushButton(self.Frame_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.gridLayout_3.addWidget(self.pushButton_4, 3, 2, 1, 2)
        self.verticalLayout_4.addWidget(self.Frame_3)
        self.verticalLayout.addWidget(self.frame_4)

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.commandLinkButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.loadSineTable)
        QtCore.QObject.connect(self.SINE1BOX, QtCore.SIGNAL(_fromUtf8("valueChanged(double)")), Form.setSINE1)
        QtCore.QObject.connect(self.SINE2BOX, QtCore.SIGNAL(_fromUtf8("valueChanged(double)")), Form.setSINE2)
        QtCore.QObject.connect(self.pushButton_4, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.setSinePhase)
        QtCore.QObject.connect(self.comboBox, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(int)")), Form.setW1Type)
        QtCore.QObject.connect(self.comboBox_2, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(int)")), Form.setW2Type)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.frame_4.setProperty("class", _translate("Form", "PeripheralCollection", None))
        self.label_3.setText(_translate("Form", "Arbitrary Waveform Generators", None))
        self.commandLinkButton.setToolTip(_translate("Form", "Edit the waveform table by setting a new function", None))
        self.commandLinkButton.setText(_translate("Form", "Edit", None))
        self.Frame_3.setProperty("class", _translate("Form", "PeripheralCollectionInner", None))
        self.label_30.setText(_translate("Form", "phase", None))
        self.WAVE2_FREQ.setText(_translate("Form", "10Hz to 5KHz", None))
        self.label_29.setText(_translate("Form", "W2", None))
        self.WAVE1_FREQ.setText(_translate("Form", "10Hz to 5KHz", None))
        self.label_17.setText(_translate("Form", "W1", None))
        self.comboBox.setItemText(0, _translate("Form", "sine", None))
        self.comboBox.setItemText(1, _translate("Form", "tria", None))
        self.comboBox_2.setItemText(0, _translate("Form", "sine", None))
        self.comboBox_2.setItemText(1, _translate("Form", "tria", None))
        self.pushButton_4.setText(_translate("Form", "SET PHASE", None))


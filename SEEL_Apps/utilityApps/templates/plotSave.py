# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'plotSave.ui'
#
# Created: Wed May 11 13:01:15 2016
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
        MainWindow.resize(878, 555)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setMargin(1)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.table = QtGui.QTableWidget(self.centralwidget)
        self.table.setFrameShadow(QtGui.QFrame.Sunken)
        self.table.setAutoScrollMargin(10)
        self.table.setAlternatingRowColors(True)
        self.table.setRowCount(100)
        self.table.setColumnCount(6)
        self.table.setObjectName(_fromUtf8("table"))
        self.table.horizontalHeader().setDefaultSectionSize(120)
        self.table.horizontalHeader().setMinimumSectionSize(40)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.verticalHeader().setCascadingSectionResizes(True)
        self.table.verticalHeader().setDefaultSectionSize(20)
        self.table.verticalHeader().setHighlightSections(True)
        self.table.verticalHeader().setMinimumSectionSize(15)
        self.verticalLayout.addWidget(self.table)
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout = QtGui.QGridLayout(self.frame)
        self.gridLayout.setMargin(3)
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setVerticalSpacing(3)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 2, 1)
        self.headerBox = QtGui.QCheckBox(self.frame)
        self.headerBox.setChecked(True)
        self.headerBox.setObjectName(_fromUtf8("headerBox"))
        self.gridLayout.addWidget(self.headerBox, 1, 3, 1, 1)
        self.pushButton = QtGui.QPushButton(self.frame)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 0, 0, 2, 1)
        self.line_3 = QtGui.QFrame(self.frame)
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.gridLayout.addWidget(self.line_3, 0, 2, 2, 2)
        self.line_7 = QtGui.QFrame(self.frame)
        self.line_7.setFrameShape(QtGui.QFrame.VLine)
        self.line_7.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_7.setObjectName(_fromUtf8("line_7"))
        self.gridLayout.addWidget(self.line_7, 3, 7, 1, 1)
        self.imageWidthBox = QtGui.QSpinBox(self.frame)
        self.imageWidthBox.setEnabled(False)
        self.imageWidthBox.setMinimum(100)
        self.imageWidthBox.setMaximum(4000)
        self.imageWidthBox.setObjectName(_fromUtf8("imageWidthBox"))
        self.gridLayout.addWidget(self.imageWidthBox, 3, 6, 1, 1)
        self.line = QtGui.QFrame(self.frame)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 0, 7, 2, 1)
        self.delims = QtGui.QComboBox(self.frame)
        self.delims.setMaximumSize(QtCore.QSize(200, 16777215))
        self.delims.setObjectName(_fromUtf8("delims"))
        self.delims.addItem(_fromUtf8(""))
        self.delims.addItem(_fromUtf8(""))
        self.delims.addItem(_fromUtf8(""))
        self.delims.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.delims, 0, 6, 2, 1)
        self.label = QtGui.QLabel(self.frame)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 5, 2, 1)
        self.line_2 = QtGui.QFrame(self.frame)
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout.addWidget(self.line_2, 0, 4, 2, 1)
        self.pushButton_2 = QtGui.QPushButton(self.frame)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout.addWidget(self.pushButton_2, 0, 8, 2, 1)
        self.label_3 = QtGui.QLabel(self.frame)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 3, 5, 1, 1)
        self.saveImageButton = QtGui.QPushButton(self.frame)
        self.saveImageButton.setEnabled(False)
        self.saveImageButton.setObjectName(_fromUtf8("saveImageButton"))
        self.gridLayout.addWidget(self.saveImageButton, 3, 8, 1, 1)
        self.line_8 = QtGui.QFrame(self.frame)
        self.line_8.setFrameShape(QtGui.QFrame.HLine)
        self.line_8.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_8.setObjectName(_fromUtf8("line_8"))
        self.gridLayout.addWidget(self.line_8, 2, 0, 1, 9)
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.close)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.save)
        QtCore.QObject.connect(self.saveImageButton, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.saveImage)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Save Your Results", None))
        self.headerBox.setText(_translate("MainWindow", "Include Headers", None))
        self.pushButton.setText(_translate("MainWindow", "Cancel", None))
        self.delims.setItemText(0, _translate("MainWindow", "space", None))
        self.delims.setItemText(1, _translate("MainWindow", "tab", None))
        self.delims.setItemText(2, _translate("MainWindow", "comma", None))
        self.delims.setItemText(3, _translate("MainWindow", "semicolon", None))
        self.label.setText(_translate("MainWindow", "Separator:", None))
        self.pushButton_2.setText(_translate("MainWindow", "Save Data", None))
        self.label_3.setText(_translate("MainWindow", "Width:", None))
        self.saveImageButton.setText(_translate("MainWindow", "Save image", None))


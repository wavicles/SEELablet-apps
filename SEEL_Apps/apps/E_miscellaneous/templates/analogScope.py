# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'analogScope.ui'
#
# Created: Fri Apr 15 13:33:18 2016
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
        MainWindow.resize(868, 535)
        MainWindow.setMinimumSize(QtCore.QSize(300, 0))
        MainWindow.setMouseTracking(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../../../../../usr/share/pixmaps/cubeview48.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setToolTip(_fromUtf8(""))
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(_fromUtf8(""))
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setTabShape(QtGui.QTabWidget.Rounded)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setSpacing(1)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.splitter = QtGui.QSplitter(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.plot_area_frame = QtGui.QFrame(self.splitter)
        self.plot_area_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.plot_area_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.plot_area_frame.setObjectName(_fromUtf8("plot_area_frame"))
        self.plot_area = QtGui.QVBoxLayout(self.plot_area_frame)
        self.plot_area.setSpacing(2)
        self.plot_area.setMargin(0)
        self.plot_area.setObjectName(_fromUtf8("plot_area"))
        self.frame_4 = QtGui.QFrame(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setMinimumSize(QtCore.QSize(300, 0))
        self.frame_4.setMaximumSize(QtCore.QSize(300, 16777215))
        self.frame_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame_4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName(_fromUtf8("frame_4"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(2, 2, 3, 2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        spacerItem = QtGui.QSpacerItem(20, 1, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.label_3 = QtGui.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setMargin(5)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_2.addWidget(self.label_3)
        self.frame_11 = QtGui.QFrame(self.frame_4)
        self.frame_11.setMinimumSize(QtCore.QSize(0, 115))
        self.frame_11.setMaximumSize(QtCore.QSize(16777215, 115))
        self.frame_11.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_11.setObjectName(_fromUtf8("frame_11"))
        self.CH1_REMAPS = QtGui.QComboBox(self.frame_11)
        self.CH1_REMAPS.setGeometry(QtCore.QRect(220, 10, 61, 21))
        self.CH1_REMAPS.setObjectName(_fromUtf8("CH1_REMAPS"))
        self.CH1_LABEL = QtGui.QLabel(self.frame_11)
        self.CH1_LABEL.setGeometry(QtCore.QRect(20, 10, 51, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.CH1_LABEL.setFont(font)
        self.CH1_LABEL.setObjectName(_fromUtf8("CH1_LABEL"))
        self.CH2_LABEL = QtGui.QLabel(self.frame_11)
        self.CH2_LABEL.setGeometry(QtCore.QRect(20, 50, 51, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.CH2_LABEL.setFont(font)
        self.CH2_LABEL.setObjectName(_fromUtf8("CH2_LABEL"))
        self.comboBox_6 = QtGui.QComboBox(self.frame_11)
        self.comboBox_6.setGeometry(QtCore.QRect(127, 10, 91, 21))
        self.comboBox_6.setObjectName(_fromUtf8("comboBox_6"))
        self.comboBox_6.addItem(_fromUtf8(""))
        self.comboBox_6.addItem(_fromUtf8(""))
        self.comboBox_6.addItem(_fromUtf8(""))
        self.comboBox_6.addItem(_fromUtf8(""))
        self.comboBox_6.addItem(_fromUtf8(""))
        self.comboBox_6.addItem(_fromUtf8(""))
        self.comboBox_6.addItem(_fromUtf8(""))
        self.comboBox_6.addItem(_fromUtf8(""))
        self.label_30 = QtGui.QLabel(self.frame_11)
        self.label_30.setGeometry(QtCore.QRect(80, 10, 51, 17))
        self.label_30.setObjectName(_fromUtf8("label_30"))
        self.label_31 = QtGui.QLabel(self.frame_11)
        self.label_31.setGeometry(QtCore.QRect(80, 50, 51, 17))
        self.label_31.setObjectName(_fromUtf8("label_31"))
        self.CH1_ENABLE = QtGui.QCheckBox(self.frame_11)
        self.CH1_ENABLE.setGeometry(QtCore.QRect(0, 10, 21, 20))
        self.CH1_ENABLE.setText(_fromUtf8(""))
        self.CH1_ENABLE.setChecked(True)
        self.CH1_ENABLE.setObjectName(_fromUtf8("CH1_ENABLE"))
        self.CH2_ENABLE = QtGui.QCheckBox(self.frame_11)
        self.CH2_ENABLE.setGeometry(QtCore.QRect(0, 50, 21, 20))
        self.CH2_ENABLE.setText(_fromUtf8(""))
        self.CH2_ENABLE.setObjectName(_fromUtf8("CH2_ENABLE"))
        self.CH3_ENABLE = QtGui.QCheckBox(self.frame_11)
        self.CH3_ENABLE.setGeometry(QtCore.QRect(0, 90, 21, 20))
        self.CH3_ENABLE.setText(_fromUtf8(""))
        self.CH3_ENABLE.setChecked(False)
        self.CH3_ENABLE.setObjectName(_fromUtf8("CH3_ENABLE"))
        self.CH2_LABEL_2 = QtGui.QLabel(self.frame_11)
        self.CH2_LABEL_2.setGeometry(QtCore.QRect(20, 90, 101, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.CH2_LABEL_2.setFont(font)
        self.CH2_LABEL_2.setObjectName(_fromUtf8("CH2_LABEL_2"))
        self.MIC_ENABLE = QtGui.QCheckBox(self.frame_11)
        self.MIC_ENABLE.setGeometry(QtCore.QRect(130, 90, 21, 20))
        self.MIC_ENABLE.setText(_fromUtf8(""))
        self.MIC_ENABLE.setChecked(False)
        self.MIC_ENABLE.setObjectName(_fromUtf8("MIC_ENABLE"))
        self.CH2_LABEL_3 = QtGui.QLabel(self.frame_11)
        self.CH2_LABEL_3.setGeometry(QtCore.QRect(150, 90, 131, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.CH2_LABEL_3.setFont(font)
        self.CH2_LABEL_3.setObjectName(_fromUtf8("CH2_LABEL_3"))
        self.CH2_LABEL_4 = QtGui.QLabel(self.frame_11)
        self.CH2_LABEL_4.setGeometry(QtCore.QRect(230, 50, 51, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.CH2_LABEL_4.setFont(font)
        self.CH2_LABEL_4.setObjectName(_fromUtf8("CH2_LABEL_4"))
        self.comboBox_7 = QtGui.QComboBox(self.frame_11)
        self.comboBox_7.setGeometry(QtCore.QRect(130, 50, 91, 21))
        self.comboBox_7.setObjectName(_fromUtf8("comboBox_7"))
        self.comboBox_7.addItem(_fromUtf8(""))
        self.comboBox_7.addItem(_fromUtf8(""))
        self.comboBox_7.addItem(_fromUtf8(""))
        self.comboBox_7.addItem(_fromUtf8(""))
        self.comboBox_7.addItem(_fromUtf8(""))
        self.comboBox_7.addItem(_fromUtf8(""))
        self.comboBox_7.addItem(_fromUtf8(""))
        self.comboBox_7.addItem(_fromUtf8(""))
        self.verticalLayout_2.addWidget(self.frame_11)
        self.frame_2 = QtGui.QFrame(self.frame_4)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 40))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 71))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.label_49 = QtGui.QLabel(self.frame_2)
        self.label_49.setGeometry(QtCore.QRect(10, 0, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_49.setFont(font)
        self.label_49.setObjectName(_fromUtf8("label_49"))
        self.horizontalSlider = QtGui.QSlider(self.frame_2)
        self.horizontalSlider.setGeometry(QtCore.QRect(120, 0, 171, 29))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalSlider.sizePolicy().hasHeightForWidth())
        self.horizontalSlider.setSizePolicy(sizePolicy)
        self.horizontalSlider.setMaximum(9)
        self.horizontalSlider.setPageStep(1)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setTickPosition(QtGui.QSlider.TicksBelow)
        self.horizontalSlider.setObjectName(_fromUtf8("horizontalSlider"))
        self.verticalLayout_2.addWidget(self.frame_2)
        self.frame = QtGui.QFrame(self.frame_4)
        self.frame.setMinimumSize(QtCore.QSize(0, 75))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 83))
        self.frame.setStyleSheet(_fromUtf8("QFrame{background-color: rgba(255, 0, 0, 50);}"))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.dial_11 = QtGui.QDial(self.frame)
        self.dial_11.setGeometry(QtCore.QRect(190, 10, 91, 71))
        self.dial_11.setMinimum(0)
        self.dial_11.setMaximum(1000)
        self.dial_11.setProperty("value", 500)
        self.dial_11.setNotchTarget(10.0)
        self.dial_11.setNotchesVisible(True)
        self.dial_11.setObjectName(_fromUtf8("dial_11"))
        self.trigger_level_box = QtGui.QDoubleSpinBox(self.frame)
        self.trigger_level_box.setGeometry(QtCore.QRect(10, 50, 161, 21))
        self.trigger_level_box.setReadOnly(True)
        self.trigger_level_box.setMinimum(-20.0)
        self.trigger_level_box.setMaximum(20.0)
        self.trigger_level_box.setObjectName(_fromUtf8("trigger_level_box"))
        self.trigger_select_box = QtGui.QComboBox(self.frame)
        self.trigger_select_box.setGeometry(QtCore.QRect(100, 30, 71, 21))
        self.trigger_select_box.setStyleSheet(_fromUtf8(""))
        self.trigger_select_box.setFrame(False)
        self.trigger_select_box.setObjectName(_fromUtf8("trigger_select_box"))
        self.trigger_select_box.addItem(_fromUtf8(""))
        self.trigger_select_box.addItem(_fromUtf8(""))
        self.trigger_select_box.addItem(_fromUtf8(""))
        self.trigger_select_box.addItem(_fromUtf8(""))
        self.triggerBox = QtGui.QCheckBox(self.frame)
        self.triggerBox.setGeometry(QtCore.QRect(0, 1, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.triggerBox.setFont(font)
        self.triggerBox.setChecked(True)
        self.triggerBox.setObjectName(_fromUtf8("triggerBox"))
        self.highresBox = QtGui.QCheckBox(self.frame)
        self.highresBox.setGeometry(QtCore.QRect(280, 0, 20, 22))
        self.highresBox.setMaximumSize(QtCore.QSize(20, 16777215))
        self.highresBox.setText(_fromUtf8(""))
        self.highresBox.setObjectName(_fromUtf8("highresBox"))
        self.label_4 = QtGui.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(10, 30, 91, 17))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_2.addWidget(self.frame)
        self.label_2 = QtGui.QLabel(self.frame_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setMargin(5)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_2.addWidget(self.label_2)
        self.frame_6 = QtGui.QFrame(self.frame_4)
        self.frame_6.setMinimumSize(QtCore.QSize(0, 70))
        self.frame_6.setMaximumSize(QtCore.QSize(16777215, 65))
        self.frame_6.setStyleSheet(_fromUtf8(""))
        self.frame_6.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_6.setObjectName(_fromUtf8("frame_6"))
        self.fit_select_box = QtGui.QComboBox(self.frame_6)
        self.fit_select_box.setGeometry(QtCore.QRect(85, 5, 66, 21))
        self.fit_select_box.setObjectName(_fromUtf8("fit_select_box"))
        self.fit_select_box.addItem(_fromUtf8(""))
        self.fit_select_box.addItem(_fromUtf8(""))
        self.fit_select_box.addItem(_fromUtf8(""))
        self.fit_select_box.addItem(_fromUtf8(""))
        self.fit_select_box.addItem(_fromUtf8(""))
        self.overlay_fit_button = QtGui.QCheckBox(self.frame_6)
        self.overlay_fit_button.setGeometry(QtCore.QRect(215, 5, 76, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.overlay_fit_button.setFont(font)
        self.overlay_fit_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.overlay_fit_button.setAutoFillBackground(False)
        self.overlay_fit_button.setIconSize(QtCore.QSize(0, 0))
        self.overlay_fit_button.setObjectName(_fromUtf8("overlay_fit_button"))
        self.fit_select_box_2 = QtGui.QComboBox(self.frame_6)
        self.fit_select_box_2.setGeometry(QtCore.QRect(150, 5, 66, 21))
        self.fit_select_box_2.setObjectName(_fromUtf8("fit_select_box_2"))
        self.fit_select_box_2.addItem(_fromUtf8(""))
        self.fit_select_box_2.addItem(_fromUtf8(""))
        self.fit_select_box_2.addItem(_fromUtf8(""))
        self.fit_select_box_2.addItem(_fromUtf8(""))
        self.fit_select_box_2.addItem(_fromUtf8(""))
        self.fit_type_box = QtGui.QComboBox(self.frame_6)
        self.fit_type_box.setGeometry(QtCore.QRect(0, 5, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.fit_type_box.setFont(font)
        self.fit_type_box.setFrame(False)
        self.fit_type_box.setObjectName(_fromUtf8("fit_type_box"))
        self.fit_type_box.addItem(_fromUtf8(""))
        self.fit_type_box.addItem(_fromUtf8(""))
        self.fourierMode = QtGui.QCheckBox(self.frame_6)
        self.fourierMode.setGeometry(QtCore.QRect(10, 40, 161, 21))
        self.fourierMode.setObjectName(_fromUtf8("fourierMode"))
        self.verticalLayout_2.addWidget(self.frame_6)
        self.frame_3 = QtGui.QFrame(self.frame_4)
        self.frame_3.setMinimumSize(QtCore.QSize(0, 65))
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 65))
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.label = QtGui.QLabel(self.frame_3)
        self.label.setGeometry(QtCore.QRect(10, 6, 71, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton = QtGui.QPushButton(self.frame_3)
        self.pushButton.setGeometry(QtCore.QRect(180, 30, 101, 31))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.Liss_show = QtGui.QCheckBox(self.frame_3)
        self.Liss_show.setGeometry(QtCore.QRect(100, 0, 181, 31))
        self.Liss_show.setObjectName(_fromUtf8("Liss_show"))
        self.Liss_x = QtGui.QComboBox(self.frame_3)
        self.Liss_x.setGeometry(QtCore.QRect(10, 30, 71, 31))
        self.Liss_x.setObjectName(_fromUtf8("Liss_x"))
        self.Liss_x.addItem(_fromUtf8(""))
        self.Liss_x.addItem(_fromUtf8(""))
        self.Liss_x.addItem(_fromUtf8(""))
        self.Liss_x.addItem(_fromUtf8(""))
        self.Liss_y = QtGui.QComboBox(self.frame_3)
        self.Liss_y.setGeometry(QtCore.QRect(90, 30, 71, 31))
        self.Liss_y.setObjectName(_fromUtf8("Liss_y"))
        self.Liss_y.addItem(_fromUtf8(""))
        self.Liss_y.addItem(_fromUtf8(""))
        self.Liss_y.addItem(_fromUtf8(""))
        self.Liss_y.addItem(_fromUtf8(""))
        self.verticalLayout_2.addWidget(self.frame_3)
        spacerItem1 = QtGui.QSpacerItem(20, 1, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(2, 1)
        self.verticalLayout_2.setStretch(3, 2)
        self.verticalLayout_2.setStretch(4, 1)
        self.verticalLayout_2.setStretch(5, 1)
        self.verticalLayout_2.setStretch(6, 1)
        self.verticalLayout_2.setStretch(7, 1)
        self.verticalLayout_2.setStretch(8, 2)
        self.verticalLayout_3.addWidget(self.splitter)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.frame_9 = QtGui.QFrame(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy)
        self.frame_9.setMinimumSize(QtCore.QSize(0, 17))
        self.frame_9.setMaximumSize(QtCore.QSize(16777215, 34))
        self.frame_9.setBaseSize(QtCore.QSize(0, 0))
        self.frame_9.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_9.setObjectName(_fromUtf8("frame_9"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame_9)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.message_label = QtGui.QLabel(self.frame_9)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.message_label.sizePolicy().hasHeightForWidth())
        self.message_label.setSizePolicy(sizePolicy)
        self.message_label.setBaseSize(QtCore.QSize(0, 17))
        self.message_label.setStyleSheet(_fromUtf8(""))
        self.message_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.message_label.setWordWrap(False)
        self.message_label.setObjectName(_fromUtf8("message_label"))
        self.horizontalLayout.addWidget(self.message_label)
        self.coord_label = QtGui.QLabel(self.frame_9)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.coord_label.sizePolicy().hasHeightForWidth())
        self.coord_label.setSizePolicy(sizePolicy)
        self.coord_label.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.coord_label.setFont(font)
        self.coord_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.coord_label.setObjectName(_fromUtf8("coord_label"))
        self.horizontalLayout.addWidget(self.coord_label)
        self.freezeButton = QtGui.QCheckBox(self.frame_9)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.freezeButton.sizePolicy().hasHeightForWidth())
        self.freezeButton.setSizePolicy(sizePolicy)
        self.freezeButton.setMaximumSize(QtCore.QSize(100, 10))
        self.freezeButton.setObjectName(_fromUtf8("freezeButton"))
        self.horizontalLayout.addWidget(self.freezeButton)
        self.verticalLayout.addWidget(self.frame_9)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 868, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.actionSave_as = QtGui.QAction(MainWindow)
        self.actionSave_as.setObjectName(_fromUtf8("actionSave_as"))

        self.retranslateUi(MainWindow)
        self.fit_select_box.setCurrentIndex(4)
        self.fit_select_box_2.setCurrentIndex(4)
        self.fit_type_box.setCurrentIndex(0)
        self.Liss_y.setCurrentIndex(1)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.plot_liss)
        QtCore.QObject.connect(self.dial_11, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), MainWindow.setTriggerLevel)
        QtCore.QObject.connect(self.trigger_select_box, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(int)")), MainWindow.setTriggerChannel)
        QtCore.QObject.connect(self.comboBox_6, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(int)")), MainWindow.setGainCH1)
        QtCore.QObject.connect(self.CH1_REMAPS, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(QString)")), MainWindow.remap_CH0)
        QtCore.QObject.connect(self.horizontalSlider, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), MainWindow.setTimeBase)
        QtCore.QObject.connect(self.Liss_show, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), MainWindow.enableXY)
        QtCore.QObject.connect(self.comboBox_7, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(int)")), MainWindow.setGainCH2)
        QtCore.QObject.connect(self.fourierMode, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), MainWindow.setFourier)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Oscilloscope", None))
        self.centralwidget.setProperty("class", _translate("MainWindow", "PeripheralCollection", None))
        self.frame_4.setProperty("class", _translate("MainWindow", "PeripheralCollection", None))
        self.label_3.setText(_translate("MainWindow", "Channel Parameters", None))
        self.frame_11.setProperty("class", _translate("MainWindow", "PeripheralCollectionInner", None))
        self.CH1_LABEL.setText(_translate("MainWindow", "Chan 1", None))
        self.CH2_LABEL.setText(_translate("MainWindow", "Chan 2", None))
        self.comboBox_6.setItemText(0, _translate("MainWindow", "+/-16V", None))
        self.comboBox_6.setItemText(1, _translate("MainWindow", "+/-8V", None))
        self.comboBox_6.setItemText(2, _translate("MainWindow", "+/-4V", None))
        self.comboBox_6.setItemText(3, _translate("MainWindow", "+/-3V", None))
        self.comboBox_6.setItemText(4, _translate("MainWindow", "+/-2V", None))
        self.comboBox_6.setItemText(5, _translate("MainWindow", "+/-1.5V", None))
        self.comboBox_6.setItemText(6, _translate("MainWindow", "+/-1V", None))
        self.comboBox_6.setItemText(7, _translate("MainWindow", "+/-500mV", None))
        self.label_30.setText(_translate("MainWindow", "Range", None))
        self.label_31.setText(_translate("MainWindow", "Range", None))
        self.CH2_LABEL_2.setText(_translate("MainWindow", "CH3(+/-3.3V)", None))
        self.CH2_LABEL_3.setText(_translate("MainWindow", "CH4(MICrophone)", None))
        self.CH2_LABEL_4.setText(_translate("MainWindow", "CH2", None))
        self.comboBox_7.setItemText(0, _translate("MainWindow", "+/-16V", None))
        self.comboBox_7.setItemText(1, _translate("MainWindow", "+/-8V", None))
        self.comboBox_7.setItemText(2, _translate("MainWindow", "+/-4V", None))
        self.comboBox_7.setItemText(3, _translate("MainWindow", "+/-3V", None))
        self.comboBox_7.setItemText(4, _translate("MainWindow", "+/-2V", None))
        self.comboBox_7.setItemText(5, _translate("MainWindow", "+/-1.5V", None))
        self.comboBox_7.setItemText(6, _translate("MainWindow", "+/-1V", None))
        self.comboBox_7.setItemText(7, _translate("MainWindow", "+/-500mV", None))
        self.frame_2.setProperty("class", _translate("MainWindow", "PeripheralCollectionInner", None))
        self.label_49.setText(_translate("MainWindow", "TIME(mS/Div)", None))
        self.frame.setProperty("class", _translate("MainWindow", "PeripheralCollectionInner", None))
        self.dial_11.setToolTip(_translate("MainWindow", "Scroll to change trigger level", None))
        self.trigger_level_box.setSuffix(_translate("MainWindow", " V", None))
        self.trigger_select_box.setItemText(0, _translate("MainWindow", "CH1", None))
        self.trigger_select_box.setItemText(1, _translate("MainWindow", "CH2", None))
        self.trigger_select_box.setItemText(2, _translate("MainWindow", "CH3", None))
        self.trigger_select_box.setItemText(3, _translate("MainWindow", "MIC", None))
        self.triggerBox.setText(_translate("MainWindow", "TRIGGER", None))
        self.label_4.setText(_translate("MainWindow", "Channel", None))
        self.label_2.setText(_translate("MainWindow", "Data Analysis", None))
        self.frame_6.setProperty("class", _translate("MainWindow", "PeripheralCollectionInner", None))
        self.fit_select_box.setItemText(0, _translate("MainWindow", "CH1", None))
        self.fit_select_box.setItemText(1, _translate("MainWindow", "CH2", None))
        self.fit_select_box.setItemText(2, _translate("MainWindow", "CH3", None))
        self.fit_select_box.setItemText(3, _translate("MainWindow", "MIC", None))
        self.fit_select_box.setItemText(4, _translate("MainWindow", "None", None))
        self.overlay_fit_button.setText(_translate("MainWindow", "Overlay", None))
        self.fit_select_box_2.setItemText(0, _translate("MainWindow", "CH1", None))
        self.fit_select_box_2.setItemText(1, _translate("MainWindow", "CH2", None))
        self.fit_select_box_2.setItemText(2, _translate("MainWindow", "CH3", None))
        self.fit_select_box_2.setItemText(3, _translate("MainWindow", "MIC", None))
        self.fit_select_box_2.setItemText(4, _translate("MainWindow", "None", None))
        self.fit_type_box.setItemText(0, _translate("MainWindow", "SINE FIT", None))
        self.fit_type_box.setItemText(1, _translate("MainWindow", "SQUARE FIT", None))
        self.fourierMode.setText(_translate("MainWindow", "Fourier Transform", None))
        self.frame_3.setProperty("class", _translate("MainWindow", "PeripheralCollectionInner", None))
        self.label.setText(_translate("MainWindow", "X-Y Mode", None))
        self.pushButton.setText(_translate("MainWindow", "View", None))
        self.Liss_show.setText(_translate("MainWindow", "Enable XY plot", None))
        self.Liss_x.setItemText(0, _translate("MainWindow", "CH1", None))
        self.Liss_x.setItemText(1, _translate("MainWindow", "CH2", None))
        self.Liss_x.setItemText(2, _translate("MainWindow", "CH3", None))
        self.Liss_x.setItemText(3, _translate("MainWindow", "MIC", None))
        self.Liss_y.setItemText(0, _translate("MainWindow", "CH1", None))
        self.Liss_y.setItemText(1, _translate("MainWindow", "CH2", None))
        self.Liss_y.setItemText(2, _translate("MainWindow", "CH3", None))
        self.Liss_y.setItemText(3, _translate("MainWindow", "MIC", None))
        self.message_label.setText(_translate("MainWindow", "Msg:", None))
        self.coord_label.setText(_translate("MainWindow", ".", None))
        self.freezeButton.setText(_translate("MainWindow", "FREEZE", None))
        self.actionSave_as.setText(_translate("MainWindow", "Save as", None))


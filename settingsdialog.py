# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settingsdialog.ui'
#
# Created: Mon May 13 19:24:11 2013
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_SettingsDialogBaseClass(object):
    def setupUi(self, SettingsDialogBaseClass):
        SettingsDialogBaseClass.setObjectName(_fromUtf8("SettingsDialogBaseClass"))
        SettingsDialogBaseClass.resize(742, 452)
        SettingsDialogBaseClass.setWindowTitle(QtGui.QApplication.translate("SettingsDialogBaseClass", "3DLP Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.horizontalLayout_21 = QtGui.QHBoxLayout(SettingsDialogBaseClass)
        self.horizontalLayout_21.setObjectName(_fromUtf8("horizontalLayout_21"))
        self.verticalLayout_11 = QtGui.QVBoxLayout()
        self.verticalLayout_11.setObjectName(_fromUtf8("verticalLayout_11"))
        self.horizontalLayout_19 = QtGui.QHBoxLayout()
        self.horizontalLayout_19.setObjectName(_fromUtf8("horizontalLayout_19"))
        self.verticalLayout_9 = QtGui.QVBoxLayout()
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.horizontalLayout_18 = QtGui.QHBoxLayout()
        self.horizontalLayout_18.setObjectName(_fromUtf8("horizontalLayout_18"))
        self.groupBox_2 = QtGui.QGroupBox(SettingsDialogBaseClass)
        self.groupBox_2.setTitle(QtGui.QApplication.translate("SettingsDialogBaseClass", "Printing Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.horizontalLayout_17 = QtGui.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_17.setObjectName(_fromUtf8("horizontalLayout_17"))
        self.horizontalLayout_16 = QtGui.QHBoxLayout()
        self.horizontalLayout_16.setObjectName(_fromUtf8("horizontalLayout_16"))
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.enableprintercontrol = QtGui.QCheckBox(self.groupBox_2)
        self.enableprintercontrol.setText(QtGui.QApplication.translate("SettingsDialogBaseClass", "Enable Printer Control?", None, QtGui.QApplication.UnicodeUTF8))
        self.enableprintercontrol.setChecked(False)
        self.enableprintercontrol.setObjectName(_fromUtf8("enableprintercontrol"))
        self.verticalLayout_8.addWidget(self.enableprintercontrol)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.radio_arduinoUno = QtGui.QRadioButton(self.groupBox_2)
        self.radio_arduinoUno.setText(QtGui.QApplication.translate("SettingsDialogBaseClass", "Arduino Uno", None, QtGui.QApplication.UnicodeUTF8))
        self.radio_arduinoUno.setChecked(True)
        self.radio_arduinoUno.setObjectName(_fromUtf8("radio_arduinoUno"))
        self.horizontalLayout_4.addWidget(self.radio_arduinoUno)
        self.radio_arduinoMega = QtGui.QRadioButton(self.groupBox_2)
        self.radio_arduinoMega.setText(QtGui.QApplication.translate("SettingsDialogBaseClass", "Arduino Mega", None, QtGui.QApplication.UnicodeUTF8))
        self.radio_arduinoMega.setObjectName(_fromUtf8("radio_arduinoMega"))
        self.horizontalLayout_4.addWidget(self.radio_arduinoMega)
        self.radio_pyMCU = QtGui.QRadioButton(self.groupBox_2)
        self.radio_pyMCU.setText(QtGui.QApplication.translate("SettingsDialogBaseClass", "PyMCU", None, QtGui.QApplication.UnicodeUTF8))
        self.radio_pyMCU.setObjectName(_fromUtf8("radio_pyMCU"))
        self.horizontalLayout_4.addWidget(self.radio_pyMCU)
        self.radio_ramps = QtGui.QRadioButton(self.groupBox_2)
        self.radio_ramps.setText(QtGui.QApplication.translate("SettingsDialogBaseClass", "RAMPS", None, QtGui.QApplication.UnicodeUTF8))
        self.radio_ramps.setObjectName(_fromUtf8("radio_ramps"))
        self.horizontalLayout_4.addWidget(self.radio_ramps)
        self.verticalLayout_8.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_29 = QtGui.QLabel(self.groupBox_2)
        self.label_29.setText(QtGui.QApplication.translate("SettingsDialogBaseClass", "Port:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_29.setObjectName(_fromUtf8("label_29"))
        self.horizontalLayout_3.addWidget(self.label_29)
        self.pickcom = QtGui.QComboBox(self.groupBox_2)
        self.pickcom.setObjectName(_fromUtf8("pickcom"))
        self.horizontalLayout_3.addWidget(self.pickcom)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout_8.addLayout(self.horizontalLayout_3)
        self.enableslideshow = QtGui.QCheckBox(self.groupBox_2)
        self.enableslideshow.setText(QtGui.QApplication.translate("SettingsDialogBaseClass", "Enable Slideshow?", None, QtGui.QApplication.UnicodeUTF8))
        self.enableslideshow.setObjectName(_fromUtf8("enableslideshow"))
        self.verticalLayout_8.addWidget(self.enableslideshow)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.label_25 = QtGui.QLabel(self.groupBox_2)
        self.label_25.setText(QtGui.QApplication.translate("SettingsDialogBaseClass", "Choose monitor to print on:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.horizontalLayout_10.addWidget(self.label_25)
        self.pickscreen = QtGui.QComboBox(self.groupBox_2)
        self.pickscreen.setObjectName(_fromUtf8("pickscreen"))
        self.horizontalLayout_10.addWidget(self.pickscreen)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem1)
        self.verticalLayout_8.addLayout(self.horizontalLayout_10)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem2)
        self.horizontalLayout_16.addLayout(self.verticalLayout_8)
        self.horizontalLayout_17.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_18.addWidget(self.groupBox_2)
        self.groupBox_4 = QtGui.QGroupBox(SettingsDialogBaseClass)
        self.groupBox_4.setTitle(QtGui.QApplication.translate("SettingsDialogBaseClass", "Stepping Mode", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.horizontalLayout_13 = QtGui.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.radioButton = QtGui.QRadioButton(self.groupBox_4)
        self.radioButton.setText(QtGui.QApplication.translate("SettingsDialogBaseClass", "Full Stepping", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.verticalLayout_3.addWidget(self.radioButton)
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox_4)
        self.radioButton_2.setText(QtGui.QApplication.translate("SettingsDialogBaseClass", "1/2 Microstepping", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.verticalLayout_3.addWidget(self.radioButton_2)
        self.radioButton_3 = QtGui.QRadioButton(self.groupBox_4)
        self.radioButton_3.setText(QtGui.QApplication.translate("SettingsDialogBaseClass", "1/4 Microstepping", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_3.setObjectName(_fromUtf8("radioButton_3"))
        self.verticalLayout_3.addWidget(self.radioButton_3)
        self.radioButton_4 = QtGui.QRadioButton(self.groupBox_4)
        self.radioButton_4.setText(QtGui.QApplication.translate("SettingsDialogBaseClass", "1/8 Microstepping", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_4.setObjectName(_fromUtf8("radioButton_4"))
        self.verticalLayout_3.addWidget(self.radioButton_4)
        self.radioButton_5 = QtGui.QRadioButton(self.groupBox_4)
        self.radioButton_5.setText(QtGui.QApplication.translate("SettingsDialogBaseClass", "1/16 Microstepping", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_5.setObjectName(_fromUtf8("radioButton_5"))
        self.verticalLayout_3.addWidget(self.radioButton_5)
        self.horizontalLayout_13.addLayout(self.verticalLayout_3)
        self.horizontalLayout_18.addWidget(self.groupBox_4)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem3)
        self.verticalLayout_9.addLayout(self.horizontalLayout_18)
        self.groupBox_5 = QtGui.QGroupBox(SettingsDialogBaseClass)
        self.groupBox_5.setTitle(QtGui.QApplication.translate("SettingsDialogBaseClass", "Layer Advance Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.horizontalLayout_15 = QtGui.QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_15.setObjectName(_fromUtf8("horizontalLayout_15"))
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.horizontalLayout_14 = QtGui.QHBoxLayout()
        self.horizontalLayout_14.setObjectName(_fromUtf8("horizontalLayout_14"))
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem4)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.label_26 = QtGui.QLabel(self.groupBox_5)
        self.label_26.setText(QtGui.QApplication.translate("SettingsDialogBaseClass", "Number of starting layers", None, QtGui.QApplication.UnicodeUTF8))
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.horizontalLayout_8.addWidget(self.label_26)
        self.starting_layers = QtGui.QLineEdit(self.groupBox_5)
        self.starting_layers.setText(_fromUtf8(""))
        self.starting_layers.setObjectName(_fromUtf8("starting_layers"))
        self.horizontalLayout_8.addWidget(self.starting_layers)
        self.horizontalLayout_14.addLayout(self.horizontalLayout_8)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem5)
        self.verticalLayout_7.addLayout(self.horizontalLayout_14)
        self.line_2 = QtGui.QFrame(self.groupBox_5)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.verticalLayout_7.addWidget(self.line_2)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.groupBox_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setText(QtGui.QApplication.translate("SettingsDialogBaseClass", "Starting Layers", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.label_27 = QtGui.QLabel(self.groupBox_5)
        self.label_27.setText(QtGui.QApplication.translate("SettingsDialogBaseClass", "Starting layer exposure ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.horizontalLayout_9.addWidget(self.label_27)
        self.starting_layer_exposure = QtGui.QLineEdit(self.groupBox_5)
        self.starting_layer_exposure.setText(_fromUtf8(""))
        self.starting_layer_exposure.setObjectName(_fromUtf8("starting_layer_exposure"))
        self.horizontalLayout_9.addWidget(self.starting_layer_exposure)
        self.label_30 = QtGui.QLabel(self.groupBox_5)
        self.label_30.setText(QtGui.QApplication.translate("SettingsDialogBaseClass", "s", None, QtGui.QApplication.UnicodeUTF8))
        self.label_30.setObjectName(_fromUtf8("label_30"))
        self.horizontalLayout_9.addWidget(self.label_30)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.groupBox_6 = QtGui.QGroupBox(self.groupBox_5)
        self.groupBox_6.setMinimumSize(QtCore.QSize(0, 80))
        self.groupBox_6.setTitle(QtGui.QApplication.translate("SettingsDialogBaseClass", "Inter-layer scripting", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.horizontalLayout_12 = QtGui.QHBoxLayout(self.groupBox_6)
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.zscript_2 = QtGui.QPlainTextEdit(self.groupBox_6)
        self.zscript_2.setObjectName(_fromUtf8("zscript_2"))
        self.horizontalLayout_12.addWidget(self.zscript_2)
        self.verticalLayout.addWidget(self.groupBox_6)
        self.horizontalLayout_5.addLayout(self.verticalLayout)
        self.line = QtGui.QFrame(self.groupBox_5)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.horizontalLayout_5.addWidget(self.line)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.label_2 = QtGui.QLabel(self.groupBox_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setText(QtGui.QApplication.translate("SettingsDialogBaseClass", "Normal Layers", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_4.addWidget(self.label_2)
        self.horizontalLayout_20 = QtGui.QHBoxLayout()
        self.horizontalLayout_20.setObjectName(_fromUtf8("horizontalLayout_20"))
        self.label_6 = QtGui.QLabel(self.groupBox_5)
        self.label_6.setText(QtGui.QApplication.translate("SettingsDialogBaseClass", "Exposure Time", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_20.addWidget(self.label_6)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.exposure_time = QtGui.QLineEdit(self.groupBox_5)
        self.exposure_time.setText(_fromUtf8(""))
        self.exposure_time.setObjectName(_fromUtf8("exposure_time"))
        self.horizontalLayout_6.addWidget(self.exposure_time)
        self.label_28 = QtGui.QLabel(self.groupBox_5)
        self.label_28.setText(QtGui.QApplication.translate("SettingsDialogBaseClass", "s", None, QtGui.QApplication.UnicodeUTF8))
        self.label_28.setObjectName(_fromUtf8("label_28"))
        self.horizontalLayout_6.addWidget(self.label_28)
        self.horizontalLayout_20.addLayout(self.horizontalLayout_6)
        self.verticalLayout_4.addLayout(self.horizontalLayout_20)
        self.groupBox = QtGui.QGroupBox(self.groupBox_5)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 80))
        self.groupBox.setTitle(QtGui.QApplication.translate("SettingsDialogBaseClass", "Inter-layer scripting", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.zscript = QtGui.QPlainTextEdit(self.groupBox)
        self.zscript.setObjectName(_fromUtf8("zscript"))
        self.horizontalLayout_7.addWidget(self.zscript)
        self.verticalLayout_4.addWidget(self.groupBox)
        self.horizontalLayout_5.addLayout(self.verticalLayout_4)
        self.verticalLayout_7.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_15.addLayout(self.verticalLayout_7)
        self.verticalLayout_9.addWidget(self.groupBox_5)
        self.horizontalLayout_19.addLayout(self.verticalLayout_9)
        self.verticalLayout_10 = QtGui.QVBoxLayout()
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.groupBox_3 = QtGui.QGroupBox(SettingsDialogBaseClass)
        self.groupBox_3.setTitle(QtGui.QApplication.translate("SettingsDialogBaseClass", "Projector Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.projectorcontrol = QtGui.QCheckBox(self.groupBox_3)
        self.projectorcontrol.setText(QtGui.QApplication.translate("SettingsDialogBaseClass", "Enable Projector Control?", None, QtGui.QApplication.UnicodeUTF8))
        self.projectorcontrol.setChecked(False)
        self.projectorcontrol.setObjectName(_fromUtf8("projectorcontrol"))
        self.verticalLayout_6.addWidget(self.projectorcontrol)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.verticalLayout_14 = QtGui.QVBoxLayout()
        self.verticalLayout_14.setObjectName(_fromUtf8("verticalLayout_14"))
        self.label_17 = QtGui.QLabel(self.groupBox_3)
        self.label_17.setText(QtGui.QApplication.translate("SettingsDialogBaseClass", "Serial Baud rate:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.verticalLayout_14.addWidget(self.label_17)
        self.projector_baud = QtGui.QComboBox(self.groupBox_3)
        self.projector_baud.setObjectName(_fromUtf8("projector_baud"))
        self.projector_baud.addItem(_fromUtf8(""))
        self.projector_baud.setItemText(0, QtGui.QApplication.translate("SettingsDialogBaseClass", "19200", None, QtGui.QApplication.UnicodeUTF8))
        self.projector_baud.addItem(_fromUtf8(""))
        self.projector_baud.setItemText(1, QtGui.QApplication.translate("SettingsDialogBaseClass", "115200", None, QtGui.QApplication.UnicodeUTF8))
        self.projector_baud.addItem(_fromUtf8(""))
        self.projector_baud.setItemText(2, QtGui.QApplication.translate("SettingsDialogBaseClass", "57600", None, QtGui.QApplication.UnicodeUTF8))
        self.projector_baud.addItem(_fromUtf8(""))
        self.projector_baud.setItemText(3, QtGui.QApplication.translate("SettingsDialogBaseClass", "38400", None, QtGui.QApplication.UnicodeUTF8))
        self.projector_baud.addItem(_fromUtf8(""))
        self.projector_baud.setItemText(4, QtGui.QApplication.translate("SettingsDialogBaseClass", "9600", None, QtGui.QApplication.UnicodeUTF8))
        self.projector_baud.addItem(_fromUtf8(""))
        self.projector_baud.setItemText(5, QtGui.QApplication.translate("SettingsDialogBaseClass", "4800", None, QtGui.QApplication.UnicodeUTF8))
        self.projector_baud.addItem(_fromUtf8(""))
        self.projector_baud.setItemText(6, QtGui.QApplication.translate("SettingsDialogBaseClass", "2400", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalLayout_14.addWidget(self.projector_baud)
        self.horizontalLayout_11.addLayout(self.verticalLayout_14)
        self.verticalLayout_6.addLayout(self.horizontalLayout_11)
        self.verticalLayout_18 = QtGui.QVBoxLayout()
        self.verticalLayout_18.setObjectName(_fromUtf8("verticalLayout_18"))
        self.label_21 = QtGui.QLabel(self.groupBox_3)
        self.label_21.setText(QtGui.QApplication.translate("SettingsDialogBaseClass", "Power Off Command:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.verticalLayout_18.addWidget(self.label_21)
        self.projector_poweroffcommand = QtGui.QLineEdit(self.groupBox_3)
        self.projector_poweroffcommand.setMinimumSize(QtCore.QSize(200, 0))
        self.projector_poweroffcommand.setText(_fromUtf8(""))
        self.projector_poweroffcommand.setObjectName(_fromUtf8("projector_poweroffcommand"))
        self.verticalLayout_18.addWidget(self.projector_poweroffcommand)
        self.verticalLayout_6.addLayout(self.verticalLayout_18)
        self.horizontalLayout.addLayout(self.verticalLayout_6)
        self.verticalLayout_2.addWidget(self.groupBox_3)
        self.verticalLayout_10.addLayout(self.verticalLayout_2)
        self.groupBox_7 = QtGui.QGroupBox(SettingsDialogBaseClass)
        self.groupBox_7.setTitle(QtGui.QApplication.translate("SettingsDialogBaseClass", "Hardware Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_7.setObjectName(_fromUtf8("groupBox_7"))
        self.horizontalLayout_24 = QtGui.QHBoxLayout(self.groupBox_7)
        self.horizontalLayout_24.setObjectName(_fromUtf8("horizontalLayout_24"))
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.horizontalLayout_22 = QtGui.QHBoxLayout()
        self.horizontalLayout_22.setObjectName(_fromUtf8("horizontalLayout_22"))
        self.label_3 = QtGui.QLabel(self.groupBox_7)
        self.label_3.setText(QtGui.QApplication.translate("SettingsDialogBaseClass", "Z Axis Leadscrew Pitch", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_22.addWidget(self.label_3)
        self.pitch = QtGui.QLineEdit(self.groupBox_7)
        self.pitch.setObjectName(_fromUtf8("pitch"))
        self.horizontalLayout_22.addWidget(self.pitch)
        self.label_5 = QtGui.QLabel(self.groupBox_7)
        self.label_5.setText(QtGui.QApplication.translate("SettingsDialogBaseClass", "mm/rev", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_22.addWidget(self.label_5)
        self.verticalLayout_5.addLayout(self.horizontalLayout_22)
        self.horizontalLayout_23 = QtGui.QHBoxLayout()
        self.horizontalLayout_23.setObjectName(_fromUtf8("horizontalLayout_23"))
        self.label_4 = QtGui.QLabel(self.groupBox_7)
        self.label_4.setText(QtGui.QApplication.translate("SettingsDialogBaseClass", "Z Axis Steps/rev", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_23.addWidget(self.label_4)
        self.stepsPerRev = QtGui.QLineEdit(self.groupBox_7)
        self.stepsPerRev.setObjectName(_fromUtf8("stepsPerRev"))
        self.horizontalLayout_23.addWidget(self.stepsPerRev)
        self.label_7 = QtGui.QLabel(self.groupBox_7)
        self.label_7.setText(QtGui.QApplication.translate("SettingsDialogBaseClass", "steps", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_23.addWidget(self.label_7)
        self.verticalLayout_5.addLayout(self.horizontalLayout_23)
        self.horizontalLayout_24.addLayout(self.verticalLayout_5)
        self.verticalLayout_10.addWidget(self.groupBox_7)
        spacerItem6 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem6)
        self.horizontalLayout_19.addLayout(self.verticalLayout_10)
        self.verticalLayout_11.addLayout(self.horizontalLayout_19)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.pushButton = QtGui.QPushButton(SettingsDialogBaseClass)
        self.pushButton.setText(QtGui.QApplication.translate("SettingsDialogBaseClass", "Apply Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.pushButton_2 = QtGui.QPushButton(SettingsDialogBaseClass)
        self.pushButton_2.setText(QtGui.QApplication.translate("SettingsDialogBaseClass", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem8)
        self.verticalLayout_11.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_21.addLayout(self.verticalLayout_11)

        self.retranslateUi(SettingsDialogBaseClass)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), SettingsDialogBaseClass.reject)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), SettingsDialogBaseClass.ApplySettings)
        QtCore.QMetaObject.connectSlotsByName(SettingsDialogBaseClass)

    def retranslateUi(self, SettingsDialogBaseClass):
        pass


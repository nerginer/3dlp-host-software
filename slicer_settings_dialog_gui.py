# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'slicer_settings_dialog.ui'
#
# Created: Sun Mar 31 19:34:46 2013
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(219, 258)
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "3DLP Slicer Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(Dialog)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setText(QtGui.QApplication.translate("Dialog", "Slicing Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.label_7 = QtGui.QLabel(Dialog)
        self.label_7.setText(QtGui.QApplication.translate("Dialog", "Image Height", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout_8.addWidget(self.label_7)
        self.imageHeight = QtGui.QLineEdit(Dialog)
        self.imageHeight.setText(_fromUtf8(""))
        self.imageHeight.setObjectName(_fromUtf8("imageHeight"))
        self.verticalLayout_8.addWidget(self.imageHeight)
        self.horizontalLayout_12.addLayout(self.verticalLayout_8)
        self.verticalLayout_9 = QtGui.QVBoxLayout()
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.label_8 = QtGui.QLabel(Dialog)
        self.label_8.setText(QtGui.QApplication.translate("Dialog", "Image Width", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.verticalLayout_9.addWidget(self.label_8)
        self.imageWidth = QtGui.QLineEdit(Dialog)
        self.imageWidth.setText(_fromUtf8(""))
        self.imageWidth.setObjectName(_fromUtf8("imageWidth"))
        self.verticalLayout_9.addWidget(self.imageWidth)
        self.horizontalLayout_12.addLayout(self.verticalLayout_9)
        self.verticalLayout.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_13 = QtGui.QHBoxLayout()
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.verticalLayout_10 = QtGui.QVBoxLayout()
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.label_9 = QtGui.QLabel(Dialog)
        self.label_9.setText(QtGui.QApplication.translate("Dialog", "Layer Thickness", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.verticalLayout_10.addWidget(self.label_9)
        self.layerThickness = QtGui.QLineEdit(Dialog)
        self.layerThickness.setEnabled(False)
        self.layerThickness.setText(_fromUtf8(""))
        self.layerThickness.setObjectName(_fromUtf8("layerThickness"))
        self.verticalLayout_10.addWidget(self.layerThickness)
        self.horizontalLayout_13.addLayout(self.verticalLayout_10)
        self.verticalLayout_11 = QtGui.QVBoxLayout()
        self.verticalLayout_11.setObjectName(_fromUtf8("verticalLayout_11"))
        self.label_10 = QtGui.QLabel(Dialog)
        self.label_10.setText(QtGui.QApplication.translate("Dialog", "Slicing Plane", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.verticalLayout_11.addWidget(self.label_10)
        self.slicingPlane = QtGui.QComboBox(Dialog)
        self.slicingPlane.setObjectName(_fromUtf8("slicingPlane"))
        self.slicingPlane.addItem(_fromUtf8(""))
        self.slicingPlane.setItemText(0, QtGui.QApplication.translate("Dialog", "XZ", None, QtGui.QApplication.UnicodeUTF8))
        self.slicingPlane.addItem(_fromUtf8(""))
        self.slicingPlane.setItemText(1, QtGui.QApplication.translate("Dialog", "XY", None, QtGui.QApplication.UnicodeUTF8))
        self.slicingPlane.addItem(_fromUtf8(""))
        self.slicingPlane.setItemText(2, QtGui.QApplication.translate("Dialog", "YZ", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalLayout_11.addWidget(self.slicingPlane)
        self.horizontalLayout_13.addLayout(self.verticalLayout_11)
        self.verticalLayout.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_14 = QtGui.QHBoxLayout()
        self.horizontalLayout_14.setObjectName(_fromUtf8("horizontalLayout_14"))
        self.label_13 = QtGui.QLabel(Dialog)
        self.label_13.setText(QtGui.QApplication.translate("Dialog", "Starting Depth:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.horizontalLayout_14.addWidget(self.label_13)
        self.startingDepth = QtGui.QLineEdit(Dialog)
        self.startingDepth.setText(_fromUtf8(""))
        self.startingDepth.setObjectName(_fromUtf8("startingDepth"))
        self.horizontalLayout_14.addWidget(self.startingDepth)
        self.verticalLayout.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_15 = QtGui.QHBoxLayout()
        self.horizontalLayout_15.setObjectName(_fromUtf8("horizontalLayout_15"))
        self.label_22 = QtGui.QLabel(Dialog)
        self.label_22.setText(QtGui.QApplication.translate("Dialog", "Ending Depth:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.horizontalLayout_15.addWidget(self.label_22)
        self.endingDepth = QtGui.QLineEdit(Dialog)
        self.endingDepth.setText(_fromUtf8(""))
        self.endingDepth.setObjectName(_fromUtf8("endingDepth"))
        self.horizontalLayout_15.addWidget(self.endingDepth)
        self.verticalLayout.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_16 = QtGui.QHBoxLayout()
        self.horizontalLayout_16.setObjectName(_fromUtf8("horizontalLayout_16"))
        self.label_23 = QtGui.QLabel(Dialog)
        self.label_23.setText(QtGui.QApplication.translate("Dialog", "Z slicing increment:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.horizontalLayout_16.addWidget(self.label_23)
        self.slicingIncrement = QtGui.QLineEdit(Dialog)
        self.slicingIncrement.setMinimumSize(QtCore.QSize(100, 0))
        self.slicingIncrement.setText(_fromUtf8(""))
        self.slicingIncrement.setObjectName(_fromUtf8("slicingIncrement"))
        self.horizontalLayout_16.addWidget(self.slicingIncrement)
        self.verticalLayout.addLayout(self.horizontalLayout_16)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setText(QtGui.QApplication.translate("Dialog", "Apply Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtGui.QPushButton(Dialog)
        self.pushButton_2.setText(QtGui.QApplication.translate("Dialog", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.reject)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        pass


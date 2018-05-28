# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'maker_ui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Maker_Dialog(object):
    def setupUi(self, Maker_Dialog):
        Maker_Dialog.setObjectName("Maker_Dialog")
        Maker_Dialog.resize(1500, 900)
        Maker_Dialog.setSizeGripEnabled(True)
        self.directoryListWidget = QtWidgets.QListWidget(Maker_Dialog)
        self.directoryListWidget.setGeometry(QtCore.QRect(15, 75, 180, 750))
        self.directoryListWidget.setObjectName("directoryListWidget")
        self.contentListWidget = QtWidgets.QListWidget(Maker_Dialog)
        self.contentListWidget.setGeometry(QtCore.QRect(210, 75, 180, 750))
        self.contentListWidget.setObjectName("contentListWidget")
        self.directories_label = QtWidgets.QLabel(Maker_Dialog)
        self.directories_label.setGeometry(QtCore.QRect(45, 30, 120, 23))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.directories_label.setFont(font)
        self.directories_label.setAlignment(QtCore.Qt.AlignCenter)
        self.directories_label.setObjectName("directories_label")
        self.contents_label = QtWidgets.QLabel(Maker_Dialog)
        self.contents_label.setGeometry(QtCore.QRect(240, 30, 120, 23))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.contents_label.setFont(font)
        self.contents_label.setAlignment(QtCore.Qt.AlignCenter)
        self.contents_label.setObjectName("contents_label")
        self.inputImageScrollArea = QtWidgets.QScrollArea(Maker_Dialog)
        self.inputImageScrollArea.setGeometry(QtCore.QRect(450, 75, 600, 450))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inputImageScrollArea.sizePolicy().hasHeightForWidth())
        self.inputImageScrollArea.setSizePolicy(sizePolicy)
        self.inputImageScrollArea.setMaximumSize(QtCore.QSize(600, 450))
        self.inputImageScrollArea.setBaseSize(QtCore.QSize(0, 0))
        self.inputImageScrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.inputImageScrollArea.setWidgetResizable(True)
        self.inputImageScrollArea.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.inputImageScrollArea.setObjectName("inputImageScrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 598, 448))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.inputImageScrollArea.setWidget(self.scrollAreaWidgetContents)
        self.inputImageLabel = QtWidgets.QLabel(Maker_Dialog)
        self.inputImageLabel.setGeometry(QtCore.QRect(450, 75, 600, 450))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inputImageLabel.sizePolicy().hasHeightForWidth())
        self.inputImageLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.inputImageLabel.setFont(font)
        self.inputImageLabel.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.inputImageLabel.setMouseTracking(True)
        self.inputImageLabel.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.inputImageLabel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.inputImageLabel.setLineWidth(2)
        self.inputImageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.inputImageLabel.setIndent(0)
        self.inputImageLabel.setObjectName("inputImageLabel")
        self.inputImageTextLabel = QtWidgets.QLabel(Maker_Dialog)
        self.inputImageTextLabel.setGeometry(QtCore.QRect(650, 30, 200, 24))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.inputImageTextLabel.setFont(font)
        self.inputImageTextLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.inputImageTextLabel.setObjectName("inputImageTextLabel")
        self.rectXLabel = QtWidgets.QLabel(Maker_Dialog)
        self.rectXLabel.setGeometry(QtCore.QRect(1110, 135, 96, 23))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.rectXLabel.setFont(font)
        self.rectXLabel.setObjectName("rectXLabel")
        self.rectYLabel = QtWidgets.QLabel(Maker_Dialog)
        self.rectYLabel.setGeometry(QtCore.QRect(1110, 180, 96, 23))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.rectYLabel.setFont(font)
        self.rectYLabel.setObjectName("rectYLabel")
        self.rectWidthLabel = QtWidgets.QLabel(Maker_Dialog)
        self.rectWidthLabel.setGeometry(QtCore.QRect(1110, 225, 96, 23))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.rectWidthLabel.setFont(font)
        self.rectWidthLabel.setObjectName("rectWidthLabel")
        self.rectHeightLabel = QtWidgets.QLabel(Maker_Dialog)
        self.rectHeightLabel.setGeometry(QtCore.QRect(1110, 270, 96, 23))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.rectHeightLabel.setFont(font)
        self.rectHeightLabel.setObjectName("rectHeightLabel")
        self.imageSizeLabel = QtWidgets.QLabel(Maker_Dialog)
        self.imageSizeLabel.setGeometry(QtCore.QRect(600, 540, 300, 23))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.imageSizeLabel.setFont(font)
        self.imageSizeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.imageSizeLabel.setObjectName("imageSizeLabel")
        self.rectLabel = QtWidgets.QLabel(Maker_Dialog)
        self.rectLabel.setGeometry(QtCore.QRect(1080, 75, 225, 24))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.rectLabel.setFont(font)
        self.rectLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.rectLabel.setObjectName("rectLabel")
        self.silhouetteLabel = QtWidgets.QLabel(Maker_Dialog)
        self.silhouetteLabel.setGeometry(QtCore.QRect(450, 600, 300, 225))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.silhouetteLabel.setFont(font)
        self.silhouetteLabel.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.silhouetteLabel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.silhouetteLabel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.silhouetteLabel.setScaledContents(True)
        self.silhouetteLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.silhouetteLabel.setObjectName("silhouetteLabel")
        self.silhouetteTextLabel = QtWidgets.QLabel(Maker_Dialog)
        self.silhouetteTextLabel.setGeometry(QtCore.QRect(540, 570, 120, 23))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.silhouetteTextLabel.setFont(font)
        self.silhouetteTextLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.silhouetteTextLabel.setObjectName("silhouetteTextLabel")
        self.skeletonLabel = QtWidgets.QLabel(Maker_Dialog)
        self.skeletonLabel.setGeometry(QtCore.QRect(750, 600, 300, 225))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.skeletonLabel.setFont(font)
        self.skeletonLabel.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.skeletonLabel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.skeletonLabel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.skeletonLabel.setScaledContents(True)
        self.skeletonLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.skeletonLabel.setObjectName("skeletonLabel")
        self.skeletonTextLabel = QtWidgets.QLabel(Maker_Dialog)
        self.skeletonTextLabel.setGeometry(QtCore.QRect(840, 570, 120, 23))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.skeletonTextLabel.setFont(font)
        self.skeletonTextLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.skeletonTextLabel.setObjectName("skeletonTextLabel")
        self.getSilhouetteButton = QtWidgets.QPushButton(Maker_Dialog)
        self.getSilhouetteButton.setGeometry(QtCore.QRect(455, 840, 140, 45))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.getSilhouetteButton.setFont(font)
        self.getSilhouetteButton.setObjectName("getSilhouetteButton")
        self.saveSilhouetteButton = QtWidgets.QPushButton(Maker_Dialog)
        self.saveSilhouetteButton.setGeometry(QtCore.QRect(605, 840, 140, 45))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.saveSilhouetteButton.setFont(font)
        self.saveSilhouetteButton.setObjectName("saveSilhouetteButton")
        self.saveSkeletonButton = QtWidgets.QPushButton(Maker_Dialog)
        self.saveSkeletonButton.setGeometry(QtCore.QRect(905, 840, 140, 45))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.saveSkeletonButton.setFont(font)
        self.saveSkeletonButton.setObjectName("saveSkeletonButton")
        self.getSkeletonButton = QtWidgets.QPushButton(Maker_Dialog)
        self.getSkeletonButton.setGeometry(QtCore.QRect(755, 840, 140, 45))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.getSkeletonButton.setFont(font)
        self.getSkeletonButton.setObjectName("getSkeletonButton")
        self.howToUseItButton = QtWidgets.QPushButton(Maker_Dialog)
        self.howToUseItButton.setGeometry(QtCore.QRect(1103, 360, 180, 42))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.howToUseItButton.setFont(font)
        self.howToUseItButton.setObjectName("howToUseItButton")
        self.labelComboBox = QtWidgets.QComboBox(Maker_Dialog)
        self.labelComboBox.setGeometry(QtCore.QRect(1103, 645, 180, 42))
        self.labelComboBox.setObjectName("labelComboBox")
        self.labelLabel = QtWidgets.QLabel(Maker_Dialog)
        self.labelLabel.setGeometry(QtCore.QRect(1103, 600, 180, 23))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelLabel.setFont(font)
        self.labelLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.labelLabel.setObjectName("labelLabel")
        self.rectXLineEdit = QtWidgets.QLineEdit(Maker_Dialog)
        self.rectXLineEdit.setGeometry(QtCore.QRect(1185, 135, 96, 23))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.rectXLineEdit.setFont(font)
        self.rectXLineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.rectXLineEdit.setReadOnly(True)
        self.rectXLineEdit.setObjectName("rectXLineEdit")
        self.rectYLineEdit = QtWidgets.QLineEdit(Maker_Dialog)
        self.rectYLineEdit.setGeometry(QtCore.QRect(1185, 180, 96, 23))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.rectYLineEdit.setFont(font)
        self.rectYLineEdit.setReadOnly(True)
        self.rectYLineEdit.setObjectName("rectYLineEdit")
        self.rectWidthLineEdit = QtWidgets.QLineEdit(Maker_Dialog)
        self.rectWidthLineEdit.setGeometry(QtCore.QRect(1185, 225, 96, 23))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.rectWidthLineEdit.setFont(font)
        self.rectWidthLineEdit.setReadOnly(True)
        self.rectWidthLineEdit.setObjectName("rectWidthLineEdit")
        self.rectHeightLineEdit = QtWidgets.QLineEdit(Maker_Dialog)
        self.rectHeightLineEdit.setGeometry(QtCore.QRect(1185, 270, 96, 23))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.rectHeightLineEdit.setFont(font)
        self.rectHeightLineEdit.setReadOnly(True)
        self.rectHeightLineEdit.setObjectName("rectHeightLineEdit")

        self.retranslateUi(Maker_Dialog)
        QtCore.QMetaObject.connectSlotsByName(Maker_Dialog)

    def retranslateUi(self, Maker_Dialog):
        _translate = QtCore.QCoreApplication.translate
        Maker_Dialog.setWindowTitle(_translate("Maker_Dialog", "cloggy dataset maker"))
        self.directoryListWidget.setToolTip(_translate("Maker_Dialog", "<html><head/><body><p>asd</p></body></html>"))
        self.directories_label.setText(_translate("Maker_Dialog", "Directories"))
        self.contents_label.setText(_translate("Maker_Dialog", "Contents"))
        self.inputImageLabel.setText(_translate("Maker_Dialog", "Input Image"))
        self.inputImageTextLabel.setText(_translate("Maker_Dialog", "Input Image"))
        self.rectXLabel.setText(_translate("Maker_Dialog", "x"))
        self.rectYLabel.setText(_translate("Maker_Dialog", "y"))
        self.rectWidthLabel.setText(_translate("Maker_Dialog", "Width"))
        self.rectHeightLabel.setText(_translate("Maker_Dialog", "Height"))
        self.imageSizeLabel.setText(_translate("Maker_Dialog", "Image size : "))
        self.rectLabel.setText(_translate("Maker_Dialog", "Rectangle for grabcut"))
        self.silhouetteLabel.setText(_translate("Maker_Dialog", "Silhouette"))
        self.silhouetteTextLabel.setText(_translate("Maker_Dialog", "Silhouette"))
        self.skeletonLabel.setText(_translate("Maker_Dialog", "Skeleton"))
        self.skeletonTextLabel.setText(_translate("Maker_Dialog", "Skeleton"))
        self.getSilhouetteButton.setText(_translate("Maker_Dialog", "Get"))
        self.saveSilhouetteButton.setText(_translate("Maker_Dialog", "Save"))
        self.saveSkeletonButton.setText(_translate("Maker_Dialog", "Save"))
        self.getSkeletonButton.setText(_translate("Maker_Dialog", "Get"))
        self.howToUseItButton.setText(_translate("Maker_Dialog", "How to use it"))
        self.labelLabel.setText(_translate("Maker_Dialog", "Label"))
        self.rectXLineEdit.setText(_translate("Maker_Dialog", "0"))
        self.rectYLineEdit.setText(_translate("Maker_Dialog", "0"))
        self.rectWidthLineEdit.setText(_translate("Maker_Dialog", "0"))
        self.rectHeightLineEdit.setText(_translate("Maker_Dialog", "0"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Maker_Dialog = QtWidgets.QDialog()
    ui = Ui_Maker_Dialog()
    ui.setupUi(Maker_Dialog)
    Maker_Dialog.show()
    sys.exit(app.exec_())


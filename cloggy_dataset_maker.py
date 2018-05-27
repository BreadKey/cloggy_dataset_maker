import sys
import os

from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore
from MakerUI import Ui_Maker_Dialog

import cv2
import numpy as np
import imageProcessor as ip

class cloggy_dataset_maker(QDialog, Ui_Maker_Dialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        self.currentPath = os.getcwd()
        self.contentPath = None
        self.imagePath = None

        self.inputImageLabelbasicCursor = QtCore.Qt.ArrowCursor
        self.inputImageLabelWaitCursor = QtCore.Qt.WaitCursor
        self.inputImageLabelDrawRectCursor = QtCore.Qt.CrossCursor

        self.initUI()
        self.show()
        self.imageInProcess = None
        self.isShiftKeyPressed = False
        self.isDrawingRect = False
        self.isInputImageExist = False
        self.rectForGrabcut = (0, 0, 0, 0)
        self.maskForGrabcut = None
        self.grabCutWithRect = True

        self.markFG = {'color' : (255, 255, 255), 'value' : 1}
        self.markBG = {'color' : (0, 0, 0), 'value' : 0}
        self.marker = self.markFG
        self.markerSize = 3
        self.isMarking = False

    def initUI(self):
        self.addDirectoryList()
        self.directoryListWidget.itemDoubleClicked.connect(self.directoryListDoubleClicked)

        self.contentListWidget.itemDoubleClicked.connect(self.contentListDoubleClicked)

        self.inputImageScrollArea.setWidget(self.inputImageLabel)
        self.inputImageLabel.mousePressEvent = self.mousePressEventInInputImageLabel
        self.inputImageLabel.mouseReleaseEvent = self.mouseReleaseEventInImageLabel
        self.inputImageLabel.mouseMoveEvent = self.mouseMoveEventInInputImageLabel
        self.inputImageLabel.setCursor(self.inputImageLabelbasicCursor)

        self.getSilhouetteButton.clicked.connect(self.getSilhouette)

        self.howToUseItButton.clicked.connect(self.howToUseIt)

    def addDirectoryList(self):
        self.directoryListWidget.clear()
        dir = next(os.walk(self.currentPath))[1]
        dir.sort()
        self.directoryListWidget.addItem("..")
        self.directoryListWidget.addItems(dir)

    def directoryListDoubleClicked(self, item):
        self.contentListWidget.clear()
        if item.text() == "..":
            self.currentPath = os.path.split(self.currentPath)[0]
            self.addDirectoryList()
            return

        self.contentPath = os.path.join(self.currentPath, item.text())
        self.addContentList()

    def addContentList(self):
        self.contentListWidget.clear()
        _, dir, files = next(os.walk(self.contentPath))
        self.contentListWidget.addItems(dir)
        self.contentListWidget.addItems(files)

    def contentListDoubleClicked(self, item):
        path = os.path.join(self.contentPath, item.text())

        if os.path.isdir(path):
            self.currentPath = self.contentPath
            self.contentPath = path
            self.addDirectoryList()
            self.addContentList()
        elif os.path.isfile(path):
            filename = os.path.split(path)[1]
            fileformat = str.split(filename, '.')[1]

            if fileformat == 'png' or fileformat == 'jpg':
                image:QtGui.QImage = QtGui.QImage(path)
                self.setImageToLabel(self.inputImageLabel, image, resizeLabel=True)
                self.imageSizeLabel.setText("Image size : {} x {}".format(image.width(), image.height()))
                self.isInputImageExist = True
                self.imagePath = path
                self.initInput()

    def setImageToLabel(self, label:QLabel, image:QtGui.QImage, resizeLabel=False):
        pixmab:QtGui.QPixmap = QtGui.QPixmap.fromImage(image)

        if resizeLabel:
            label.setMinimumSize(pixmab.size())
            label.setBaseSize(pixmab.size())

        label.setPixmap(pixmab)

    def mousePressEventInInputImageLabel(self, event:QtGui.QMouseEvent):
        if self.isShiftKeyPressed and not self.isDrawingRect:
            self.startDrawRect(event.pos())
        elif not self.isShiftKeyPressed and not self.isDrawingRect:
            if self.imageInProcess is not None:
                if not self.isMarking:
                    self.isMarking = True

                    self.changerMarker(event)
                    self.mark(event.pos())

    def mouseMoveEventInInputImageLabel(self, event:QtGui.QMouseEvent):
        if self.isShiftKeyPressed and self.isDrawingRect:
            self.drawingRect(event.pos())
        elif not self.isShiftKeyPressed and self.isMarking:
            self.changerMarker(event)
            self.mark(event.pos())


    def mouseReleaseEventInImageLabel(self, event:QtGui.QMouseEvent):
        if self.isShiftKeyPressed and self.isDrawingRect:
            self.endDrawRect(event.pos())
        if self.isMarking:
            self.isMarking = False

    def startDrawRect(self, pos:QtCore.QPoint):
        self.isDrawingRect = True
        self.rectXValueLabel.setText(str(pos.x()))
        self.rectYValueLabel.setText(str(pos.y()))
        self.imageInProcess = cv2.imread(self.imagePath)
        #self.maskForGrabcut = np.zeros(self.imageInProcess.shape[:2], dtype=np.uint8)

    def drawingRect(self, pos:QtCore.QPoint):
        imgCopy = self.imageInProcess.copy()
        self.drawRect(pos, imgCopy)

    def endDrawRect(self, pos:QtCore.QPoint):
        self.isDrawingRect = False
        x, y, width, height, self.imageInProcess = self.drawRect(pos, self.imageInProcess)
        self.rectForGrabcut = (x, y, width, height)
        self.rectXValueLabel.setText(str(x))
        self.rectYValueLabel.setText(str(y))
        self.rectWidthValueLabel.setText(str(width))
        self.rectHeightValueLabel.setText(str(height))

        self.maskForGrabcut = np.zeros(self.imageInProcess.shape[:2], dtype=np.uint8)
        self.grabCutWithRect = True

    def drawRect(self, pos:QtCore.QPoint, img):
        x = int(self.rectXValueLabel.text())
        y = int(self.rectYValueLabel.text())

        if x > pos.x():
            width = x - pos.x()
            x = pos.x()

        else:
            width = pos.x() - x

        if y > pos.y():
            height = y - pos.y()
            y = pos.y()

        else:
            height = pos.y() - y

        rectedImg = ip.drawRectangle(img, (x, y, width, height), color=(0, 0, 255), size=1)
        qimg = self.npArrayToQImage(rectedImg)
        self.setImageToLabel(self.inputImageLabel, qimg, True)

        return (x, y, width, height, rectedImg)

    def changerMarker(self, event:QtGui.QMouseEvent):
        if event.buttons() == QtCore.Qt.LeftButton:
            self.marker = self.markFG
        elif event.buttons() == QtCore.Qt.RightButton:
            self.marker = self.markBG

    def mark(self, pos:QtCore.QPoint):
        x = pos.x()
        y = pos.y()

        self.imageInProcess = cv2.circle(self.imageInProcess, (x, y), self.markerSize, self.marker['color'], -1)
        self.maskForGrabcut = cv2.circle(self.maskForGrabcut, (x, y), self.markerSize, self.marker['value'], -1)
        qimg = self.npArrayToQImage(self.imageInProcess)
        self.setImageToLabel(self.inputImageLabel, qimg)

    def keyPressEvent(self, QKeyEvent:QtGui.QKeyEvent):
        if QKeyEvent.key() == 16777248:
            self.shiftKeyPressed()

    def keyReleaseEvent(self, QKeyEvent:QtGui.QKeyEvent):
        if QKeyEvent.key() == 16777248:
            self.shiftKeyReleased()
            
    def shiftKeyPressed(self):
        if self.isInputImageExist:
            self.inputImageLabel.setCursor(self.inputImageLabelDrawRectCursor)
            self.isShiftKeyPressed = True

    def shiftKeyReleased(self):
        self.inputImageLabel.setCursor(self.inputImageLabelbasicCursor)
        self.isShiftKeyPressed = False
        if self.isDrawingRect:
            qimg = self.npArrayToQImage(self.imageInProcess)
            self.setImageToLabel(self.inputImageLabel, qimg)
            self.initInput()

    def npArrayToQImage(self, img, copy=False):
        gray_color_table = [QtGui.qRgb(i, i, i) for i in range(256)]

        if img.dtype == np.uint8:
            if len(img.shape) == 2:
                qim = QtGui.QImage(img.data, img.shape[1], img.shape[0], img.strides[0], QtGui.QImage.Format_Indexed8)
                qim.setColorTable(gray_color_table)
                return qim.copy() if copy else qim

            elif len(img.shape) == 3:
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                if img.shape[2] == 3:
                    qim = QtGui.QImage(img.data, img.shape[1], img.shape[0], img.strides[0], QtGui.QImage.Format_RGB888);
                    return qim.copy() if copy else qim
                elif img.shape[2] == 4:
                    qim = QtGui.QImage(img.data, img.shape[1], img.shape[0], img.strides[0], QtGui.QImage.Format_ARGB32);
                    return qim.copy() if copy else qim

    def getSilhouette(self):
        self.setCursor(self.inputImageLabelWaitCursor)

        img = cv2.imread(self.imagePath)
        width, height = self.rectForGrabcut[2:4]
        if width > 0 and height > 0:
            if self.grabCutWithRect:
                bgdModel = np.zeros((1, 65), np.float64)
                fgdModel = np.zeros((1, 65), np.float64)
                cv2.grabCut(img, self.maskForGrabcut, self.rectForGrabcut, bgdModel, fgdModel, 1, cv2.GC_INIT_WITH_RECT)
                self.grabCutWithRect = False
            else:
                bgdModel = np.zeros((1, 65), np.float64)
                fgdModel = np.zeros((1, 65), np.float64)
                cv2.grabCut(img, self.maskForGrabcut, self.rectForGrabcut, bgdModel, fgdModel, 1, cv2.GC_INIT_WITH_MASK)
            silhouette = np.where((self.maskForGrabcut == 1) + (self.maskForGrabcut == 3), 255, 0).astype('uint8')
            qimg = self.npArrayToQImage(silhouette)
            self.setImageToLabel(self.silhouetteLabel, qimg)
        self.setCursor(self.inputImageLabelbasicCursor)

    def initInput(self):
        self.imageInProcess = None
        self.maskForGrabcut = None
        self.isDrawingRect = False
        self.isShiftKeyPressed = False
        self.isMarking = False
        self.rectXValueLabel.setText("0")
        self.rectYValueLabel.setText("0")
        self.rectWidthValueLabel.setText("0")
        self.rectHeightValueLabel.setText("0")
        self.rectForGrabcut = (0, 0, 0, 0)

    def howToUseIt(self):
        QMessageBox.about(self, "How to use it", "1. Select the cloggy image you want to get a data."
                                                 "\n\n2. Holding down the Shift key, click and drag to draw the rectangle containing the cloggy."
                                                 "\n\n3. To get a silhouette, press the Get button under the silhouette box. (The rectangle must exist before getting a silhouette.)"
                                                 "\n\n4. If you want to get a more accurate silhouette, mark the foreground of the object with mouse left click and mark the background of the object with mouse right click."
                                                 "\n\n5. To get a skeleton, press the Get button under the silhouette box. (The Silhouette must exist before getting a skeleton.)"
                                                 "\n\n6. Press the save buttons to save the results.")

app = QApplication(sys.argv)
xwin = cloggy_dataset_maker()
app.exec()

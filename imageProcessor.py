import numpy as np
import cv2
import matplotlib.pyplot as plt

_medianFilterKernalSize = 3
_medianFilterCount = 30

def deleteBackground(img, rect):
    mask = np.full(img.shape[:2], 2, np.uint8)

    bgdModel = np.zeros((1, 65), np.float64)
    fgdModel = np.zeros((1, 65), np.float64)

    cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)

    mask2 = np.where((mask == 2)|(mask == 0), 0, 1).astype('uint8')
    #return img*mask2[:, :, np.newaxis]
    return mask2

def objectToWhite(img):
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    for i in range(gray.shape[0]):
        for j in range(gray.shape[1]):
            if gray[i][j] != 0:
                gray[i][j] = 255
    return gray

def drawRectangle(img, rect: tuple, color: tuple = (0, 255, 0), size: int = 7):
    newImg = img.copy()
    startXY = (rect[0], rect[1])
    endXY = (rect[0] + rect[2], rect[1] + rect[3])

    return cv2.rectangle(newImg, startXY, endXY, color, size)
import pygame as pg
import numpy as np

figureImages = np.ndarray(12, dtype=pg.Surface)
figureImagesDict = {}

def getBoardImage():
    return pg.image.load(r'./Sl/board.png').convert_alpha()

def initFigureImages():
    allFiguresImage = pg.image.load(r'./Sl/figures.png').convert_alpha()
    for row in range(2):
        for column in range(6):
            image = allFiguresImage.subsurface((column * 60,  row * 60, 60, 60))
            image = pg.transform.rotozoom(image, 0, 731 / 8 / 60)
            figureImages[row * 6 + column] = image
    figureNumbers = [-9, -100, -5, -2, -3, -1, 9, 100, 5, 2, 3, 1]
    for i in range(12):
        figureImagesDict[figureNumbers[i]] = figureImages[i]

def getFigureImageByNum(figNum: int):
    return figureImagesDict[figNum]
 

import numpy as np
import pygame as pg
from . import guiImages as guiImg
import chessLogic 

BOARD_START_POS = [0, 0]
BOARD_FIELD_WIDTH = 731 / 8

class Board:
    def __init__(self, display_surface: pg.surface):
        self.selectedFigure = None
        self.potentialMoves = []
        self.displaySurface = display_surface
        self.initBoard()

    def initBoard(self):
        guiImg.initFigureImages()

    def drawBoard(self, table: np.ndarray):
        self.displaySurface.blit(guiImg.getBoardImage(), BOARD_START_POS)
        for i in range(8):
            for j in range(8):
                figNum = table[i][j]
                if(figNum == 0):
                    continue
                image = guiImg.getFigureImageByNum(figNum)
                self.displaySurface.blit(image, [BOARD_START_POS[0] + j * BOARD_FIELD_WIDTH, BOARD_START_POS[1] + i * BOARD_FIELD_WIDTH])
        if self.selectedFigure != None:
            pg.draw.rect(self.displaySurface, (255, 0, 0), (BOARD_START_POS[1] + self.selectedFigure[1] * BOARD_FIELD_WIDTH, BOARD_START_POS[0] + self.selectedFigure[0] * BOARD_FIELD_WIDTH, BOARD_FIELD_WIDTH , BOARD_FIELD_WIDTH), 5)
            for move in self.potentialMoves:
                pg.draw.rect(self.displaySurface, (0, 0, 255), (BOARD_START_POS[1] + move[1] * BOARD_FIELD_WIDTH, BOARD_START_POS[0] + move[0] * BOARD_FIELD_WIDTH, BOARD_FIELD_WIDTH , BOARD_FIELD_WIDTH), 5)

    def handleClick(self, table: np.ndarray, mousePos: tuple, turn: int):
        x = (mousePos[1] - BOARD_START_POS[1]) // BOARD_FIELD_WIDTH
        y = (mousePos[0] - BOARD_START_POS[0]) // BOARD_FIELD_WIDTH
        if x < 0 or y < 0 or y > 7 or x > 7:
            self.selectedFigure = None
            self.potentialMoves = []
            return turn
        clickedPos = (int(x), int(y))
        print(clickedPos)
        if clickedPos in self.potentialMoves:
            table[clickedPos] = table[self.selectedFigure]
            table[self.selectedFigure] = 0.0
            self.selectedFigure = None
            self.potentialMoves = []
            return -turn
        elif table[int(x)][int(y)] * turn > 0:
            self.selectedFigure = clickedPos
            self.potentialMoves = chessLogic.getPotentialMoveFromPos(table, self.selectedFigure)
        else: 
            self.selectedFigure = None
            self.potentialMoves = []
        return turn

    # def selectFigure(self, table: np.ndarray, mousePos: tuple):
    #     # mousePos = pg.mouse.get_pos()
    #     x = (mousePos[1] - BOARD_START_POS[1]) // BOARD_FIELD_WIDTH
    #     y = (mousePos[0] - BOARD_START_POS[0]) // BOARD_FIELD_WIDTH
    #     if x < 0 or y < 0 or y > 7 or x > 7:
    #         self.selectedFigure = None
    #         return
    #     # print(table[int(x)][int(y)])
    #     if table[int(x)][int(y)] == 0:
    #         self.selectedFigure = None
    #         return 
    #     self.selectedFigure = (int(x), int(y))
    #     self.potentialMoves = chessLogic.getPotentialMoveFromPos(table, self.selectedFigure)
    #     return
    
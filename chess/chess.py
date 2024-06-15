import numpy as np
import pygame as pg
from gui.Board import *

from constants import *

table = np.ndarray(shape=(8,8))

def getInitFigureFromPos(i, j):
    if i > 1 and i < 6:
        return 0
    elif i == 1:
        return BLACK_PAWN
    elif i == 6:
        return WHITE_PAWN
    elif i == 0:
        if j == 0 or j == 7:
            return BLACK_ROOK
        elif j == 1 or j == 6:
            return BLACK_KNIGHT
        elif j == 2 or j == 5:
            return BLACK_BISHOP
        elif j == 3:
            return BLACK_QUEEN
        else: 
            return BLACK_KING
    else:
        if j == 0 or j == 7:
            return WHITE_ROOK
        elif j == 1 or j == 6:
            return WHITE_KNIGHT
        elif j == 2 or j == 5:
            return WHITE_BISHOP
        elif j == 3:
            return WHITE_QUEEN
        else:
            return WHITE_KING
        
def initTable(table: np.ndarray):
    for i in range(0,8):
        for j in range(0,8):
            table[i, j] = getInitFigureFromPos(i, j)

    
display_surface = pg.display.set_mode((0, 0), pg.FULLSCREEN) 
pg.display.set_caption('Sah')
def startGame():
    initTable(table)
    board = Board(display_surface)
    turn = 1
    while True:
        # get all events
        ev = pg.event.get()
            # proceed events
        for event in ev:
            # handle MOUSEBUTTONUP
            if event.type == pg.MOUSEBUTTONUP:
                mousePos = pg.mouse.get_pos()
                turn = board.handleClick(table, mousePos, turn)
        display_surface.fill((255,255,255))
        board.drawBoard(table)
        pg.display.update()  

startGame()




print(table)

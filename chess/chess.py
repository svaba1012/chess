import numpy as np
import pygame as pg
import button as bt
from Board import *

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
    '''
    set figures in their init start positions
    '''
    for i in range(0,8):
        for j in range(0,8):
            table[i, j] = getInitFigureFromPos(i, j)

display_surface = pg.display.set_mode((0, 0), pg.FULLSCREEN) 

def mainMenu():
    pg.display.set_caption('Sah')
    X = 1350
    Y = 700
    pg.init()
    naslov = bt.button(X / 2 - 150, 50, 300, 50, (0,0,0), "SRB SAH", 20, (255,255,255))
    p1VsP2 = bt.button(X / 2 - 150, Y / 2, 300, 50, (255,255,255), "P1 VS P2", 20, (0,0,0))
    p1VsCom = bt.button(X / 2 - 150, Y / 2 - 75, 300, 50, (255,255,255), "P1 VS COM", 20, (0,0,0))
    izlaz = bt.button(X / 2 - 150, Y / 2 + 75, 300, 50, (255,255,255), "QUIT", 20, (0,0,0))
    igraj = None
    kraj = None
    while True:
        display_surface.fill((0,0,0))
        naslov.crtaj(display_surface)
        p1VsP2.crtaj(display_surface)
        p1VsCom.crtaj(display_surface)
        izlaz.crtaj(display_surface)
        igraj = p1VsP2.buttonFunc(startGameP1vsP2)
        p1VsCom.buttonFunc(startGameP1vsCOM)
        kraj = izlaz.buttonFunc(pg.quit)
        if igraj != None:
            break
        if kraj != None:
            pg.quit() 
            quit()
        for event in pg.event.get() : 
            if event.type == pg.QUIT : 
                pg.quit() 
                quit() 
            pg.display.update()


def gameOver(gameStatus: int):
    font = pg.font.Font('freesansbold.ttf', 32)
    textCheckMateB = font.render('Black won. Click anywhere to exit', True, (0,0,255), (0,255,0))
    textCheckMateW = font.render('White won. Click anywhere to exit', True, (0,0,255), (0,255,0))
    textStalemate = font.render('Stalemate. Click anywhere to exit', True, (0,0,255), (0,255,0))
    checkMateRect = textCheckMateB.get_rect()
    checkMateRect.center = (370, 350)

    if gameStatus == 1:
        display_surface.blit(textCheckMateW, checkMateRect)            
    elif gameStatus == -1:
        display_surface.blit(textCheckMateB, checkMateRect)
    elif gameStatus == 2:
        display_surface.blit(textStalemate, checkMateRect)

    pg.display.update()

    while gameStatus != 0:
        ev = pg.event.get()            
        for event in ev:
                if event.type == pg.MOUSEBUTTONUP:
                    gameStatus = 0



def startGameP1vsP2():
    initTable(table)
    board = Board(display_surface)
    turn = 1
    gameStatus = 0
    display_surface.fill((255,255,255))
    board.drawBoard(table)
    while gameStatus == 0:
        gameStatus = board.playerMove(table, turn)
        turn *= -1
    gameOver(gameStatus)
    
                    
def startGameP1vsCOM():
    initTable(table)
    board = Board(display_surface)
    turn = 1
    gameStatus = 0
    display_surface.fill((255,255,255))
    board.drawBoard(table)
    while gameStatus == 0:
        gameStatus = board.playerMove(table, turn)
        turn *= -1
        if gameStatus != 0:
            break
        gameStatus = board.comMove(table, turn)
        turn *= -1
    gameOver(gameStatus)
    
mainMenu()





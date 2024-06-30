import numpy as np
import pygame as pg
from gui import guiImages as guiImg
from minimax import *
import chessLogic 

BOARD_START_POS = [0, 0]
BOARD_FIELD_WIDTH = 731 / 8

UPGRADE_PAWN_MENU_START_POS = [BOARD_START_POS[0] + BOARD_FIELD_WIDTH * 2, BOARD_START_POS[1] + BOARD_FIELD_WIDTH * 3.5]
UPGRADE_PAWN_MENU_HEIGHT = 300
UPGRADE_PAWN_MENU_PADDING = 50

CHESS_ENDGAME = 2
CHESS_MIDGAME = 1
CHESS_OPENGAME = 0

TABLE_POS = [[0, 0, 0, 0, 0, 0, 0, 0], 
             [0, 1/6, 1/6, 1/6, 1/6, 1/6, 1/6, 0],
             [0, 1/6, 1/3, 1/3, 1/3, 1/3, 1/6, 0],
             [0, 1/6, 1/3, 1/2, 1/2, 1/3, 1/6, 0],
             [0, 1/6, 1/3, 1/2, 1/2, 1/3, 1/6, 0],
             [0, 1/6, 1/3, 1/3, 1/3, 1/3, 1/6, 0],
             [0, 1/6, 1/6, 1/6, 1/6, 1/6, 1/6, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],]

def evalTable(table: np.ndarray, turn: int):
    sum = 0
    for i in range(8):
        for j in range(8):
            if table[i][j] == 0:
                continue
            fig = table[i][j]
            sign = 1        
            if fig < 0.0:
                sign = -1
            if abs(fig) == 2:
                fig = sign * 3
            sum += fig + sign * TABLE_POS[i][j]
    return sum
                
def makeMove(table: np.ndarray, move):
    newTable = table.copy()
    if move["figure"] == None:
        fig = table[move["pos"]]
    else:
        fig = move["figure"]
    newTable[move["pos"]] = 0
    newTable[move["move"]] = fig
    return newTable

def realMakeMove(table: np.ndarray, move):
    if(move == None or move["pos"] == None):
        return 1
    if move["figure"] == None:
        fig = table[move["pos"]]
    else:
        fig = move["figure"]
    table[move["pos"]] = 0
    table[move["move"]] = fig
    return 0

def isEnd(table: np.ndarray, potMoves, turn):
    if(len(potMoves) == 0):
        if chessLogic.isCheck(table, turn):
            return -turn
        else: 
            return 2 #stalemate
    return 0
    

class Board:
    def __init__(self, display_surface: pg.surface):
        self.selectedFigure = None
        self.potentialMoves = []
        self.allPotentialMoves = []
        self.displaySurface = display_surface
        self.pawnForUpgradePos = None
        self.initBoard()

    def initBoard(self):
        '''
        set images used for rendering board with pieces
        '''
        guiImg.initFigureImages()
        
    def drawBoard(self, table: np.ndarray):
        '''
        render board
        '''
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
        if self.pawnForUpgradePos != None:
            turn = -1
            if self.pawnForUpgradePos[0] == 0:
                turn = 1 
            self.drawUpgradePawnMenu(turn)
        pg.display.update()

    def drawUpgradePawnMenu(self, turn: int):
        '''
        render promotion menu for pawn
        '''
        pg.draw.rect(self.displaySurface, (200, 150, 150), (UPGRADE_PAWN_MENU_START_POS[0] - UPGRADE_PAWN_MENU_PADDING // 2, UPGRADE_PAWN_MENU_START_POS[1] - UPGRADE_PAWN_MENU_PADDING // 2, BOARD_FIELD_WIDTH * 4 + UPGRADE_PAWN_MENU_PADDING, BOARD_FIELD_WIDTH + UPGRADE_PAWN_MENU_PADDING))
        upgradeFigs = [2, 3, 5, 9]
        for i in range(4):
            pg.draw.rect(self.displaySurface, (0, 255, 0), (UPGRADE_PAWN_MENU_START_POS[0] + i * BOARD_FIELD_WIDTH, UPGRADE_PAWN_MENU_START_POS[1], BOARD_FIELD_WIDTH, BOARD_FIELD_WIDTH), 3)
            image = guiImg.getFigureImageByNum(turn * upgradeFigs[i])
            self.displaySurface.blit(image, [UPGRADE_PAWN_MENU_START_POS[0] + i * BOARD_FIELD_WIDTH, UPGRADE_PAWN_MENU_START_POS[1]])

    def handlePawnUpgradeMenuClick(self, table: np.ndarray, mousePos: tuple, turn: int):

        upgradeFigs = [2, 3, 5, 9]
        y = (mousePos[1] - UPGRADE_PAWN_MENU_START_POS[1]) // BOARD_FIELD_WIDTH
        x = (mousePos[0] - UPGRADE_PAWN_MENU_START_POS[0]) // BOARD_FIELD_WIDTH
        if x < 0 or y != 0 or x > 3:
            return turn
        table[self.pawnForUpgradePos] = turn * upgradeFigs[int(x)]
        self.pawnForUpgradePos = None
        self.drawBoard(table)
        return -turn

    def calculatePossibleMoves(self, table: np.ndarray, turn: int):
        '''
        return 1 if white wins, -1 if black and 0 if continue and 2 if stalemate
        '''
        self.allPotentialMoves = chessLogic.getAllPotentialMoves(table, turn)
        # print(self.allPotentialMoves)
        
        if(len(self.allPotentialMoves) == 0):
            if chessLogic.isCheck(table, turn):
                return -turn
            else: 
                return 2 #stalemate
        return 0

    def handleClick(self, table: np.ndarray, mousePos: tuple, turn: int):
        if self.pawnForUpgradePos != None:
            return self.handlePawnUpgradeMenuClick(table, mousePos, turn)
        x = (mousePos[1] - BOARD_START_POS[1]) // BOARD_FIELD_WIDTH
        y = (mousePos[0] - BOARD_START_POS[0]) // BOARD_FIELD_WIDTH
        if x < 0 or y < 0 or y > 7 or x > 7:
            self.selectedFigure = None
            self.potentialMoves = []
            return turn
        clickedPos = (int(x), int(y))
        if clickedPos in self.potentialMoves:
            table[clickedPos] = table[self.selectedFigure]
            table[self.selectedFigure] = 0.0
            self.selectedFigure = None
            self.potentialMoves = []
            if table[clickedPos] * turn == 1 and (clickedPos[0] == 7 or clickedPos[0] == 0):
                self.pawnForUpgradePos = clickedPos
                self.drawBoard(table)
                return turn
            self.drawBoard(table)
            return -turn
        elif table[int(x)][int(y)] * turn > 0:
            shouldRerender = self.selectedFigure != clickedPos
            self.selectedFigure = clickedPos
            hasMoves = False
            for moves in self.allPotentialMoves:
                if moves["pos"] == clickedPos:
                    hasMoves = True
                    self.potentialMoves = moves["moves"]
                    break
            if not hasMoves: 
                self.potentialMoves = []
            if shouldRerender:
                self.drawBoard(table)
        else:
            shouldRerender = self.selectedFigure != None 
            self.selectedFigure = None
            self.potentialMoves = []
            if shouldRerender:
                self.drawBoard(table)
        return turn
    
    def playerMove(self, table: np.ndarray, turn: int):
        newTurn = turn
        gameStatus = self.calculatePossibleMoves(table, turn)
        if gameStatus != 0:
            return gameStatus
        while newTurn == turn:
            ev = pg.event.get()                        
            for event in ev:
                if event.type == pg.MOUSEBUTTONUP:
                    if gameStatus != 0:
                        pg.quit()
                        quit()
                    mousePos = pg.mouse.get_pos()
                    newTurn = self.handleClick(table, mousePos, turn)
        return gameStatus

    def comMove(self, table: np.ndarray, turn: int):
        (bestScore, bestMove) = minimax(table, evalTable, chessLogic.getAllPotentialMovesArray, turn, makeMove, 3, isEnd)
        res = realMakeMove(table, bestMove)
        self.drawBoard(table)
        if res != 0:
            if bestScore == 0:
                return 2
            return int(bestScore / abs(bestScore))
        else:
            return 0

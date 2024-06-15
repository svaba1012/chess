import numpy as np
from constants import *

def lineFigurePotentialMoves(table: np.ndarray, pos: tuple[int, int], directions: tuple):
    '''
    line figure = rook, queen or bishop
    generic function for calculating potential moves for these figures
    '''
    figureY = pos[0]
    figureX = pos[1]
    potMoves = []
    # directions = ((-1, 0), (0, 1), (1, 0), (0, -1))
    for dir in directions:
        for i in range(1, 8):
            # ! set for all directions
            newFigurePosY = figureY + i * dir[0]
            newFigurePosX = figureX + i * dir[1]
            if newFigurePosY < 0 or newFigurePosY >= 8 or newFigurePosX < 0 or newFigurePosX >= 8:
                break
            tempProduct = table[newFigurePosY][newFigurePosX] * table[figureY] [figureX]
            print(tempProduct)
            if tempProduct <= 0.0:
                figNum = table[pos]
                potTable = np.copy(table)
                potTable[newFigurePosY][newFigurePosX] = figNum
                potTable[pos] = 0
                if not isCheck(potTable, figNum/abs(figNum)):
                    potMoves.append((newFigurePosY, newFigurePosX))
            if tempProduct != 0:
                break
    return potMoves

def kingPotentialMoves(table: np.ndarray, pos: tuple[int, int]):
    figureY = pos[0]
    figureX = pos[1]
    potMoves = []
    directions = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, -1), (1, 1))
    for dir in directions:
        # ! set for all directions
        newFigurePosY = figureY + dir[0]
        newFigurePosX = figureX + dir[1]
        if newFigurePosY < 0 or newFigurePosY >= 8 or newFigurePosX < 0 or newFigurePosX >= 8:
            continue
        tempProduct = table[newFigurePosY][newFigurePosX] * table[figureY][figureX]
        if tempProduct <= 0:
            figNum = table[pos]
            potTable = np.copy(table)
            potTable[newFigurePosY][newFigurePosX] = figNum
            potTable[pos] = 0
            if not isCheck(potTable, figNum/abs(figNum)):
                potMoves.append((newFigurePosY, newFigurePosX))
    return potMoves

def rookPotentialMoves(table: np.ndarray, pos: tuple[int, int]):
    return lineFigurePotentialMoves(table, pos, ((-1, 0), (0, 1), (1, 0), (0, -1)))

def bishopPotentialMoves(table: np.ndarray, pos: tuple[int, int]):
    return lineFigurePotentialMoves(table, pos, ((-1, -1), (-1, 1), (1, 1), (1, -1)))

def queenPotentialMoves(table: np.ndarray, pos: tuple[int, int]):
    return lineFigurePotentialMoves(table, pos, ((-1, -1), (-1, 1), (1, 1), (1, -1), (-1, 0), (0, 1), (1, 0), (0, -1)))

def knightPotentialMoves(table: np.ndarray, pos: tuple[int, int]):
    figureY = pos[0]
    figureX = pos[1]
    potMoves = []
    directions = ((-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1))
    for dir in directions:
        # ! set for all directions
        newFigurePosY = figureY + dir[0]
        newFigurePosX = figureX + dir[1]
        if newFigurePosY < 0 or newFigurePosY >= 8 or newFigurePosX < 0 or newFigurePosX >= 8:
            continue
        tempProduct = table[newFigurePosY][newFigurePosX] * table[figureY][figureX]
        if tempProduct <= 0:
            figNum = table[pos]
            potTable = np.copy(table)
            potTable[newFigurePosY][newFigurePosX] = figNum
            potTable[pos] = 0
            if not isCheck(potTable, figNum/abs(figNum)):
                potMoves.append((newFigurePosY, newFigurePosX))
    return potMoves

def pawnCheckDiagonal(table: np.ndarray, pos: tuple[int, int], direction: int, diag: int):
    figureY = pos[0]
    figureX = pos[1]
    newFigurePosY = figureY + direction
    newFigurePosX = figureX + diag
    isInvalidPos = newFigurePosY < 0 or newFigurePosY >= 8 or newFigurePosX < 0 or newFigurePosX >= 8
    if isInvalidPos:
        return None
    tempProduct = table[newFigurePosY][newFigurePosX] * table[figureY][figureX] 
    if tempProduct < 0:
        figNum = table[pos]
        potTable = np.copy(table)
        potTable[newFigurePosY][newFigurePosX] = figNum
        potTable[pos] = 0
        if isCheck(potTable, figNum/abs(figNum)):
            return None
        return (newFigurePosY, newFigurePosX)
    

def pawnPotentialMoves(table: np.ndarray, pos: tuple[int, int]):
    direction = -int(table[pos[0]][pos[1]])
    figureY = pos[0]
    figureX = pos[1]
    isFirstPawnMove = (figureY == 6 and direction == -1) or (figureY == 1 and direction == 1)
    potentialDistance = 2
    if(isFirstPawnMove):
        potentialDistance = 3 
    potMoves = []
    potDiagMove = pawnCheckDiagonal(table, pos, direction, -1)
    if(potDiagMove != None):
        potMoves.append(potDiagMove)
    potDiagMove = pawnCheckDiagonal(table, pos, direction, 1)
    if(potDiagMove != None):
        potMoves.append(potDiagMove)
    
    for i in range(1, potentialDistance):
        # ! set for all directions
        newFigurePosY = figureY + i * direction
        newFigurePosX = figureX 
        # print(newFigurePosY)
        if newFigurePosY < 0 or newFigurePosY >= 8:
            break
        tempProduct = table[newFigurePosY][newFigurePosX] * table[figureY][figureX] != 0 
        if tempProduct == 0:
            figNum = table[pos]
            potTable = np.copy(table)
            potTable[newFigurePosY][newFigurePosX] = figNum
            potTable[pos] = 0
            if not isCheck(potTable, figNum/abs(figNum)):
                potMoves.append((newFigurePosY, newFigurePosX))
        else:
            break
    return potMoves


figurePotMoveDict = {
    -100:   kingPotentialMoves,
    -9:     queenPotentialMoves,
    -5:     rookPotentialMoves,
    -3:     bishopPotentialMoves,
    -2:     knightPotentialMoves,
    -1:     pawnPotentialMoves,
    1:      pawnPotentialMoves,
    2:      knightPotentialMoves,
    3:      bishopPotentialMoves,
    5:      rookPotentialMoves,
    9:      queenPotentialMoves,
    100:    kingPotentialMoves
}

def isCheck(table: np.ndarray, turn: int):
    king = turn * WHITE_KING
    kingPos = (0, 0)
    for i in range(8):
        for j in range(8):
            if(table[i][j] == king):
                kingPos = (i, j)
                break
    kingPosX = kingPos[1]
    kingPosY = kingPos[0]
    # check if pawn attacks

    # check if knight attacks
    directions = ((-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1))
    for dir in directions:
        # ! set for all directions
        newFigurePosY = kingPosY + dir[0]
        newFigurePosX = kingPosX + dir[1]
        if newFigurePosY < 0 or newFigurePosY >= 8 or newFigurePosX < 0 or newFigurePosX >= 8:
            continue
        isKnightAttacking = table[newFigurePosY][newFigurePosX] == turn * BLACK_KNIGHT
        if isKnightAttacking:
            return True
    # check if bishop/queen attacks
    directions = ((-1, -1), (-1, 1), (1, -1), (1, 1))
    for dir in directions:
        for i in range(1, 8):
            # ! set for all directions
            newFigurePosY = kingPosY + i * dir[0]
            newFigurePosX = kingPosX + i * dir[1]
            if newFigurePosY < 0 or newFigurePosY >= 8 or newFigurePosX < 0 or newFigurePosX >= 8:
                break
            fieldFig = table[newFigurePosY][newFigurePosX]
            tempProduct = fieldFig * table[kingPosY] [kingPosX]
            if tempProduct > 0.0:
                break
            if fieldFig == BLACK_QUEEN * turn or fieldFig == BLACK_BISHOP * turn:
                return True
    # check if rook/queen attacks
    directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
    for dir in directions:
        for i in range(1, 8):
            # ! set for all directions
            newFigurePosY = kingPosY + i * dir[0]
            newFigurePosX = kingPosX + i * dir[1]
            if newFigurePosY < 0 or newFigurePosY >= 8 or newFigurePosX < 0 or newFigurePosX >= 8:
                break
            fieldFig = table[newFigurePosY][newFigurePosX]
            tempProduct = fieldFig * table[kingPosY] [kingPosX]
            if tempProduct > 0.0:
                break
            if fieldFig == BLACK_QUEEN * turn or fieldFig == BLACK_ROOK * turn:
                return True
    # check if king attacks
    directions = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, -1), (1, 1))
    for dir in directions:
        # ! set for all directions
        newFigurePosY = kingPosY + dir[0]
        newFigurePosX = kingPosX + dir[1]
        if newFigurePosY < 0 or newFigurePosY >= 8 or newFigurePosX < 0 or newFigurePosX >= 8:
            continue
        isKnightAttacking = table[newFigurePosY][newFigurePosX] == turn * BLACK_KING
        if isKnightAttacking:
            return True
    return False
            

def getPotentialMoveFromPos(table: np.ndarray, pos: tuple[int, int]):
    figureNum = table[pos[0]][pos[1]]
    potMoveFunc = figurePotMoveDict[figureNum]
    return potMoveFunc(table, pos)
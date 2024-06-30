import numpy as np
from constants import *

allPotentialMoves = {}

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
    '''
    get potential moves for king
    '''
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
    '''
    get potential moves for rook
    '''
    return lineFigurePotentialMoves(table, pos, ((-1, 0), (0, 1), (1, 0), (0, -1)))

def bishopPotentialMoves(table: np.ndarray, pos: tuple[int, int]):
    '''
    get potential moves for bishop
    '''
    return lineFigurePotentialMoves(table, pos, ((-1, -1), (-1, 1), (1, 1), (1, -1)))

def queenPotentialMoves(table: np.ndarray, pos: tuple[int, int]):
    '''
    get potential moves for queen
    '''
    return lineFigurePotentialMoves(table, pos, ((-1, -1), (-1, 1), (1, 1), (1, -1), (-1, 0), (0, 1), (1, 0), (0, -1)))

def knightPotentialMoves(table: np.ndarray, pos: tuple[int, int]):
    '''
    get potential moves for knight
    '''
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
    '''
    get potential moves for pawn when capturing pieces
    '''
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
    '''
    get potential moves for pawn
    '''
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
    BLACK_KING:     kingPotentialMoves,
    BLACK_QUEEN:    queenPotentialMoves,
    BLACK_ROOK:     rookPotentialMoves,
    BLACK_BISHOP:   bishopPotentialMoves,
    BLACK_KNIGHT:   knightPotentialMoves,
    BLACK_PAWN:     pawnPotentialMoves,
    WHITE_PAWN:     pawnPotentialMoves,
    WHITE_KNIGHT:   knightPotentialMoves,
    WHITE_BISHOP:   bishopPotentialMoves,
    WHITE_ROOK:     rookPotentialMoves,
    WHITE_QUEEN:    queenPotentialMoves,
    WHITE_KING:     kingPotentialMoves
}

def isCheck(table: np.ndarray, turn: int):
    '''
    is check
    '''
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
    directions = ((-1, -1), (-1, 1))
    if turn == -1:
        directions = ((1, -1), (1, 1))
    for dir in directions:
        # ! set for all directions
        newFigurePosY = kingPosY + dir[0]
        newFigurePosX = kingPosX + dir[1]
        if newFigurePosY < 0 or newFigurePosY >= 8 or newFigurePosX < 0 or newFigurePosX >= 8:
            continue
        isPawnAttacking = table[newFigurePosY][newFigurePosX] == turn * BLACK_PAWN
        if isPawnAttacking:
            return True
    

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
            if fieldFig != 0:
                break
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
            if fieldFig != 0:
                break
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
    '''
    get potential moves based on table pos
    '''
    figureNum = table[pos[0]][pos[1]]
    potMoveFunc = figurePotMoveDict[figureNum]
    return potMoveFunc(table, pos)

def getAllPotentialMoves(table: np.ndarray, turn: int):
    '''
    get all potential moves for table 
    '''
    allMove = []
    for i in range(8):
        for j in range(8):
            if(table[i][j] * turn > 0):
                pos = (i, j)
                moves = getPotentialMoveFromPos(table, pos)
                if len(moves) > 0:
                    allMove.append({"pos": pos, "moves": moves })
    return allMove

def getAllPotentialMovesArray(table: np.ndarray, turn: int):
    '''
    get all potential moves for table, used in search algo (minimax) 
    '''
    allMove = []
    for i in range(8):
        for j in range(8):
            if(table[i][j] * turn > 0):
                pos = (i, j)
                moves = getPotentialMoveFromPos(table, pos)
                if len(moves) > 0:
                    if table[pos] == 1 and pos[0] == 1:
                        for move in moves:
                            allMove.append({"pos": (i, j), "move": move, "figure": 2  })
                            allMove.append({"pos": (i, j), "move": move, "figure": 3  })
                            allMove.append({"pos": (i, j), "move": move, "figure": 5  })
                            allMove.append({"pos": (i, j), "move": move, "figure": 9  })
                        continue
                    elif table[pos] == -1 and pos[0] == 6:
                        for move in moves:
                            allMove.append({"pos": (i, j), "move": move, "figure": -2  })
                            allMove.append({"pos": (i, j), "move": move, "figure": -3  })
                            allMove.append({"pos": (i, j), "move": move, "figure": -5  })
                            allMove.append({"pos": (i, j), "move": move, "figure": -9  })

                        continue
                    for move in moves:
                        allMove.append({"pos": pos, "move": move, "figure": table[pos] })
    return allMove
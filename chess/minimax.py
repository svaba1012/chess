

def minimax(table, evalTable, getPotentialMoves, turn, makeMove, depth, isEnd):
    '''
    get (bestScore, bestMove) for ai given:
        - table
        - evalTable - function for score calculating fanction based on table state
        - getPotentialMoves - function for get all potential moves based on 
                                table state
        - turn - 1-white1  -1-black
        - makeMove - function for making new table given table and move (applies 
                        move on table and save it to copy of table)
        - depth - depth of search tree
        - isEnd - function for checking is end of the game:
                    - 0 - game not over
                    - 1 - white wins
                    - -1 - black wins
                    - 2 - stalemate, draw
    '''    
    potMoves = getPotentialMoves(table, turn)
    winner = isEnd(table, potMoves, turn)
    if winner != 0:
        if winner == 2:
            return (0, None)
        return (winner * 100000.0, None)
    bestMove = None
    bestScore = None
    for move in potMoves:
        newTable = makeMove(table, move)
        if depth > 1:
            (score, oldMove) = minimax(newTable, evalTable, getPotentialMoves, -turn, makeMove, depth - 1, isEnd)
        else: 
            score = evalTable(newTable, turn)
        if bestScore == None:
            bestScore = score
            bestMove = move
            continue
        if turn == 1:
            if bestScore < score:
                bestScore = score
                bestMove = move
        else:
            if bestScore > score:
                bestScore = score
                bestMove = move
    return (bestScore, bestMove)

        

#program to solve 8 queens problem

global N 
N = 8

def printSolution(board):
    for i in range(N): 
        for j in range(N):
            if(board[i][j] == 1):
                print('Q', end = ' ')
            else:
                print('_', end = ' ') 
        print()

def isSafe(board, row, col):
    for i in range(col): 
        if board[row][i] == 1: 
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)): 
        if board[i][j] == 1: 
            return False
    for i, j in zip(range(row, N, 1), range(col, -1, -1)): 
        if board[i][j] == 1: 
            return False
    return True
  
def queenSolve(board, col):

    if col >= N:
        return True

    for i in range(N):
        if isSafe(board, i, col):
            board[i][col] = 1
            if queenSolve(board, col + 1) == True: 
                return True
            board[i][col] = 0

    return False

board = [[0 for i in range(N)] for j in range(N)]
queenSolve(board, 0)
printSolution(board)

'''OUTPUT:

Q _ _ _ _ _ _ _ 
_ _ _ _ _ _ Q _ 
_ _ _ _ Q _ _ _ 
_ _ _ _ _ _ _ Q 
_ Q _ _ _ _ _ _ 
_ _ _ Q _ _ _ _ 
_ _ _ _ _ Q _ _ 
_ _ Q _ _ _ _ _ 

'''

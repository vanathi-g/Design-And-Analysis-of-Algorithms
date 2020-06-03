
global N 
N = 8

k = 0

def printSolution(board):
    global k
    k+=1
    print("Solution",k,":")
    for i in range(N): 
        for j in range(N):
            if(board[i][j] == 1):
                print('Q', end = ' ')
            else:
                print('_', end = ' ') 
        print()
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
      
    if col == N:
        printSolution(board)
        return True

    res = False
    for i in range(N): 
        if (isSafe(board, i, col)):
            board[i][col] = 1;  
            res = queenSolve(board, col + 1) or res;
            board[i][col] = 0

    return res

board = [[0 for i in range(N)] for j in range(N)]
queenSolve(board, 0)

print("Total number of solutions = ", k)

'''OUTPUT:

Solution 1 :
Q _ _ _ _ _ _ _ 
_ _ _ _ _ _ Q _ 
_ _ _ _ Q _ _ _ 
_ _ _ _ _ _ _ Q 
_ Q _ _ _ _ _ _ 
_ _ _ Q _ _ _ _ 
_ _ _ _ _ Q _ _ 
_ _ Q _ _ _ _ _ 

Solution 2 :
Q _ _ _ _ _ _ _ 
_ _ _ _ _ _ Q _ 
_ _ _ Q _ _ _ _ 
_ _ _ _ _ Q _ _ 
_ _ _ _ _ _ _ Q 
_ Q _ _ _ _ _ _ 
_ _ _ _ Q _ _ _ 
_ _ Q _ _ _ _ _ 

Solution 3 :
Q _ _ _ _ _ _ _ 
_ _ _ _ _ Q _ _ 
_ _ _ _ _ _ _ Q 
_ _ Q _ _ _ _ _ 
_ _ _ _ _ _ Q _ 
_ _ _ Q _ _ _ _ 
_ Q _ _ _ _ _ _ 
_ _ _ _ Q _ _ _ 

Solution 4 :
Q _ _ _ _ _ _ _ 
_ _ _ _ Q _ _ _ 
_ _ _ _ _ _ _ Q 
_ _ _ _ _ Q _ _ 
_ _ Q _ _ _ _ _ 
_ _ _ _ _ _ Q _ 
_ Q _ _ _ _ _ _ 
_ _ _ Q _ _ _ _ 

Solution 5 :
_ _ _ _ _ Q _ _ 
Q _ _ _ _ _ _ _ 
_ _ _ _ Q _ _ _ 
_ Q _ _ _ _ _ _ 
_ _ _ _ _ _ _ Q 
_ _ Q _ _ _ _ _ 
_ _ _ _ _ _ Q _ 
_ _ _ Q _ _ _ _ 

Solution 6 :
_ _ _ Q _ _ _ _ 
Q _ _ _ _ _ _ _ 
_ _ _ _ Q _ _ _ 
_ _ _ _ _ _ _ Q 
_ Q _ _ _ _ _ _ 
_ _ _ _ _ _ Q _ 
_ _ Q _ _ _ _ _ 
_ _ _ _ _ Q _ _ 

Solution 7 :
_ _ _ _ Q _ _ _ 
Q _ _ _ _ _ _ _ 
_ _ _ _ _ _ _ Q 
_ _ _ Q _ _ _ _ 
_ Q _ _ _ _ _ _ 
_ _ _ _ _ _ Q _ 
_ _ Q _ _ _ _ _ 
_ _ _ _ _ Q _ _ 

Solution 8 :
_ _ Q _ _ _ _ _ 
Q _ _ _ _ _ _ _ 
_ _ _ _ _ _ Q _ 
_ _ _ _ Q _ _ _ 
_ _ _ _ _ _ _ Q 
_ Q _ _ _ _ _ _ 
_ _ _ Q _ _ _ _ 
_ _ _ _ _ Q _ _ 

Solution 9 :
_ _ _ _ Q _ _ _ 
Q _ _ _ _ _ _ _ 
_ _ _ Q _ _ _ _ 
_ _ _ _ _ Q _ _ 
_ _ _ _ _ _ _ Q 
_ Q _ _ _ _ _ _ 
_ _ _ _ _ _ Q _ 
_ _ Q _ _ _ _ _ 

Solution 10 :
_ _ _ _ _ _ Q _ 
Q _ _ _ _ _ _ _ 
_ _ Q _ _ _ _ _ 
_ _ _ _ _ _ _ Q 
_ _ _ _ _ Q _ _ 
_ _ _ Q _ _ _ _ 
_ Q _ _ _ _ _ _ 
_ _ _ _ Q _ _ _ 

Solution 11 :
_ _ _ _ Q _ _ _ 
Q _ _ _ _ _ _ _ 
_ _ _ _ _ _ _ Q 
_ _ _ _ _ Q _ _ 
_ _ Q _ _ _ _ _ 
_ _ _ _ _ _ Q _ 
_ Q _ _ _ _ _ _ 
_ _ _ Q _ _ _ _ 

Solution 12 :
_ _ _ Q _ _ _ _ 
Q _ _ _ _ _ _ _ 
_ _ _ _ Q _ _ _ 
_ _ _ _ _ _ _ Q 
_ _ _ _ _ Q _ _ 
_ _ Q _ _ _ _ _ 
_ _ _ _ _ _ Q _ 
_ Q _ _ _ _ _ _ 

Solution 13 :
_ Q _ _ _ _ _ _ 
_ _ _ _ _ Q _ _ 
Q _ _ _ _ _ _ _ 
_ _ _ _ _ _ Q _ 
_ _ _ Q _ _ _ _ 
_ _ _ _ _ _ _ Q 
_ _ Q _ _ _ _ _ 
_ _ _ _ Q _ _ _ 

Solution 14 :
_ _ _ _ Q _ _ _ 
_ _ Q _ _ _ _ _ 
Q _ _ _ _ _ _ _ 
_ _ _ _ _ _ Q _ 
_ Q _ _ _ _ _ _ 
_ _ _ _ _ _ _ Q 
_ _ _ _ _ Q _ _ 
_ _ _ Q _ _ _ _ 

Solution 15 :
_ _ _ _ _ _ _ Q 
_ _ Q _ _ _ _ _ 
Q _ _ _ _ _ _ _ 
_ _ _ _ _ Q _ _ 
_ Q _ _ _ _ _ _ 
_ _ _ _ Q _ _ _ 
_ _ _ _ _ _ Q _ 
_ _ _ Q _ _ _ _ 

Solution 16 :
_ _ _ Q _ _ _ _ 
_ _ _ _ _ Q _ _ 
Q _ _ _ _ _ _ _ 
_ _ _ _ Q _ _ _ 
_ Q _ _ _ _ _ _ 
_ _ _ _ _ _ _ Q 
_ _ Q _ _ _ _ _ 
_ _ _ _ _ _ Q _ 

Solution 17 :
_ _ _ _ Q _ _ _ 
_ _ _ _ _ _ Q _ 
Q _ _ _ _ _ _ _ 
_ _ _ Q _ _ _ _ 
_ Q _ _ _ _ _ _ 
_ _ _ _ _ _ _ Q 
_ _ _ _ _ Q _ _ 
_ _ Q _ _ _ _ _ 

Solution 18 :
_ _ _ _ _ Q _ _ 
_ _ Q _ _ _ _ _ 
Q _ _ _ _ _ _ _ 
_ _ _ _ _ _ _ Q 
_ _ _ Q _ _ _ _ 
_ Q _ _ _ _ _ _ 
_ _ _ _ _ _ Q _ 
_ _ _ _ Q _ _ _ 

Solution 19 :
_ _ _ _ Q _ _ _ 
_ _ Q _ _ _ _ _ 
Q _ _ _ _ _ _ _ 
_ _ _ _ _ Q _ _ 
_ _ _ _ _ _ _ Q 
_ Q _ _ _ _ _ _ 
_ _ _ Q _ _ _ _ 
_ _ _ _ _ _ Q _ 

Solution 20 :
_ _ _ _ _ Q _ _ 
_ _ Q _ _ _ _ _ 
Q _ _ _ _ _ _ _ 
_ _ _ _ _ _ _ Q 
_ _ _ _ Q _ _ _ 
_ Q _ _ _ _ _ _ 
_ _ _ Q _ _ _ _ 
_ _ _ _ _ _ Q _ 

Solution 21 :
_ _ _ Q _ _ _ _ 
_ _ _ _ _ _ _ Q 
Q _ _ _ _ _ _ _ 
_ _ Q _ _ _ _ _ 
_ _ _ _ _ Q _ _ 
_ Q _ _ _ _ _ _ 
_ _ _ _ _ _ Q _ 
_ _ _ _ Q _ _ _ 

Solution 22 :
_ _ _ _ _ _ _ Q 
_ _ _ Q _ _ _ _ 
Q _ _ _ _ _ _ _ 
_ _ Q _ _ _ _ _ 
_ _ _ _ _ Q _ _ 
_ Q _ _ _ _ _ _ 
_ _ _ _ _ _ Q _ 
_ _ _ _ Q _ _ _ 

Solution 23 :
_ _ _ Q _ _ _ _ 
_ _ _ _ _ _ _ Q 
Q _ _ _ _ _ _ _ 
_ _ _ _ Q _ _ _ 
_ _ _ _ _ _ Q _ 
_ Q _ _ _ _ _ _ 
_ _ _ _ _ Q _ _ 
_ _ Q _ _ _ _ _ 

Solution 24 :
_ _ _ Q _ _ _ _ 
_ _ _ _ _ _ Q _ 
Q _ _ _ _ _ _ _ 
_ _ _ _ _ _ _ Q 
_ _ _ _ Q _ _ _ 
_ Q _ _ _ _ _ _ 
_ _ _ _ _ Q _ _ 
_ _ Q _ _ _ _ _ 

Solution 25 :
_ _ _ _ _ Q _ _ 
_ _ _ Q _ _ _ _ 
Q _ _ _ _ _ _ _ 
_ _ _ _ Q _ _ _ 
_ _ _ _ _ _ _ Q 
_ Q _ _ _ _ _ _ 
_ _ _ _ _ _ Q _ 
_ _ Q _ _ _ _ _ 

Solution 26 :
_ _ _ _ _ Q _ _ 
_ _ Q _ _ _ _ _ 
Q _ _ _ _ _ _ _ 
_ _ _ _ _ _ Q _ 
_ _ _ _ Q _ _ _ 
_ _ _ _ _ _ _ Q 
_ Q _ _ _ _ _ _ 
_ _ _ Q _ _ _ _ 

Solution 27 :
_ _ _ _ _ _ Q _ 
_ _ Q _ _ _ _ _ 
Q _ _ _ _ _ _ _ 
_ _ _ _ _ Q _ _ 
_ _ _ _ _ _ _ Q 
_ _ _ _ Q _ _ _ 
_ Q _ _ _ _ _ _ 
_ _ _ Q _ _ _ _ 

Solution 28 :
_ _ _ _ Q _ _ _ 
_ _ _ _ _ _ Q _ 
Q _ _ _ _ _ _ _ 
_ _ Q _ _ _ _ _ 
_ _ _ _ _ _ _ Q 
_ _ _ _ _ Q _ _ 
_ _ _ Q _ _ _ _ 
_ Q _ _ _ _ _ _ 

Solution 29 :
_ Q _ _ _ _ _ _ 
_ _ _ _ Q _ _ _ 
_ _ _ _ _ _ Q _ 
Q _ _ _ _ _ _ _ 
_ _ Q _ _ _ _ _ 
_ _ _ _ _ _ _ Q 
_ _ _ _ _ Q _ _ 
_ _ _ Q _ _ _ _ 

Solution 30 :
_ Q _ _ _ _ _ _ 
_ _ _ _ _ _ _ Q 
_ _ _ _ _ Q _ _ 
Q _ _ _ _ _ _ _ 
_ _ Q _ _ _ _ _ 
_ _ _ _ Q _ _ _ 
_ _ _ _ _ _ Q _ 
_ _ _ Q _ _ _ _ 

Solution 31 :
_ _ _ _ _ Q _ _ 
_ Q _ _ _ _ _ _ 
_ _ _ _ _ _ Q _ 
Q _ _ _ _ _ _ _ 
_ _ Q _ _ _ _ _ 
_ _ _ _ Q _ _ _ 
_ _ _ _ _ _ _ Q 
_ _ _ Q _ _ _ _ 

Solution 32 :
_ _ _ _ _ _ Q _ 
_ Q _ _ _ _ _ _ 
_ _ _ Q _ _ _ _ 
Q _ _ _ _ _ _ _ 
_ _ _ _ _ _ _ Q 
_ _ _ _ Q _ _ _ 
_ _ Q _ _ _ _ _ 
_ _ _ _ _ Q _ _ 

Solution 33 :
_ _ _ _ _ _ _ Q 
_ Q _ _ _ _ _ _ 
_ _ _ Q _ _ _ _ 
Q _ _ _ _ _ _ _ 
_ _ _ _ _ _ Q _ 
_ _ _ _ Q _ _ _ 
_ _ Q _ _ _ _ _ 
_ _ _ _ _ Q _ _ 

Solution 34 :
_ _ _ _ Q _ _ _ 
_ Q _ _ _ _ _ _ 
_ _ _ _ _ _ _ Q 
Q _ _ _ _ _ _ _ 
_ _ _ Q _ _ _ _ 
_ _ _ _ _ _ Q _ 
_ _ Q _ _ _ _ _ 
_ _ _ _ _ Q _ _ 

Solution 35 :
_ _ _ _ _ Q _ _ 
_ Q _ _ _ _ _ _ 
_ _ _ _ _ _ Q _ 
Q _ _ _ _ _ _ _ 
_ _ _ Q _ _ _ _ 
_ _ _ _ _ _ _ Q 
_ _ _ _ Q _ _ _ 
_ _ Q _ _ _ _ _ 

Solution 36 :
_ _ _ _ Q _ _ _ 
_ Q _ _ _ _ _ _ 
_ _ _ _ _ Q _ _ 
Q _ _ _ _ _ _ _ 
_ _ _ _ _ _ Q _ 
_ _ _ Q _ _ _ _ 
_ _ _ _ _ _ _ Q 
_ _ Q _ _ _ _ _ 

Solution 37 :
_ _ Q _ _ _ _ _ 
_ _ _ _ Q _ _ _ 
_ _ _ _ _ _ Q _ 
Q _ _ _ _ _ _ _ 
_ _ _ Q _ _ _ _ 
_ Q _ _ _ _ _ _ 
_ _ _ _ _ _ _ Q 
_ _ _ _ _ Q _ _ 

Solution 38 :
_ _ _ _ _ Q _ _ 
_ _ _ Q _ _ _ _ 
_ _ _ _ _ _ Q _ 
Q _ _ _ _ _ _ _ 
_ _ _ _ _ _ _ Q 
_ Q _ _ _ _ _ _ 
_ _ _ _ Q _ _ _ 
_ _ Q _ _ _ _ _ 

Solution 39 :
_ _ _ _ Q _ _ _ 
_ _ _ _ _ _ _ Q 
_ _ _ Q _ _ _ _ 
Q _ _ _ _ _ _ _ 
_ _ _ _ _ _ Q _ 
_ Q _ _ _ _ _ _ 
_ _ _ _ _ Q _ _ 
_ _ Q _ _ _ _ _ 

Solution 40 :
_ _ Q _ _ _ _ _ 
_ _ _ _ _ Q _ _ 
_ _ _ _ _ _ _ Q 
Q _ _ _ _ _ _ _ 
_ _ _ _ Q _ _ _ 
_ _ _ _ _ _ Q _ 
_ Q _ _ _ _ _ _ 
_ _ _ Q _ _ _ _ 

Solution 41 :
_ _ _ _ _ _ Q _ 
_ _ _ _ Q _ _ _ 
_ _ Q _ _ _ _ _ 
Q _ _ _ _ _ _ _ 
_ _ _ _ _ Q _ _ 
_ _ _ _ _ _ _ Q 
_ Q _ _ _ _ _ _ 
_ _ _ Q _ _ _ _ 

Solution 42 :
_ _ _ _ _ Q _ _ 
_ _ _ Q _ _ _ _ 
_ _ _ _ _ _ Q _ 
Q _ _ _ _ _ _ _ 
_ _ Q _ _ _ _ _ 
_ _ _ _ Q _ _ _ 
_ Q _ _ _ _ _ _ 
_ _ _ _ _ _ _ Q 

Solution 43 :
_ _ _ _ Q _ _ _ 
_ _ _ _ _ _ _ Q 
_ _ _ Q _ _ _ _ 
Q _ _ _ _ _ _ _ 
_ _ Q _ _ _ _ _ 
_ _ _ _ _ Q _ _ 
_ Q _ _ _ _ _ _ 
_ _ _ _ _ _ Q _ 

Solution 44 :
_ _ Q _ _ _ _ _ 
_ _ _ _ _ Q _ _ 
_ _ _ Q _ _ _ _ 
Q _ _ _ _ _ _ _ 
_ _ _ _ _ _ _ Q 
_ _ _ _ Q _ _ _ 
_ _ _ _ _ _ Q _ 
_ Q _ _ _ _ _ _ 

Solution 45 :
_ _ Q _ _ _ _ _ 
_ _ _ _ _ Q _ _ 
_ _ _ _ _ _ _ Q 
Q _ _ _ _ _ _ _ 
_ _ _ Q _ _ _ _ 
_ _ _ _ _ _ Q _ 
_ _ _ _ Q _ _ _ 
_ Q _ _ _ _ _ _ 

Solution 46 :
_ _ _ _ Q _ _ _ 
_ _ _ _ _ _ Q _ 
_ _ _ Q _ _ _ _ 
Q _ _ _ _ _ _ _ 
_ _ Q _ _ _ _ _ 
_ _ _ _ _ _ _ Q 
_ _ _ _ _ Q _ _ 
_ Q _ _ _ _ _ _ 

Solution 47 :
_ Q _ _ _ _ _ _ 
_ _ _ _ _ Q _ _ 
_ _ _ _ _ _ _ Q 
_ _ Q _ _ _ _ _ 
Q _ _ _ _ _ _ _ 
_ _ _ Q _ _ _ _ 
_ _ _ _ _ _ Q _ 
_ _ _ _ Q _ _ _ 

Solution 48 :
_ Q _ _ _ _ _ _ 
_ _ _ _ Q _ _ _ 
_ _ _ _ _ _ Q _ 
_ _ _ Q _ _ _ _ 
Q _ _ _ _ _ _ _ 
_ _ _ _ _ _ _ Q 
_ _ _ _ _ Q _ _ 
_ _ Q _ _ _ _ _ 

Solution 49 :
_ Q _ _ _ _ _ _ 
_ _ _ _ _ _ Q _ 
_ _ _ _ Q _ _ _ 
_ _ _ _ _ _ _ Q 
Q _ _ _ _ _ _ _ 
_ _ _ Q _ _ _ _ 
_ _ _ _ _ Q _ _ 
_ _ Q _ _ _ _ _ 

Solution 50 :
_ _ _ _ _ _ Q _ 
_ Q _ _ _ _ _ _ 
_ _ _ _ _ Q _ _ 
_ _ Q _ _ _ _ _ 
Q _ _ _ _ _ _ _ 
_ _ _ Q _ _ _ _ 
_ _ _ _ _ _ _ Q 
_ _ _ _ Q _ _ _ 

Solution 51 :
_ _ _ _ _ _ _ Q 
_ Q _ _ _ _ _ _ 
_ _ _ _ Q _ _ _ 
_ _ Q _ _ _ _ _ 
Q _ _ _ _ _ _ _ 
_ _ _ _ _ _ Q _ 
_ _ _ Q _ _ _ _ 
_ _ _ _ _ Q _ _ 

Solution 52 :
_ _ _ Q _ _ _ _ 
_ Q _ _ _ _ _ _ 
_ _ _ _ _ _ _ Q 
_ _ _ _ _ Q _ _ 
Q _ _ _ _ _ _ _ 
_ _ Q _ _ _ _ _ 
_ _ _ _ Q _ _ _ 
_ _ _ _ _ _ Q _ 

Solution 53 :
_ _ _ Q _ _ _ _ 
_ Q _ _ _ _ _ _ 
_ _ _ _ _ _ Q _ 
_ _ _ _ Q _ _ _ 
Q _ _ _ _ _ _ _ 
_ _ _ _ _ _ _ Q 
_ _ _ _ _ Q _ _ 
_ _ Q _ _ _ _ _ 

Solution 54 :
_ _ Q _ _ _ _ _ 
_ _ _ _ _ Q _ _ 
_ Q _ _ _ _ _ _ 
_ _ _ _ _ _ Q _ 
Q _ _ _ _ _ _ _ 
_ _ _ Q _ _ _ _ 
_ _ _ _ _ _ _ Q 
_ _ _ _ Q _ _ _ 

Solution 55 :
_ _ Q _ _ _ _ _ 
_ _ _ _ Q _ _ _ 
_ Q _ _ _ _ _ _ 
_ _ _ _ _ _ _ Q 
Q _ _ _ _ _ _ _ 
_ _ _ _ _ _ Q _ 
_ _ _ Q _ _ _ _ 
_ _ _ _ _ Q _ _ 

Solution 56 :
_ _ _ _ _ Q _ _ 
_ _ _ _ _ _ _ Q 
_ Q _ _ _ _ _ _ 
_ _ _ Q _ _ _ _ 
Q _ _ _ _ _ _ _ 
_ _ _ _ _ _ Q _ 
_ _ _ _ Q _ _ _ 
_ _ Q _ _ _ _ _ 

Solution 57 :
_ _ Q _ _ _ _ _ 
_ _ _ _ _ _ _ Q 
_ _ _ Q _ _ _ _ 
_ _ _ _ _ _ Q _ 
Q _ _ _ _ _ _ _ 
_ _ _ _ _ Q _ _ 
_ Q _ _ _ _ _ _ 
_ _ _ _ Q _ _ _ 

Solution 58 :
_ _ Q _ _ _ _ _ 
_ _ _ _ Q _ _ _ 
_ _ _ _ _ _ _ Q 
_ _ _ Q _ _ _ _ 
Q _ _ _ _ _ _ _ 
_ _ _ _ _ _ Q _ 
_ Q _ _ _ _ _ _ 
_ _ _ _ _ Q _ _ 

Solution 59 :
_ _ _ _ _ Q _ _ 
_ _ Q _ _ _ _ _ 
_ _ _ _ _ _ Q _ 
_ _ _ Q _ _ _ _ 
Q _ _ _ _ _ _ _ 
_ _ _ _ _ _ _ Q 
_ Q _ _ _ _ _ _ 
_ _ _ _ Q _ _ _ 

Solution 60 :
_ _ _ _ _ Q _ _ 
_ _ Q _ _ _ _ _ 
_ _ _ _ Q _ _ _ 
_ _ _ _ _ _ Q _ 
Q _ _ _ _ _ _ _ 
_ _ _ Q _ _ _ _ 
_ Q _ _ _ _ _ _ 
_ _ _ _ _ _ _ Q 

Solution 61 :
_ _ _ _ _ Q _ _ 
_ _ Q _ _ _ _ _ 
_ _ _ _ Q _ _ _ 
_ _ _ _ _ _ _ Q 
Q _ _ _ _ _ _ _ 
_ _ _ Q _ _ _ _ 
_ Q _ _ _ _ _ _ 
_ _ _ _ _ _ Q _ 

Solution 62 :
_ _ _ Q _ _ _ _ 
_ _ _ _ _ _ _ Q 
_ _ _ _ Q _ _ _ 
_ _ Q _ _ _ _ _ 
Q _ _ _ _ _ _ _ 
_ _ _ _ _ _ Q _ 
_ Q _ _ _ _ _ _ 
_ _ _ _ _ Q _ _ 

Solution 63 :
_ _ _ Q _ _ _ _ 
_ _ _ _ _ _ Q _ 
_ _ _ _ Q _ _ _ 
_ _ Q _ _ _ _ _ 
Q _ _ _ _ _ _ _ 
_ _ _ _ _ Q _ _ 
_ _ _ _ _ _ _ Q 
_ Q _ _ _ _ _ _ 

Solution 64 :
_ _ _ Q _ _ _ _ 
_ _ _ _ _ Q _ _ 
_ _ _ _ _ _ _ Q 
_ _ Q _ _ _ _ _ 
Q _ _ _ _ _ _ _ 
_ _ _ _ _ _ Q _ 
_ _ _ _ Q _ _ _ 
_ Q _ _ _ _ _ _ 

Solution 65 :
_ Q _ _ _ _ _ _ 
_ _ _ Q _ _ _ _ 
_ _ _ _ _ Q _ _ 
_ _ _ _ _ _ _ Q 
_ _ Q _ _ _ _ _ 
Q _ _ _ _ _ _ _ 
_ _ _ _ _ _ Q _ 
_ _ _ _ Q _ _ _ 

Solution 66 :
_ _ _ Q _ _ _ _ 
_ Q _ _ _ _ _ _ 
_ _ _ _ Q _ _ _ 
_ _ _ _ _ _ _ Q 
_ _ _ _ _ Q _ _ 
Q _ _ _ _ _ _ _ 
_ _ Q _ _ _ _ _ 
_ _ _ _ _ _ Q _ 

Solution 67 :
_ _ _ Q _ _ _ _ 
_ Q _ _ _ _ _ _ 
_ _ _ _ _ _ _ Q 
_ _ _ _ Q _ _ _ 
_ _ _ _ _ _ Q _ 
Q _ _ _ _ _ _ _ 
_ _ Q _ _ _ _ _ 
_ _ _ _ _ Q _ _ 

Solution 68 :
_ _ Q _ _ _ _ _ 
_ _ _ _ _ _ Q _ 
_ Q _ _ _ _ _ _ 
_ _ _ _ _ _ _ Q 
_ _ _ _ Q _ _ _ 
Q _ _ _ _ _ _ _ 
_ _ _ Q _ _ _ _ 
_ _ _ _ _ Q _ _ 

Solution 69 :
_ _ Q _ _ _ _ _ 
_ _ _ _ _ Q _ _ 
_ Q _ _ _ _ _ _ 
_ _ _ _ Q _ _ _ 
_ _ _ _ _ _ _ Q 
Q _ _ _ _ _ _ _ 
_ _ _ _ _ _ Q _ 
_ _ _ Q _ _ _ _ 

Solution 70 :
_ _ Q _ _ _ _ _ 
_ _ _ _ _ Q _ _ 
_ Q _ _ _ _ _ _ 
_ _ _ _ _ _ Q _ 
_ _ _ _ Q _ _ _ 
Q _ _ _ _ _ _ _ 
_ _ _ _ _ _ _ Q 
_ _ _ Q _ _ _ _ 

Solution 71 :
_ _ _ _ Q _ _ _ 
_ _ _ _ _ _ Q _ 
_ Q _ _ _ _ _ _ 
_ _ _ _ _ Q _ _ 
_ _ Q _ _ _ _ _ 
Q _ _ _ _ _ _ _ 
_ _ _ Q _ _ _ _ 
_ _ _ _ _ _ _ Q 

Solution 72 :
_ _ _ _ Q _ _ _ 
_ _ _ _ _ _ Q _ 
_ Q _ _ _ _ _ _ 
_ _ _ _ _ Q _ _ 
_ _ Q _ _ _ _ _ 
Q _ _ _ _ _ _ _ 
_ _ _ _ _ _ _ Q 
_ _ _ Q _ _ _ _ 

Solution 73 :
_ _ _ _ _ _ Q _ 
_ _ _ Q _ _ _ _ 
_ Q _ _ _ _ _ _ 
_ _ _ _ Q _ _ _ 
_ _ _ _ _ _ _ Q 
Q _ _ _ _ _ _ _ 
_ _ Q _ _ _ _ _ 
_ _ _ _ _ Q _ _ 

Solution 74 :
_ _ _ _ _ _ Q _ 
_ _ _ Q _ _ _ _ 
_ Q _ _ _ _ _ _ 
_ _ _ _ _ _ _ Q 
_ _ _ _ _ Q _ _ 
Q _ _ _ _ _ _ _ 
_ _ Q _ _ _ _ _ 
_ _ _ _ Q _ _ _ 

Solution 75 :
_ _ _ _ Q _ _ _ 
_ _ _ _ _ _ Q _ 
_ Q _ _ _ _ _ _ 
_ _ _ Q _ _ _ _ 
_ _ _ _ _ _ _ Q 
Q _ _ _ _ _ _ _ 
_ _ Q _ _ _ _ _ 
_ _ _ _ _ Q _ _ 

Solution 76 :
_ _ Q _ _ _ _ _ 
_ _ _ _ _ Q _ _ 
_ _ _ _ _ _ _ Q 
_ Q _ _ _ _ _ _ 
_ _ _ Q _ _ _ _ 
Q _ _ _ _ _ _ _ 
_ _ _ _ _ _ Q _ 
_ _ _ _ Q _ _ _ 

Solution 77 :
_ _ _ _ _ _ Q _ 
_ _ Q _ _ _ _ _ 
_ _ _ _ _ _ _ Q 
_ Q _ _ _ _ _ _ 
_ _ _ _ Q _ _ _ 
Q _ _ _ _ _ _ _ 
_ _ _ _ _ Q _ _ 
_ _ _ Q _ _ _ _ 

Solution 78 :
_ _ _ Q _ _ _ _ 
_ _ _ _ _ _ Q _ 
_ _ _ _ Q _ _ _ 
_ Q _ _ _ _ _ _ 
_ _ _ _ _ Q _ _ 
Q _ _ _ _ _ _ _ 
_ _ Q _ _ _ _ _ 
_ _ _ _ _ _ _ Q 

Solution 79 :
_ _ _ Q _ _ _ _ 
_ _ _ _ _ Q _ _ 
_ _ _ _ _ _ _ Q 
_ Q _ _ _ _ _ _ 
_ _ _ _ _ _ Q _ 
Q _ _ _ _ _ _ _ 
_ _ Q _ _ _ _ _ 
_ _ _ _ Q _ _ _ 

Solution 80 :
_ _ _ _ Q _ _ _ 
_ _ Q _ _ _ _ _ 
_ _ _ _ _ _ _ Q 
_ _ _ Q _ _ _ _ 
_ _ _ _ _ _ Q _ 
Q _ _ _ _ _ _ _ 
_ _ _ _ _ Q _ _ 
_ Q _ _ _ _ _ _ 

Solution 81 :
_ Q _ _ _ _ _ _ 
_ _ _ _ _ _ Q _ 
_ _ Q _ _ _ _ _ 
_ _ _ _ _ Q _ _ 
_ _ _ _ _ _ _ Q 
_ _ _ _ Q _ _ _ 
Q _ _ _ _ _ _ _ 
_ _ _ Q _ _ _ _ 

Solution 82 :
_ _ _ Q _ _ _ _ 
_ Q _ _ _ _ _ _ 
_ _ _ _ _ _ Q _ 
_ _ Q _ _ _ _ _ 
_ _ _ _ _ Q _ _ 
_ _ _ _ _ _ _ Q 
Q _ _ _ _ _ _ _ 
_ _ _ _ Q _ _ _ 

Solution 83 :
_ _ _ _ Q _ _ _ 
_ Q _ _ _ _ _ _ 
_ _ _ Q _ _ _ _ 
_ _ _ _ _ Q _ _ 
_ _ _ _ _ _ _ Q 
_ _ Q _ _ _ _ _ 
Q _ _ _ _ _ _ _ 
_ _ _ _ _ _ Q _ 

Solution 84 :
_ _ Q _ _ _ _ _ 
_ _ _ _ _ _ Q _ 
_ Q _ _ _ _ _ _ 
_ _ _ _ _ _ _ Q 
_ _ _ _ _ Q _ _ 
_ _ _ Q _ _ _ _ 
Q _ _ _ _ _ _ _ 
_ _ _ _ Q _ _ _ 

Solution 85 :
_ _ _ _ _ Q _ _ 
_ _ _ Q _ _ _ _ 
_ Q _ _ _ _ _ _ 
_ _ _ _ _ _ _ Q 
_ _ _ _ Q _ _ _ 
_ _ _ _ _ _ Q _ 
Q _ _ _ _ _ _ _ 
_ _ Q _ _ _ _ _ 

Solution 86 :
_ _ _ _ _ Q _ _ 
_ _ Q _ _ _ _ _ 
_ _ _ _ _ _ Q _ 
_ Q _ _ _ _ _ _ 
_ _ _ Q _ _ _ _ 
_ _ _ _ _ _ _ Q 
Q _ _ _ _ _ _ _ 
_ _ _ _ Q _ _ _ 

Solution 87 :
_ _ _ _ _ Q _ _ 
_ _ Q _ _ _ _ _ 
_ _ _ _ _ _ Q _ 
_ Q _ _ _ _ _ _ 
_ _ _ _ _ _ _ Q 
_ _ _ _ Q _ _ _ 
Q _ _ _ _ _ _ _ 
_ _ _ Q _ _ _ _ 

Solution 88 :
_ _ _ Q _ _ _ _ 
_ _ _ _ _ _ Q _ 
_ _ Q _ _ _ _ _ 
_ _ _ _ _ _ _ Q 
_ Q _ _ _ _ _ _ 
_ _ _ _ Q _ _ _ 
Q _ _ _ _ _ _ _ 
_ _ _ _ _ Q _ _ 

Solution 89 :
_ _ _ Q _ _ _ _ 
_ Q _ _ _ _ _ _ 
_ _ _ _ _ _ Q _ 
_ _ Q _ _ _ _ _ 
_ _ _ _ _ Q _ _ 
_ _ _ _ _ _ _ Q 
_ _ _ _ Q _ _ _ 
Q _ _ _ _ _ _ _ 

Solution 90 :
_ _ _ _ Q _ _ _ 
_ Q _ _ _ _ _ _ 
_ _ _ Q _ _ _ _ 
_ _ _ _ _ _ Q _ 
_ _ Q _ _ _ _ _ 
_ _ _ _ _ _ _ Q 
_ _ _ _ _ Q _ _ 
Q _ _ _ _ _ _ _ 

Solution 91 :
_ _ Q _ _ _ _ _ 
_ _ _ _ Q _ _ _ 
_ Q _ _ _ _ _ _ 
_ _ _ _ _ _ _ Q 
_ _ _ _ _ Q _ _ 
_ _ _ Q _ _ _ _ 
_ _ _ _ _ _ Q _ 
Q _ _ _ _ _ _ _ 

Solution 92 :
_ _ Q _ _ _ _ _ 
_ _ _ _ _ Q _ _ 
_ _ _ Q _ _ _ _ 
_ Q _ _ _ _ _ _ 
_ _ _ _ _ _ _ Q 
_ _ _ _ Q _ _ _ 
_ _ _ _ _ _ Q _ 
Q _ _ _ _ _ _ _ 

Total number of solutions =  92

'''
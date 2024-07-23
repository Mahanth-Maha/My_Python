import pandas as pd
import random 

def get_sudoku_board_from_Str( s: str):
        s = str(s)
        board = []
        if len(s) != 81:
            return None
        temp = []
        try:
            for i in s:
                temp.append(int(i))
                if len(temp) == 9:
                    board.append(temp)
                    temp = []
        except Exception:
            board = None
        finally:
            return board

def getSudoku():
    df = pd.read_csv('sudoku_500000_for_github.csv')
    question, solution = (df.loc[random.randint(0, df.shape[0])])
    qb = get_sudoku_board_from_Str(question)
    ab = get_sudoku_board_from_Str(solution)
    return qb, ab


def solveSudoku(board , verbose = False):
    rows = [[False for j in range(9)] for i in range(9) ]
    cols = [[False for j in range(9)] for i in range(9) ]
    boxes = [[False for j in range(9)] for i in range(9) ]
    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                rows[i][board[i][j] - 1] = True
                cols[j][board[i][j] - 1] = True
                boxes[3*(i//3) + (j//3)][board[i][j] - 1] = True
    
    def solver(board, rows, cols, boxes , verbose = False):
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    for value in range(1,10):
                        if not rows[i][value - 1] and not cols[j][value - 1] and not boxes[3*(i//3) + (j//3)][value - 1] :
                            board[i][j] = value
                            rows[i][value - 1] = cols[j][value - 1] = boxes[3*(i//3) + (j//3)][value - 1] = True
                            if verbose:
                                print("Solving... (Forward)")
                                printBoard(board)
                            if solver(board , rows, cols , boxes , verbose):
                                return True
                            else :
                                board[i][j] = 0
                                rows[i][value - 1] = cols[j][value - 1] = boxes[3*(i//3) + (j//3)][value - 1] = False
                                if verbose:
                                    print("Solving... (Backtrack)")
                                    printBoard(board)
                    return False
        return True
    
    solver(board, rows, cols, boxes , verbose)
    return board

def printBoard(board):
    for i in board:
        for j in i:
            if j == 0:
                print('_', end=' ')
            else :
                print(j, end=' ')
        print()
    print()

if __name__ == '__main__':
    q, a = getSudoku()
    print("Question board : ")
    printBoard(q)
    print("Solution board : ")
    printBoard(a)
    
    solveSudoku( q , verbose= True)
    # solveSudoku( q )
    
    if q == a:
        print("[+] Solved\n")
    else :
        print("[-] Not Solved\n")

    print("Final board : ")
    printBoard(q)

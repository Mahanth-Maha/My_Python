import pandas as pd
import random

df = pd.read_csv('sudoku.csv')
# df2 = df[:500000]
# df2.to_csv('sudoku_500000_for_github.csv')

def get_sudoku(self):
    question, solution = (df.loc[random.randint(0,df.shape[0])])
    qb = get_sudoku_board_from_Str(question)
    ab = get_sudoku_board_from_Str(solution)
    
def get_sudoku_board_from_Str(self, s :str):
    s = str(s)
    board = []
    if len(s) != 81 : 
        return None
    temp = []
    for i in s:
        temp.append(int(i))
        if len(temp) == 9:
            board.append(temp)
            temp = []
    return board
            


            


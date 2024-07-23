from SudokuGame import game
from time import sleep
import pygame


# SPEED_OF_ANIMATION = 0.025  # INV :: lower -> fast 
SPEED_OF_ANIMATION = 0.05 

class Visualization(game):
    def __init__(self, game_board=None, sol_board=None) -> None:
        super().__init__(game_board, sol_board)
        self.running = True
        self.clock = pygame.time.Clock()

    def run_visualization(self):
        board = self.get_board_from_Outside()
        self.solveSudoku(board)
        
    def solveSudoku(self , board):
        rows = [[False for j in range(9)] for i in range(9) ]
        cols = [[False for j in range(9)] for i in range(9) ]
        boxes = [[False for j in range(9)] for i in range(9) ]
        for i in range(9):
            for j in range(9):
                if board[i][j] != 0:
                    rows[i][board[i][j] - 1] = True
                    cols[j][board[i][j] - 1] = True
                    boxes[3*(i//3) + (j//3)][board[i][j] - 1] = True
        
        def solver(board, rows, cols, boxes):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            if not self.running:
                return False
            
            for i in range(9):
                for j in range(9):
                    if board[i][j] == 0:
                        for value in range(1,10):
                            if not rows[i][value - 1] and not cols[j][value - 1] and not boxes[3*(i//3) + (j//3)][value - 1] :
                                board[i][j] = value
                                rows[i][value - 1] = cols[j][value - 1] = boxes[3*(i//3) + (j//3)][value - 1] = True
                                self.set_board_from_Outside(board)
                                sleep(SPEED_OF_ANIMATION)
                                if solver(board , rows, cols , boxes):
                                    return True
                                else :
                                    board[i][j] = 0
                                    rows[i][value - 1] = cols[j][value - 1] = boxes[3*(i//3) + (j//3)][value - 1] = False
                                    self.set_board_from_Outside(board)
                                    sleep(SPEED_OF_ANIMATION)
                        return False
                    pygame.display.update()
            return True
        
        solver(board, rows, cols, boxes)
        return board

def main():
    pygame.init()
    visualization = Visualization()
    visualization.run_visualization()
    print('Done Solving !')
    try:
        n = int(input("Enter 1 to solve another :"))
        if(n == 1):
            pygame.quit()
            main()
    except :
        pygame.quit()
        
        
if __name__ == "__main__":
    main()
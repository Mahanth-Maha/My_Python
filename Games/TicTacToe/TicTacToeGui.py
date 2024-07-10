from time import sleep
import pygame
import numpy as np

pygame.init()
WIDTH, HEIGHT = 300, 300
LINE_WIDTH = 15
BOARD_ROWS, BOARD_COLS = 3, 3
SQ_SIZE = WIDTH // BOARD_COLS
CIRCLE_RADIUS = SQ_SIZE // 3
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = SQ_SIZE // 4
FONT = pygame.font.Font(pygame.font.get_default_font(), 48)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = RED
CROSS_COLOR = BLUE


class TicTacToe:
    def __init__(self):
        self.board = np.full((BOARD_ROWS, BOARD_COLS), None)
        self.current_player = "X"
        self.game_over = False
        self.draw = False
        self.game_on = False

    def mark_square(self, row, col, player):
        if self.board[row][col] is None:
            self.board[row][col] = player
            return True
        return False

    def is_board_full(self):
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                if self.board[row][col] is None:
                    return False
        return True

    def check_winner(self, player):
        for col in range(BOARD_COLS):
            if all([self.board[row][col] == player for row in range(BOARD_ROWS)]):
                return True

        for row in range(BOARD_ROWS):
            if all([self.board[row][col] == player for col in range(BOARD_COLS)]):
                return True

        if all([self.board[row][row] == player for row in range(BOARD_ROWS)]):
            return True

        if all([self.board[row][BOARD_ROWS - 1 - row] == player for row in range(BOARD_ROWS)]):
            return True

        return False

    def restart(self):
        self.board = np.full((BOARD_ROWS, BOARD_COLS), None)
        self.current_player = "X"
        self.game_over = False
        self.draw = False
        self.game_on = False


class Game:
    def __init__(self):
        self.tic_tac_toe = TicTacToe()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT + 50))
        pygame.display.set_caption('Tic Tac Toe')
        self.screen.fill(BG_COLOR)
        self.draw_lines()

    def draw_lines(self):
        for row in range(1, BOARD_ROWS):
            pygame.draw.line(self.screen, LINE_COLOR, (0, row *
                             SQ_SIZE), (WIDTH, row * SQ_SIZE), LINE_WIDTH)
        for col in range(1, BOARD_COLS):
            pygame.draw.line(self.screen, LINE_COLOR, (col *
                             SQ_SIZE, 0), (col * SQ_SIZE, HEIGHT), LINE_WIDTH)

    def draw_figures(self):
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                if self.tic_tac_toe.board[row][col] == 'X':
                    self.draw_cross(row, col)
                elif self.tic_tac_toe.board[row][col] == 'O':
                    self.draw_circle(row, col)

    def draw_circle(self, row, col):
        pygame.draw.circle(self.screen, CIRCLE_COLOR, (int(
            col * SQ_SIZE + SQ_SIZE//2), int(row * SQ_SIZE + SQ_SIZE//2)), CIRCLE_RADIUS, CIRCLE_WIDTH)

    def draw_cross(self, row, col):
        start_desc = (col * SQ_SIZE + SPACE, row * SQ_SIZE + SPACE)
        end_desc = (col * SQ_SIZE + SQ_SIZE - SPACE,
                    row * SQ_SIZE + SQ_SIZE - SPACE)
        pygame.draw.line(self.screen, CROSS_COLOR,
                         start_desc, end_desc, CROSS_WIDTH)
        start_asc = (col * SQ_SIZE + SPACE, row * SQ_SIZE + SQ_SIZE - SPACE)
        end_asc = (col * SQ_SIZE + SQ_SIZE - SPACE, row * SQ_SIZE + SPACE)
        pygame.draw.line(self.screen, CROSS_COLOR,
                         start_asc, end_asc, CROSS_WIDTH)

    def draw_winner(self, player):
        line_col = CROSS_COLOR if (player == 'X') else CIRCLE_COLOR
        for col in range(BOARD_COLS):
            if all([self.tic_tac_toe.board[row][col] == player for row in range(BOARD_ROWS)]):
                pygame.draw.line(self.screen, line_col, ((
                    col * SQ_SIZE) + (SQ_SIZE / 2), 0), ((col * SQ_SIZE) + (SQ_SIZE / 2), HEIGHT), 15)
                return

        for row in range(BOARD_ROWS):
            if all([self.tic_tac_toe.board[row][col] == player for col in range(BOARD_COLS)]):
                pygame.draw.line(self.screen, line_col, (0, (row * SQ_SIZE) +
                                 (SQ_SIZE / 2)), (WIDTH, (row * SQ_SIZE) + (SQ_SIZE / 2)), 15)
                return

        if all([self.tic_tac_toe.board[row][row] == player for row in range(BOARD_ROWS)]):
            pygame.draw.line(self.screen, line_col,
                             (0, 0), (WIDTH, HEIGHT), 15)
            return

        if all([self.tic_tac_toe.board[row][BOARD_ROWS - 1 - row] == player for row in range(BOARD_ROWS)]):
            pygame.draw.line(self.screen, line_col,
                             (0, HEIGHT), (WIDTH, 0), 15)
            return

    def reset_screen(self):
        self.screen.fill(BG_COLOR)
        self.draw_lines()
        self.tic_tac_toe.restart()

    def run(self):
        running = True
        while running:
            # if self.tic_tac_toe.game_on == False:
            #     text = FONT.render(f"X starts", True, (0, 0, 0))
            #     self.screen.blit(text, (0, HEIGHT))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN and not self.tic_tac_toe.game_over:
                    self.tic_tac_toe.game_on = True
                    mouseX = event.pos[0]  # x
                    mouseY = event.pos[1]  # y

                    clicked_row = int(mouseY // SQ_SIZE)
                    clicked_col = int(mouseX // SQ_SIZE)

                    if self.tic_tac_toe.mark_square(clicked_row, clicked_col, self.tic_tac_toe.current_player):
                        if self.tic_tac_toe.check_winner(self.tic_tac_toe.current_player):
                            self.tic_tac_toe.game_over = True
                            self.draw_winner(self.tic_tac_toe.current_player)

                        elif self.tic_tac_toe.is_board_full():
                            self.tic_tac_toe.game_over = True
                            self.tic_tac_toe.draw = True
                        else:
                            self.tic_tac_toe.current_player = 'O' if self.tic_tac_toe.current_player == 'X' else 'X'

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.reset_screen()

            self.draw_figures()
            if (self.tic_tac_toe.game_over == True):
                if (self.tic_tac_toe.draw == True):
                    pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(
                        WIDTH/5, HEIGHT/3, 3.5*(WIDTH/5), 1*(HEIGHT/4)))
                    text = FONT.render(f"DRAW", True, (0, 0, 0))
                    self.screen.blit(text, (WIDTH/4, HEIGHT/2.5))
                else:
                    pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(
                        WIDTH/5, HEIGHT/3, 3.5*(WIDTH/5), 1*(HEIGHT/4)))
                    text = FONT.render(
                        f"{self.tic_tac_toe.current_player} WINS", True, (0, 0, 0))
                    self.screen.blit(text, (WIDTH/4, HEIGHT/2.5))
            pygame.display.update()

            if (self.tic_tac_toe.game_over == True):
                sleep(2)
                text = FONT.render(f"Restarting...", True, (0, 0, 0))
                self.screen.blit(text, (0, HEIGHT))
                pygame.display.update()
                sleep(2)
                self.reset_screen()

        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run()

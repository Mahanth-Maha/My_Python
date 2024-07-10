import copy
import time
import pygame
import math
import os
import random
import pandas as pd


df = pd.read_csv('sudoku_500000_for_github.csv')
pygame.init()

G = 0.25
SEED_SIZE = 5
PARTICLE_SIZE = 2
PARTICLE_NUM = 100
COOLDOWN = 3000

WIDTH, HEIGHT = 450, 450
LINE_WIDTH = 1
PAD_LINE_WIDTH = 10
WIDTH_PADDING = WIDTH + PAD_LINE_WIDTH

BOARD_ROWS, BOARD_COLS = 9, 9
SQ_SIZE = WIDTH // BOARD_COLS

INPUT_ROWS, INPUT_COLS = 3, 3
IN_SIZE = WIDTH // INPUT_COLS

FONT_SIZE = 48
FONT = pygame.font.Font(pygame.font.get_default_font(), FONT_SIZE)

RED = (248, 1, 41)
RED_TEXT = (251, 201, 159)
BLUE = (3, 165, 207)
DARK_BLUE = (0, 122, 204)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLACK_FADED = (0, 0, 0, 100)
GREEN = (164, 251, 166)
ORANGE = (254, 118, 2)
BG_COLOR = (30, 30, 30)
LINE_COLOR = (252, 252, 252)
FONT_COLOR = (187, 238, 255)
FONT_COLOR2 = (238, 187, 255)
COLOURS = [(255, 89, 94), (255, 202, 58), (138, 201, 38),
           (25, 130, 196), (106, 76, 147)]

pygame.mixer.init()
launch1 = pygame.mixer.Sound('audio/launch1.wav')
launch2 = pygame.mixer.Sound('audio/launch2.wav')
explode1 = pygame.mixer.Sound('audio/explode1.wav')
explode2 = pygame.mixer.Sound('audio/explode2.wav')

vec = pygame.math.Vector2

unit = vec(1, 0)
heart_vectors = []
for i in range(360):
    x = 16 * (math.sin(i) ** 3)
    y = -1 * (13 * math.cos(i) - 5 * math.cos(2 * i) -
              2 * math.cos(3 * i) - math.cos(4 * i))
    heart_vectors.append(vec(x, y) * 0.25)

os.environ['SDL_VIDEO_CENTERED'] = '1'


class Particle:
    def __init__(self, screen, pos, vel, size, colour):
        self.pos = pos
        self.vel = vel
        self.size = size
        self.screen = screen
        self.colour = colour

    def update(self, acc):
        self.vel += acc
        self.pos += self.vel

    def draw(self):
        pygame.draw.circle(self.screen, self.colour,
                           (int(self.pos.x), int(self.pos.y)), self.size)


class Firework:
    def __init__(self, screen, pos, vel, heart=False):
        self.g = vec(0, G)
        self.screen = screen
        self.colour = random.choice(COLOURS)
        self.seed = Particle(self.screen, vec(
            pos), vec(0, vel), SEED_SIZE, self.colour)
        self.particles = []
        self.exploded = False
        self.explode_time = 0
        self.finished = False
        self.heart = heart
        random.choice((launch1, launch2)).play()

    def update(self):
        if not self.exploded:
            self.seed.update(self.g)
        else:
            now = pygame.time.get_ticks()
            if now - self.explode_time > COOLDOWN:
                self.finished = True
        for particle in self.particles:
            if self.heart:
                particle.update(vec(0, 0))
            else:
                particle.update(self.g)

    def draw(self):
        if not self.exploded:
            self.seed.draw()
        for particle in self.particles:
            particle.draw()

    def explode(self):
        if not self.exploded:
            if self.seed.vel.y >= 0:
                for j in range(PARTICLE_NUM):
                    velocity = unit.rotate(random.randrange(
                        0, 360)) * random.randrange(0, 300, 10) / 100
                    if self.heart:
                        velocity = random.choice(heart_vectors)
                    self.particles.append(
                        Particle(self.screen, vec(self.seed.pos.x, self.seed.pos.y), velocity, PARTICLE_SIZE,
                                 self.colour))
                del self.seed
                self.exploded = True
                self.explode_time = pygame.time.get_ticks()
                random.choice((explode1, explode2)).play()


class game:
    def __init__(self, game_board=None, sol_board=None) -> None:
        if game_board == None and sol_board == None:
            try:
                self.Game_Board, self.solution = self.get_sudoku()
                self.board = copy.deepcopy(self.Game_Board)

            except Exception:
                self.Game_Board = [
                    [0, 7, 1, 9, 2, 0, 0, 4, 3],
                    [0, 4, 0, 8, 0, 1, 6, 0, 0],
                    [2, 0, 0, 0, 0, 3, 1, 0, 8],
                    [5, 0, 0, 7, 3, 4, 0, 6, 0],
                    [0, 0, 0, 0, 1, 0, 8, 3, 0],
                    [1, 0, 0, 0, 8, 5, 0, 7, 4],
                    [9, 1, 0, 3, 0, 2, 0, 8, 0],
                    [0, 0, 7, 5, 0, 0, 0, 1, 0],
                    [6, 8, 3, 0, 0, 0, 0, 0, 0]
                ]
                # user board
                self.board = [
                    [0, 7, 1, 9, 2, 0, 0, 4, 3],
                    [0, 4, 0, 8, 0, 1, 6, 0, 0],
                    [2, 0, 0, 0, 0, 3, 1, 0, 8],
                    [5, 0, 0, 7, 3, 4, 0, 6, 0],
                    [0, 0, 0, 0, 1, 0, 8, 3, 0],
                    [1, 0, 0, 0, 8, 5, 0, 7, 4],
                    [9, 1, 0, 3, 0, 2, 0, 8, 0],
                    [0, 0, 7, 5, 0, 0, 0, 1, 0],
                    [6, 8, 3, 0, 0, 0, 0, 0, 0]
                ]
                self.solution = [
                    [8, 7, 1, 9, 2, 6, 5, 4, 3],
                    [3, 4, 9, 8, 5, 1, 6, 2, 7],
                    [2, 5, 6, 4, 7, 3, 1, 9, 8],
                    [5, 9, 8, 7, 3, 4, 2, 6, 1],
                    [7, 6, 4, 2, 1, 9, 8, 3, 5],
                    [1, 3, 2, 6, 8, 5, 9, 7, 4],
                    [9, 1, 5, 3, 4, 2, 7, 8, 6],
                    [4, 2, 7, 5, 6, 8, 3, 1, 9],
                    [6, 8, 3, 1, 9, 7, 4, 5, 2]
                ]
        else:
            self.Game_Board = game_board
            self.board = game_board
            self.solution = sol_board

        self.screen = pygame.display.set_mode((WIDTH + WIDTH_PADDING, HEIGHT))
        pygame.display.set_caption('Sudoku')
        self.screen.fill(BG_COLOR)
        self.draw_lines()
        self.draw_board()
        self.draw_input_reader()
        self.selected_square = None
        self.game_over = False
        self.fireworks = []

    def get_sudoku(self):
        question, solution = (df.loc[random.randint(0, df.shape[0])])
        qb = self.get_sudoku_board_from_Str(question)
        ab = self.get_sudoku_board_from_Str(solution)
        if qb == None or ab == None:
            return self.get_sudoku()
        return qb, ab

    def get_sudoku_board_from_Str(self, s: str):
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

    def draw_lines(self):
        line_width_bold = 0
        for row in range(1, BOARD_ROWS):
            if (row) % 3 == 0:
                line_width_bold = 3
            else:
                line_width_bold = 0
            pygame.draw.line(self.screen, LINE_COLOR, (0, row * SQ_SIZE),
                             (WIDTH, row * SQ_SIZE), LINE_WIDTH + line_width_bold)
        for col in range(1, BOARD_COLS):
            if (col) % 3 == 0:
                line_width_bold = 3
            else:
                line_width_bold = 0
            pygame.draw.line(self.screen, LINE_COLOR, (col * SQ_SIZE, 0),
                             (col * SQ_SIZE, HEIGHT), LINE_WIDTH + line_width_bold)
        pygame.draw.line(self.screen, LINE_COLOR, (BOARD_COLS * SQ_SIZE, 0),
                         (BOARD_COLS * SQ_SIZE, HEIGHT), PAD_LINE_WIDTH)

    def draw_board(self):
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                if self.board[row][col] != 0 and self.Game_Board[row][col] == 0:
                    text = FONT.render(f"{self.board[row][col]}", True, BLUE)
                    self.screen.blit(
                        text, (col * SQ_SIZE + (FONT_SIZE)/4, row * SQ_SIZE + (FONT_SIZE)/8))
                if self.board[row][col] != 0 and self.Game_Board[row][col] != 0:
                    text = FONT.render(
                        f"{self.board[row][col]}", True, FONT_COLOR)
                    self.screen.blit(
                        text, (col * SQ_SIZE + (FONT_SIZE)/4, row * SQ_SIZE + (FONT_SIZE)/8))

                if self.board[row][col] != 0 and self.Game_Board[row][col] == 0 and self.validate_input(row, col) == False:
                    pygame.draw.rect(self.screen, RED, pygame.Rect(
                        col * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    text = FONT.render(
                        f"{self.board[row][col]}", True, RED_TEXT)
                    self.screen.blit(
                        text, (col * SQ_SIZE + (FONT_SIZE)/4, row * SQ_SIZE + (FONT_SIZE)/8))

                if self.board[row][col] != 0 and self.Game_Board[row][col] != 0 and self.validate_input(row, col) == False:
                    pygame.draw.rect(self.screen, BLUE, pygame.Rect(
                        col * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    text = FONT.render(
                        f"{self.board[row][col]}", True, RED_TEXT)
                    self.screen.blit(
                        text, (col * SQ_SIZE + (FONT_SIZE)/4, row * SQ_SIZE + (FONT_SIZE)/8))

    def draw_input_reader(self):
        for row in range(1, 4):
            pygame.draw.line(self.screen, LINE_COLOR, (WIDTH_PADDING, row *
                             IN_SIZE), (WIDTH + WIDTH_PADDING, row * IN_SIZE), LINE_WIDTH)
        for col in range(1, 4):
            pygame.draw.line(self.screen, LINE_COLOR, (WIDTH_PADDING + (col * IN_SIZE),
                             0), (WIDTH_PADDING + (col * IN_SIZE), HEIGHT), LINE_WIDTH)
        values = list(range(1, 10))
        for row in range(3):
            for col in range(3):
                FONT2 = pygame.font.Font(
                    pygame.font.get_default_font(), int(FONT_SIZE * 2.5))
                text = FONT2.render(
                    f"{3 * (row) + col + 1}", True, FONT_COLOR2)
                self.screen.blit(text, (WIDTH_PADDING + (col * IN_SIZE) +
                                 int((FONT_SIZE)/1.25), (row * IN_SIZE) + (FONT_SIZE)/2))

    def select_square(self, row, col):
        if (self.selected_square == (row, col)):
            if self.Game_Board[row][col] == 0:
                self.board[row][col] = 0
            self.selected_square = None
            self.refresh_draw_Screen()
            return

        if (self.Game_Board[row][col] != 0):
            self.refresh_draw_Screen()
            pygame.draw.rect(self.screen, (215, 225, 215), pygame.Rect(
                col * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE))
            text = FONT.render(f"{self.board[row][col]}", True, BLACK)
            self.screen.blit(
                text, (col * SQ_SIZE + (FONT_SIZE)/4, row * SQ_SIZE + (FONT_SIZE)/8))
        else:
            self.refresh_draw_Screen()
            for i in range(BOARD_ROWS):
                pygame.draw.rect(self.screen, DARK_BLUE, pygame.Rect(
                    i * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                if (self.board[row][i] != 0):
                    text = FONT.render(f"{self.board[row][i]}", True, WHITE)
                    self.screen.blit(
                        text, (i * SQ_SIZE + (FONT_SIZE)/4, row * SQ_SIZE + (FONT_SIZE)/8))

                pygame.draw.rect(self.screen, DARK_BLUE, pygame.Rect(
                    col * SQ_SIZE, i * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                if (self.board[i][col] != 0):
                    text = FONT.render(f"{self.board[i][col]}", True, WHITE)
                    self.screen.blit(
                        text, (col * SQ_SIZE + (FONT_SIZE)/4, i * SQ_SIZE + (FONT_SIZE)/8))

                r, c = row // 3, col // 3
                row_box, col_box = (r*3) + (i % 3), (c*3) + (i//3)

                pygame.draw.rect(self.screen, DARK_BLUE, pygame.Rect(
                    col_box * SQ_SIZE, row_box * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                if (self.board[row_box][col_box] != 0):
                    text = FONT.render(
                        f"{self.board[row_box][col_box]}", True, WHITE)
                    self.screen.blit(
                        text, (col_box * SQ_SIZE + (FONT_SIZE)/4, row_box * SQ_SIZE + (FONT_SIZE)/8))

            pygame.draw.rect(self.screen, GREEN, pygame.Rect(
                col * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE))
            if (self.board[row][col] != 0):
                text = FONT.render(f"{self.board[row][col]}", True, BLACK)
                self.screen.blit(
                    text, (col * SQ_SIZE + (FONT_SIZE)/4, row * SQ_SIZE + (FONT_SIZE)/8))
            self.selected_square = (row, col)

        value = self.board[row][col]
        if value != 0:
            for row in range(BOARD_ROWS):
                for col in range(BOARD_COLS):
                    if self.board[row][col] == value:
                        pygame.draw.rect(self.screen, DARK_BLUE, pygame.Rect(
                            col * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                        text = FONT.render(
                            f"{self.board[row][col]}", True, ORANGE)
                        self.screen.blit(
                            text, (col * SQ_SIZE + (FONT_SIZE)/4, row * SQ_SIZE + (FONT_SIZE)/8))

        self.draw_lines()

    def read_input_from_screen(self, col, row):
        updating_number = 3 * col + row + 1
        # print(f"number updated : {updating_number}")
        self.board[self.selected_square[0]
                   ][self.selected_square[1]] = updating_number
        board_row, board_col = self.selected_square
        self.screen.fill(BG_COLOR)
        if self.validate_input(board_row, board_col) == False:
            pygame.draw.rect(self.screen, RED, pygame.Rect(
                board_col * SQ_SIZE, board_row * SQ_SIZE, SQ_SIZE, SQ_SIZE))
            text = FONT.render(
                f"{self.board[board_row][board_col]}", True, RED_TEXT)
            self.screen.blit(text, (board_col * SQ_SIZE +
                             (FONT_SIZE)/4, board_row * SQ_SIZE + (FONT_SIZE)/8))
            # print("wrong input")

        self.draw_lines()
        self.draw_board()
        self.draw_input_reader()
        self.selected_square = None

        if self.check_if_won():
            self.play_winning_celebrations()
            self.game_over = True

    def refresh_draw_Screen(self):
        self.screen.fill(BG_COLOR)
        self.draw_lines()
        self.draw_board()
        self.draw_input_reader()
        self.selected_square = None

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN and not self.game_over:
                    mouseX = event.pos[0]
                    mouseY = event.pos[1]

                    if (self.selected_square == None and mouseX < WIDTH) or (mouseX < WIDTH):
                        clicked_row = int(mouseY // SQ_SIZE)
                        clicked_col = int(mouseX // SQ_SIZE)
                        # print("board " ,clicked_row,clicked_col)
                        self.select_square(clicked_row, clicked_col)
                    elif mouseX > WIDTH_PADDING and self.selected_square != None:
                        clicked_row = int(mouseY // IN_SIZE)
                        clicked_col = int((mouseX - WIDTH_PADDING) // IN_SIZE)
                        # print("input : " ,clicked_row,clicked_col)
                        self.read_input_from_screen(clicked_row, clicked_col)

            pygame.display.update()

            if self.game_over:
                running = False

        pygame.quit()

    def validate_input(self, row=None, col=None):
        if row == None and col == None:
            row, col = self.selected_square
        value = self.board[row][col]
        for i in range(BOARD_ROWS):
            if (i != col and self.board[row][i] == value) or (i != row and self.board[i][col] == value) or (self.board[((row//3)*3) + (i % 3)][((col//3)*3) + (i//3)] == value and ((row//3)*3) + (i % 3) != row and ((col//3)*3) + (i//3) != col):
                return False
        return True

    def check_if_won(self):
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                if self.board[row][col] == 0 or not self.validate_input(row, col):
                    return False
        return True

    def spawn(self, pos, button):
        if button == 'left':
            vel = -math.sqrt(2 * G * (HEIGHT - pos[1]))
            self.fireworks.append(
                Firework(self.screen, (pos[0], HEIGHT), vel, True))

        if button == 'right':
            self.fireworks.append(
                Firework(self.screen, pos, random.randrange(-20, -15)))

    def play_winning_celebrations(self):
        starting_celeb = time.time()
        self.screen.fill(BG_COLOR)
        clock = pygame.time.Clock()
        fade = pygame.Surface((WIDTH_PADDING + WIDTH, HEIGHT)).convert_alpha()
        fade.fill(BLACK_FADED)
        FONT_SIZE = 48
        FONT = pygame.font.Font(pygame.font.get_default_font(), FONT_SIZE)
        text = FONT.render(f"Congrats , You won !", True, WHITE)
        celeb = True
        while celeb:
            self.screen.blit(text, ((WIDTH_PADDING + WIDTH)/4, HEIGHT / 8))
            self.screen.blit(fade, (0, 0))
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    celeb  = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if event.button == 1:
                        self.spawn(mouse_pos, 'left')
                    if event.button == 3:
                        self.spawn(mouse_pos, 'right')

            chance = random.random()
            if chance < 0.01:
                self.fireworks.append(Firework(self.screen, (random.randrange(
                    0, WIDTH), HEIGHT), random.randrange(-20, -15)))

            for firework in self.fireworks:
                firework.explode()
                firework.update()
                firework.draw()
                if firework.finished:
                    self.fireworks.remove(firework)
                    del firework

            pygame.display.flip()
            end_celeb = time.time()
            if(end_celeb - starting_celeb > 10) :
                celeb = False
        # pygame.quit()

if __name__ == '__main__':
    play = True
    while play:
        play = False
        Sudoku = game()
        Sudoku.run()
        y = input("Enter Y to play again : ")
        if y in ('y', 'Y', 'yes', 'YES'):
            play = True
            pygame.init()
        

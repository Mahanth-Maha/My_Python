import numpy as np
import pygame


class ChessBoard():
    def __init__(self, size = 400) -> None:
        pygame.init()
        self.WIDTH, self.HEIGHT = size ,size
        self.WINDOW = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption('Chess')

        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)

        self.BOARD_SIZE = 8
        self.SQ_SIZE = self.WIDTH // self.BOARD_SIZE
        self.IMAGES = self.load_images()

        self.board = np.array([
            ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
            ['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
            ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR']
        ])
        
        self.player_turn = 'w'
        self.selected_square = None
        self.target_square = None

    def Play(self):
        self.run = True
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    col = pos[0] // self.SQ_SIZE
                    row = pos[1] // self.SQ_SIZE
                    if selected_square:
                        end_square = (row, col)
                        self.move_piece(self.board, selected_square, end_square)
                        selected_square = None
                    else:
                        selected_square = (row, col)

            self.draw_board()
            self.draw_pieces()
            pygame.display.update()

    pygame.quit()
        
    def load_images(self):
        pieces = ['bB', 'bK', 'bN', 'bP', 'bQ', 'bR', 'wB', 'wK', 'wN', 'wP', 'wQ', 'wR']
        images = {}
        for piece in pieces:
            images[piece] = pygame.transform.scale(pygame.image.load(f'images/{piece}.png'), (self.SQ_SIZE, self.SQ_SIZE))
        return images

    def draw_board(self):
        colors = [pygame.Color(235, 235, 208), pygame.Color(119, 148, 85)]
        for r in range(self.BOARD_SIZE):
            for c in range(self.BOARD_SIZE):
                color = colors[(r + c) % 2]
                pygame.draw.rect(self.WINDOW, color, pygame.Rect(c * self.SQ_SIZE, r * self.SQ_SIZE, self.SQ_SIZE, self.SQ_SIZE))

    def draw_pieces(self):
        for r in range(self.BOARD_SIZE):
            for c in range(self.BOARD_SIZE):
                piece = self.board[r][c]
                if piece != '--':
                    self.WINDOW.blit(self.IMAGES[piece], pygame.Rect(c * self.SQ_SIZE, r * self.SQ_SIZE, self.SQ_SIZE, self.SQ_SIZE))

    
    def move_piece(self,start_square,end_square):
        sr, sc = start_square
        er, ec = end_square
        piece = self.board[sr][sc]
        self.board[sr][sc] = '--'
        self.board[er][ec] = piece

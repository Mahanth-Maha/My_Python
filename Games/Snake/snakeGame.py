import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
ROWS, COLS = HEIGHT // CELL_SIZE, WIDTH // CELL_SIZE

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

APPLE_IMAGE = pygame.image.load(r"images\apple.png")
APPLE_IMAGE = pygame.transform.scale(APPLE_IMAGE, (CELL_SIZE, CELL_SIZE)) 

HEAD_IMAGE = pygame.image.load(r"images\head.png")  # Ensure the path is correct
HEAD_IMAGE = pygame.transform.scale(HEAD_IMAGE, (CELL_SIZE, CELL_SIZE))  # Scale to grid size

BODY_IMAGE = pygame.image.load(r"images\body.png")
BODY_IMAGE = pygame.transform.scale(BODY_IMAGE, (CELL_SIZE, CELL_SIZE))

TURN_IMAGE = pygame.image.load(r"images\turn.png")
TURN_IMAGE = pygame.transform.scale(TURN_IMAGE, (CELL_SIZE, CELL_SIZE))

TAIL_IMAGE = pygame.image.load(r"images\tail.png")
TAIL_IMAGE = pygame.transform.scale(TAIL_IMAGE, (CELL_SIZE, CELL_SIZE))

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Snake and game setup
class SnakeGame:
    def __init__(self):
        self.snake = [[5, 5]]  # Initial snake position (list of x,y pairs)
        self.direction = RIGHT  # Initial direction
        self.apple = self.spawn_apple()
        self.score = 0

    def spawn_apple(self):
        # Spawn apple at random position, ensuring it's not on the snake
        while True:
            apple = [random.randint(0, COLS-1), random.randint(0, ROWS-1)]
            if apple not in self.snake:
                return apple

    def move(self):
        # Get the current head of the snake
        head = self.snake[-1]
        new_head = [head[0] + self.direction[0], head[1] + self.direction[1]]

        # Check collisions with walls or self
        if (new_head in self.snake or 
            new_head[0] < 0 or new_head[0] >= COLS or
            new_head[1] < 0 or new_head[1] >= ROWS):
            return False  # Game over condition
        
        # Add new head to snake
        self.snake.append(new_head)

        # Check if snake eats apple
        if new_head == self.apple:
            self.score += 1
            self.apple = self.spawn_apple()  # Respawn apple
        else:
            self.snake.pop(0)  # Remove tail segment (normal movement)
        
        return True

    def change_direction(self, new_direction):
        # Prevent the snake from reversing direction
        opposite = (self.direction[0] * -1, self.direction[1] * -1)
        if new_direction != opposite:
            self.direction = new_direction


    def draw(self, screen):
        # Draw the snake
        for i, segment in enumerate(self.snake):
            x = segment[0] * CELL_SIZE
            y = segment[1] * CELL_SIZE

            # Draw the head
            if i == len(self.snake) - 1:  # Head of the snake
                if self.direction == RIGHT:
                    rotated_head = pygame.transform.rotate(HEAD_IMAGE, 0)
                elif self.direction == LEFT:
                    rotated_head = pygame.transform.rotate(HEAD_IMAGE, 180)
                elif self.direction == UP:
                    rotated_head = pygame.transform.rotate(HEAD_IMAGE, 90)
                elif self.direction == DOWN:
                    rotated_head = pygame.transform.rotate(HEAD_IMAGE, -90)
                screen.blit(rotated_head, (x, y))

            # Draw the body
            elif 0 < i < len(self.snake) - 1:  # Ignore head and tail
                prev_segment = self.snake[i - 1]
                next_segment = self.snake[i + 1]

                # Determine if this is a turn
                if (prev_segment[0] != next_segment[0] and 
                    prev_segment[1] != next_segment[1]):  # Turn condition
                    # Use the turn image
                    if (prev_segment[0] < segment[0] and next_segment[1] < segment[1]) or \
                    (next_segment[0] < segment[0] and prev_segment[1] < segment[1]):
                        rotated_turn = pygame.transform.rotate(TURN_IMAGE, 0)  # Bottom-Right turn
                    elif (prev_segment[0] < segment[0] and next_segment[1] > segment[1]) or \
                        (next_segment[0] < segment[0] and prev_segment[1] > segment[1]):
                        rotated_turn = pygame.transform.rotate(TURN_IMAGE, 90)  # Top-Right turn
                    elif (prev_segment[0] > segment[0] and next_segment[1] < segment[1]) or \
                        (next_segment[0] > segment[0] and prev_segment[1] < segment[1]):
                        rotated_turn = pygame.transform.rotate(TURN_IMAGE, -90)  # Bottom-Left turn
                    else:
                        rotated_turn = pygame.transform.rotate(TURN_IMAGE, 180)  # Top-Left turn
                    screen.blit(rotated_turn, (x, y))
                else:
                    # Straight body segment
                    if prev_segment[0] == next_segment[0]:  # Vertical body
                        rotated_body = pygame.transform.rotate(BODY_IMAGE, 90)
                    else:  # Horizontal body
                        rotated_body = BODY_IMAGE
                    screen.blit(rotated_body, (x, y))

            # Draw the tail (optional, as improvement)
            elif i == 0:  # Tail segment
                prev_segment = self.snake[1]
                if prev_segment[0] > segment[0]:  # Tail facing left
                    rotated_tail = pygame.transform.rotate(TAIL_IMAGE, 0)
                elif prev_segment[0] < segment[0]:  # Tail facing right
                    rotated_tail = pygame.transform.rotate(TAIL_IMAGE, 180)
                elif prev_segment[1] > segment[1]:  # Tail facing up
                    rotated_tail = pygame.transform.rotate(TAIL_IMAGE, -90)
                elif prev_segment[1] < segment[1]:  # Tail facing down
                    rotated_tail = pygame.transform.rotate(TAIL_IMAGE, 90)
                screen.blit(rotated_tail, (x, y))

        # Draw the apple
        screen.blit(APPLE_IMAGE, (self.apple[0] * CELL_SIZE, self.apple[1] * CELL_SIZE))


    def get_state(self):
        """
        This method can be extended later to return the game state in a way that 
        can be used by a reinforcement learning model.
        For now, it just shows the snake and apple positions.
        """
        return {"snake": self.snake, "apple": self.apple}

    

# Main game loop
def main():
    game = SnakeGame()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    game.change_direction(UP)
                elif event.key == pygame.K_DOWN:
                    game.change_direction(DOWN)
                elif event.key == pygame.K_LEFT:
                    game.change_direction(LEFT)
                elif event.key == pygame.K_RIGHT:
                    game.change_direction(RIGHT)

        # Update game state
        running = game.move()

        # Draw everything
        screen.fill(BLACK)  # Clear the screen
        game.draw(screen)
        pygame.display.flip()

        # Control frame rate
        clock.tick(10)  # 10 frames per second

    print("Game Over! Your Score:", game.score)

if __name__ == "__main__":
    main()


# play

'''
conda activate iisc
cd C:\Maha\dev\Reinforcement_Proj\Snake
python snakeGame.py

'''
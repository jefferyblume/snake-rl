import pygame
from .snake import Snake
from .board import Board
from .utils import WHITE, BLACK, RED, GREEN, TILE_SIZE, BOARD_WIDTH, BOARD_HEIGHT, draw_text

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((BOARD_WIDTH*TILE_SIZE, BOARD_HEIGHT*TILE_SIZE))
    clock = pygame.time.Clock()

    snake = Snake()
    board = Board()
    score = 0

    running = True
    while running:
        clock.tick(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.change_direction((0,-1))
                elif event.key == pygame.K_DOWN:
                    snake.change_direction((0,1))
                elif event.key == pygame.K_LEFT:
                    snake.change_direction((-1,0))
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction((1,0))

        snake.step()
        head = snake.body[0]

        if head[0]<0 or head[0]>=BOARD_WIDTH or head[1]<0 or head[1]>=BOARD_HEIGHT:
            running = False
        if head in snake.body[1:]:
            running = False
        if head == board.food:
            snake.grow = True
            score += 1
            board.reset()

        screen.fill(BLACK)
        for x,y in snake.body:
            pygame.draw.rect(screen, GREEN, (x*TILE_SIZE, y*TILE_SIZE, TILE_SIZE, TILE_SIZE))
        fx, fy = board.food
        pygame.draw.rect(screen, RED, (fx*TILE_SIZE, fy*TILE_SIZE, TILE_SIZE, TILE_SIZE))

        draw_text(screen, f"Score: {score}", WHITE, 5,5)

        pygame.display.flip()

    pygame.quit()
    print("Game Over! Score:", score)

if __name__ == "__main__":
    run_game()

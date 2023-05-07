import pygame
import time
import sys
import os.path

from components.snake import Snake
from components.fruit import Fruit
from components.score import Score

BASE_PATH = os.path.dirname(__file__)
ASSETS_PATH = os.path.join(BASE_PATH, 'assets')

SCREEN_X = 320
SCREEN_Y = 240
SCREEN_UNIT = 8

COLORS = {
    'lightgreen': pygame.Color(0xc7, 0xf0, 0xd8),
    'darkgreen': pygame.Color(0x43, 0x52, 0x3d)
}

pygame.init()
pygame.display.set_caption('Snek')
window = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
fps = pygame.time.Clock()

snake = Snake(
    position=[96, 48],
    body=[ [96, 48], [88, 48], [80, 48], [72, 48] ],
    color=COLORS['darkgreen'],
    direction=Snake.Directions.RIGHT,
    image=pygame.image.load(os.path.join(ASSETS_PATH, 'snake_body.png')),
)

fruit = Fruit(
    screen_x=SCREEN_X,
    screen_y=SCREEN_Y,
    image=pygame.image.load(os.path.join(ASSETS_PATH, 'fruit.png')),
    unit=SCREEN_UNIT
)

score = Score(
    font=pygame.font.SysFont('courier', 20),
    color=COLORS['darkgreen']
)

def finish():
    window.fill(COLORS['lightgreen'])
    my_font = pygame.font.SysFont('courier', 20)
    game_over_surface = my_font.render(
        'Score: ' + str(score.value), 
        True, 
        COLORS['darkgreen']
    )
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (SCREEN_X/2, SCREEN_Y/4)
    window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    sys.exit()

while True:

    direction = None

    # Events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            direction = event.key
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Logic
    snake.move(direction, SCREEN_UNIT)
    snake.grow_if_eat_fruit(fruit)
    if fruit.was_eaten:
        score.update()
        fruit.spawn(SCREEN_X, SCREEN_Y, SCREEN_UNIT)

    # Draw stuff on screen
    window.fill(COLORS['lightgreen'])
    snake.draw(window)
    fruit.draw(window)
    score.display(window)

    # Game Over conditions
    if snake.has_collided_on_itself() or \
    snake.has_collided_on_screen_edges(SCREEN_X, SCREEN_Y, SCREEN_UNIT):
        finish()

    pygame.display.update()
    fps.tick(snake.speed)

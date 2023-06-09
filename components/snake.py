import pygame
from enum import Enum

class Snake:

    class Directions(Enum):
        LEFT = 1
        RIGHT = 2
        UP = 3
        DOWN = 4

    def __init__(self, position, body, color, direction, image) -> None:
        self.position = position
        self.body = body
        self.color = color
        self.direction = direction
        self.image = image
        self.speed = 15

    def move(self, new_direction, unit) -> None:
        if new_direction == pygame.K_UP and self.direction != Snake.Directions.DOWN:
            self.direction = Snake.Directions.UP
        if new_direction == pygame.K_DOWN and self.direction != Snake.Directions.UP:
            self.direction = Snake.Directions.DOWN
        if new_direction == pygame.K_LEFT and self.direction != Snake.Directions.RIGHT:
            self.direction = Snake.Directions.LEFT
        if new_direction == pygame.K_RIGHT and self.direction != Snake.Directions.LEFT:
            self.direction = Snake.Directions.RIGHT

        match self.direction:
            case Snake.Directions.UP:
                self.position[1] -= unit
            case Snake.Directions.DOWN:
                self.position[1] += unit
            case Snake.Directions.LEFT:
                self.position[0] -= unit
            case Snake.Directions.RIGHT:
                self.position[0] += unit

    def grow_if_eat_fruit(self, fruit) -> None:
        self.body.insert(0, list(self.position))
        if self.position[0] == fruit.position[0] and self.position[1] == fruit.position[1]:
            fruit.was_eaten = True
        else:
            self.body.pop()

    def draw(self, window) -> None:
        for block in self.body:
            window.blit(self.image, block)
    
    def has_collided_on_screen_edges(self, screen_x, screen_y, unit) -> bool:
        return (
            self.position[0] < 0 or self.position[0] > screen_x-unit or
            self.position[1] < 0 or self.position[1] > screen_y-unit
        )
    
    def has_collided_on_itself(self) -> bool:
        for block in self.body[1:]:
            if self.position[0] == block[0] and self.position[1] == block[1]:
                return True
        return False

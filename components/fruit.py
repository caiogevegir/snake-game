import random

from .globals import Global

class Fruit:
    
    def __init__(self, screen_x, screen_y, image) -> None:
        self.image = image
        self.spawn(screen_x, screen_y)
    
    def spawn(self, screen_x, screen_y) -> None:
        self.position = [
            random.randrange(1, (screen_x//Global.unit)) * Global.unit,
            random.randrange(1, (screen_y//Global.unit)) * Global.unit
        ]
        self.was_eaten = False

    def draw(self, game_window) -> None:
        game_window.blit(
            self.image, self.position
        )

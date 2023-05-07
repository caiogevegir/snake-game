import random

class Fruit:
    
    def __init__(self, screen_x, screen_y, image, unit) -> None:
        self.image = image
        self.spawn(screen_x, screen_y, unit)
    
    def spawn(self, screen_x, screen_y, unit) -> None:
        self.position = [
            random.randrange(1, (screen_x//unit)) * unit,
            random.randrange(1, (screen_y//unit)) * unit
        ]
        self.was_eaten = False

    def draw(self, game_window) -> None:
        game_window.blit(self.image, self.position)

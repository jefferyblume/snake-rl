import random
from .utils import BOARD_WIDTH, BOARD_HEIGHT

class Board:
    def __init__(self):
        self.reset()

    def reset(self):
        self.food = self._place_food()

    def _place_food(self):
        return (random.randint(0, BOARD_WIDTH-1), random.randint(0, BOARD_HEIGHT-1))

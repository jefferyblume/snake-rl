from .utils import BOARD_WIDTH, BOARD_HEIGHT

class Snake:
    def __init__(self):
        self.reset()

    def reset(self):
        self.body = [(BOARD_WIDTH//2, BOARD_HEIGHT//2)]
        self.direction = (1,0)
        self.grow = False

    def step(self):
        head = self.body[0]
        new_head = (head[0]+self.direction[0], head[1]+self.direction[1])
        self.body.insert(0, new_head)
        if not self.grow:
            self.body.pop()
        else:
            self.grow = False

    def change_direction(self, new_dir):
        if (new_dir[0], new_dir[1]) == (-self.direction[0], -self.direction[1]):
            return
        self.direction = new_dir

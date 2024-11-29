from display import Display
from game_of_life import GameOfLife
import random

seeds = {
    "glider": [
        [0, 1, 0],
        [0, 0, 1],
        [1, 1, 1]
    ],
    "pentomino_r": [
        [0, 1, 0],
        [0, 1, 1],
        [1, 1, 0]
    ]
}

class LifeGameController:
    def __init__(self, width, height, cell_size=10):
        self.game = GameOfLife(width, height)
        self.display = Display(width, height, cell_size)

        self.game.set_seed(seeds["pentomino_r"], 20, 20)

    def generate_random_cells(self):
        for y in range(self.game.height):
            for x in range(self.game.width):
                self.game.set_cell(x, y, random.choice([0, 1]))

    def generate_glider(self):
        seed = [
            [0, 1, 0],
            [0, 0, 1],
            [1, 1, 1]
        ]
        self.game.set_seed(seed, 30, 30)


    def update(self):
        self.game.next_generation()
        self.display.update(self.game.grid)
        self.display.window.after(100, self.update)

    def start(self):
        self.update()
        self.display.start()
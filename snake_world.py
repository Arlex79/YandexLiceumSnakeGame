from snake import *
from time import time


class SnakeWorld:
    def __init__(self):
        self.snakes = []
        self.game_type = None
        self.tick_last_time = time()

    def new_game(self, game_type='single'):
        self.game_type = game_type
        if game_type == 'single':
            self.snakes.append(Snake([SnakeBodySegment(5, 5), SnakeBodySegment(5, 6)]))

        else:
            assert False

    def move_snakes(self):
        for snake in self.snakes:
            snake.move()

    def try_move_snakes(self):
        now_ms = time()
        if (now_ms - self.tick_last_time) > 1:
            self.tick_last_time = now_ms
            self.move_snakes()

    def draw(self, scr):
        for snake in self.snakes:
            snake.draw(scr)

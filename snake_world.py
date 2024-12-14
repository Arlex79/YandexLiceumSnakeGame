from snake import *
from time import time
from random import randint
from hud import HUD
class SnakeWorld:
    def __init__(self):
        self.snakes = []
        self.apples = []
        self.inGameHud = HUD()
        self.game_type = None
        self.tick_last_time = time()
        self.isDrawHitbox = True
        self.isDrawSprites = False

    def new_game(self, game_type='single'):
        self.game_type = game_type
        self.snakes = []
        if game_type == 'single':
            self.snakes.append(Snake([SnakeBodySegment(5, 5), SnakeBodySegment(5, 6)]))

        else:
            assert False

    def add_random_coords_snake(self):
        x = randint(0, MAX_SNAKE_X)
        y = randint(0, MAX_SNAKE_Y)
    def control_by_keyboard(self, keys):
        for snake in self.snakes:
            snake.control(keys)

    def move_snakes(self):
        for snake in self.snakes:
            snake.move()

    def move_snakes(self):
        for snake in self.snakes:
            snake.try_move_snake()


    def draw(self, scr):

        for snake in self.snakes:
            snake.draw(scr)

        self.inGameHud.draw(scr)

import pygame as pg
from settings import *
from copy import copy
from time import time
from random import choice, randint


class SnakeSkin:
    def __init__(self, head='white', *body):
        self.head = head
        self.body = body

    def get_color_for_index(self, index):
        assert index >= 0
        if index == 0:
            return self.head

        else:
            return self.body[index % len(self.body)]
SNAKE_DEFAULT_SKINS = [SnakeSkin('yellow', 'red', 'orange', 'yellow', 'green', 'cyan', 'blue', 'violet'),
                       SnakeSkin('gray', 'white', 'blue', 'red'),
                       SnakeSkin('red', 'yellow', 'orange', 'red'),
                       SnakeSkin('gray', 'blue', 'cyan', 'violetq'),]


class SnakeBodySegment:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Snake:
    def __init__(self, body, skin=None, control_scheme=DEFAULT_CONTROL_SCHEME):
        self.control_scheme = control_scheme
        self.body = body

        self.tick_last_time = time()
        self.dx = 1
        self.dy = 0
        if skin is None:
            self.skin = choice(SNAKE_DEFAULT_SKINS)
        else:
            self.skin = skin

    def draw(self, scr):
        for i in range(len(self.body)):
            snake_body_segment = self.body[i]
            x = snake_body_segment.x
            y = snake_body_segment.y
            pg.draw.rect(scr, self.skin.get_color_for_index(i),
                         pg.Rect(SNAKE_TILE * x, SNAKE_TILE * y, SNAKE_TILE, SNAKE_TILE))

    def move(self):
        del self.body[-1]
        head = self.body[0]
        self.body.insert(0, SnakeBodySegment(head.x + self.dx, head.y + self.dy))
    def get_move_timeout(self):
        return SNAKE_SLOWLY_MOVE_TIMEOUT
    def try_move_snake(self):
        now_ms = time()

        if (now_ms - self.tick_last_time) > self.get_move_timeout():
            self.tick_last_time = now_ms
            self.move()

    def add_segment(self, count=1):
        self.snake_end = self.body[-1]
        self.body.append(copy(self.snake_end))

    def control(self, keys):
        if keys[self.control_scheme['up']]:
            self.dx = 0
            self.dy = -1

        if keys[self.control_scheme['down']]:
            self.dx = 0
            self.dy = 1

        if keys[self.control_scheme['left']]:
            self.dx = -1
            self.dy = 0

        if keys[self.control_scheme['right']]:
            self.dx = 1
            self.dy = 0

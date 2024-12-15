import pygame as pg
from settings import *
from random import randint


class Apple:
    def __init__(self, x=None, y=None, size=1, color='red'):
        if x is None:
            self.x = randint(0, MAX_SNAKE_X)
        else:
            self.x = x
        if y is None:
            self.y = randint(0, MAX_SNAKE_Y)
        else:
            self.y = y
        self.size = size
        self.color = color

    def draw(self, scr):

        pg.draw.rect(scr, self.color,
                     pg.Rect(SNAKE_TILE * self.x, SNAKE_TILE * self.y, SNAKE_TILE, SNAKE_TILE))

    def draw_hitbox(self, scr):

        pg.draw.rect(scr, self.color,
                     pg.Rect(SNAKE_TILE * self.x, SNAKE_TILE * self.y, SNAKE_TILE, SNAKE_TILE), 1)

import pygame as pg
from settings import *

class Apple:
    def __init__(self, x, y, size=1, color='red'):
        self.x = x
        self.y = y
        self.size = size
        self.color = color

    def draw(self, scr):

        pg.draw.rect(scr, self.color,
                         pg.Rect(SNAKE_TILE * self.x, SNAKE_TILE * self.y, SNAKE_TILE, SNAKE_TILE))
    def draw_hitbox(self, scr):

        pg.draw.rect(scr, self.color,
                         pg.Rect(SNAKE_TILE * self.x, SNAKE_TILE * self.y, SNAKE_TILE, SNAKE_TILE), 1)
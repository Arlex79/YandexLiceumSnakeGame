import pygame as pg
from settings import *
class SnakeBodySegment:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Snake:
    def __init__(self, body):
        self.color = 'red'
        self.body = body

    def draw(self, scr):
        for snake_body_segment in self.body:
            x = snake_body_segment.x
            y = snake_body_segment.y
            pg.draw.rect(scr, self.color, pg.Rect(30, 30, 60, 60))

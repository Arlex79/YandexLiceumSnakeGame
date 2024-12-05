import pygame as pg
from settings import *


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


class SnakeBodySegment:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Snake:
    def __init__(self, body, skin=SnakeSkin('yellow', 'red', 'green')):
        self.color = 'red'
        self.body = body
        self.skin = skin
        self.dx = 1
        self.dy = 0

    def draw(self, scr):
        for i in range(len(self.body)):
            snake_body_segment = self.body[i]
            x = snake_body_segment.x
            y = snake_body_segment.y
            pg.draw.rect(scr, self.skin.get_color_for_index(i),
                         pg.Rect(SNAKE_TILE * x, SNAKE_TILE * y, SNAKE_TILE, SNAKE_TILE))

    def move(self):
        print('pass move snake')
        end_body = self.body[-1]
        del self.body[-1]
        head = self.body[0]
        self.body.insert(0, SnakeBodySegment(head.x - self.dx, head.y - self.dy))

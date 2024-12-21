from additionall.settings import *
import pygame as pg


class Background:
    def __init__(self, color='#333d48', image_filename=None):
        self.color = color
        self.image_filename = image_filename

    def draw(self, scr):
        scr.fill(self.color)


class GridBackground(Background):
    def __init__(self, color='#333333', image_filename=None, grid_size=TILE, grid_color='black', grid_width=1):
        super().__init__(color, image_filename)
        self.grid_size = grid_size
        self.grid_color = grid_color
        self.grid_width = grid_width

    def draw(self, scr):
        super().draw(scr)
        for x in range(0, X_SIZE, self.grid_size):
            pg.draw.line(scr, self.grid_color, [x, 0], [x, Y_SIZE], self.grid_width)

        for y in range(0, Y_SIZE, self.grid_size):
            pg.draw.line(scr, self.grid_color, [0, y], [X_SIZE, y], self.grid_width)

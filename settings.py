from random import choice
import pygame as pg
from math import sqrt, pi

FPS = 60

# SCREEN SIZE
Y_SIZE = HEIGHT = 700
X_SIZE = WIDTH = 1000
size = [WIDTH, HEIGHT]
HALF_HEIGHT = HEIGHT / 2
HALF_WIDTH = WIDTH / 2


# COLORS
BG_COLOR = 'black'
GRID_COLOR = 'green'

# SNAKE
SNAKE_DEFAULT_COLOR = 'green'
TILE = 20
SNAKE_SLOWLY_MOVE_TIMEOUT = 0.09
MAX_SNAKE_X = X_SIZE // TILE
MAX_SNAKE_Y = Y_SIZE // TILE
DEFAULT_SKIN = 0

WASD_CONTROL_SCHEME = {'up': pg.K_w, 'right': pg.K_d, 'down': pg.K_s, 'left': pg.K_a}
ARROWS_CONTROL_SCHEME = {'up': pg.K_UP, 'right': pg.K_RIGHT, 'down': pg.K_DOWN, 'left': pg.K_LEFT}

NUMBERS_OF_APPLES = 75

# FONTS
FIRST_LINE_SPACE = 5
DEFAULT_FONT_SIZE = 30
FONT_HEIGHT_SPACE = 24

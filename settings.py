from random import choice
import pygame as pg
from math import sqrt, pi

# SCREEN SIZE
Y_SIZE = HEIGHT = 700
X_SIZE = WIDTH = 1000
size = [WIDTH, HEIGHT]
HALF_HEIGHT = HEIGHT / 2
HALF_WIDTH = WIDTH / 2

# COLORS
BG_COLOR = 'black'

# SNAKE
SNAKE_DEFAULT_COLOR = 'green'
SNAKE_TILE = 10
SNAKE_SLOWLY_MOVE_TIMEOUT = 0.09
DEFAULT_CONTROL_SCHEME = {'up': pg.K_w, 'right': pg.K_d, 'down': pg.K_s, 'left': pg.K_a}
MAX_SNAKE_X = 8
MAX_SNAKE_Y = 8
DEFAULT_SKIN = 0

# FONTS
FIRST_LINE_SPACE = 5
DEFAULT_FONT_SIZE = 30
FONT_HEIGHT_SPACE = 24

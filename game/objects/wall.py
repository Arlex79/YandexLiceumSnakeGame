from game.additional.settings import *
from random import randint


class Wall:
    def __init__(self, x=None, y=None, the_size=1, color=WALL_COLOR):
        """Инициализация стены с заданными координатами, размером и цветом."""
        if x is None:
            self.x = randint(0, MAX_SNAKE_X - 1)
        else:
            self.x = x
        if y is None:
            self.y = randint(0, MAX_SNAKE_Y - 1)
        else:
            self.y = y

        self.size = the_size
        self.color = color

    def draw(self, scr):
        """Рисует стену на заданной поверхности."""
        pg.draw.rect(scr, self.color, pg.Rect(TILE * self.x, TILE * self.y, TILE, TILE))

    def draw_hitbox(self, scr):
        """Рисует хитбокс для стены на заданной поверхности."""
        pg.draw.rect(scr, self.color, pg.Rect(TILE * self.x, TILE * self.y, TILE, TILE), 1)

    def get_position(self):
        """Возвращает текущие координаты стены."""
        return self.x, self.y

    def is_collided(self, snake_head):
        """Проверяет, произошло ли столкновение с головой змеи."""
        return self.x == snake_head.x and self.y == snake_head.y

from game.additionall.settings import *
from random import randint


class Apple:
    def __init__(self, x=None, y=None, size=1, color='red'):
        if x is None:
            self.x = randint(0, MAX_SNAKE_X - 1)
        else:
            self.x = x
        if y is None:
            self.y = randint(0, MAX_SNAKE_Y - 1)
        else:
            self.y = y

        self.size = size
        self.color = color

    def draw(self, scr):
        """Отрисовывает яблоко на экране"""
        pg.draw.circle(scr, self.color, (TILE * self.x + TILE // 2, TILE * self.y + TILE // 2), TILE // 2)

    def draw_hitbox(self, scr):
        """Отображает хитбокс яблока"""
        pg.draw.rect(scr, self.color, pg.Rect(TILE * self.x, TILE * self.y, TILE, TILE), 1)

    def get_position(self):
        """Возвращает координаты яблока"""
        return self.x, self.y

    def respawn(self):
        """Перемещает яблоко на случайные координаты"""
        self.x = randint(0, MAX_SNAKE_X - 1)
        self.y = randint(0, MAX_SNAKE_Y - 1)

    def is_collided(self, snake_head):
        """Проверяет столкновение с головой змеи"""
        return self.x == snake_head.x and self.y == snake_head.y

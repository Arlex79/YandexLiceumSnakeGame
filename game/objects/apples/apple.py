from game.additional.settings import *
from random import randint


class Apple:
    image = pg.image.load(APPLE_IMG_PATH)
    image = pg.transform.scale(image, (TILE, TILE))

    def __init__(self, x=None, y=None, the_size=1, color=APPLE_COLOR):
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
        """Отрисовывает яблоко на экране"""
        scr.blit(self.image, (TILE * self.x, TILE * self.y))

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

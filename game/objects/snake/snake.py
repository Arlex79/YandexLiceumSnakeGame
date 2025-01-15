from copy import copy
from random import randint
from game.objects.hud import *

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


SNAKE_DEFAULT_SKINS = {'green': SnakeSkin('green', *(
                               list((0, i, 0) for i in range(70, 190, 5)))),
                       'red-orange-yellow': SnakeSkin('black', *(
                               list((i, 0, 0) for i in range(70, 190, 5)) +
                               list((0, i, 0) for i in range(190, 70, 5)) +
                               list((0, 0, i) for i in range(190, 70, 5)))),
                       'black-white': SnakeSkin('black', *(
                               list((i, i, i) for i in range(70, 190, 5)) +
                               list((i, i, i) for i in range(190, 70, -5)))),
                       'yellow-cyan': SnakeSkin('red', *(
                               list((i, i, 0) for i in range(70, 190, 10)) +
                               list((0, i, i) for i in range(190, 70, -10))))
                       }


def get_skin(name):
    try:
        if type(name) == str:
            skin = SNAKE_DEFAULT_SKINS[DEFAULT_SKIN]

        elif type(name) == int:
            skin = list(SNAKE_DEFAULT_SKINS.values())[name]

    except ValueError:
        skin = SnakeSkin('green', 'green')

    except IndexError:
        skin = list(SNAKE_DEFAULT_SKINS.values())[(len(SNAKE_DEFAULT_SKINS) - 1) % name]

    return skin


class SnakeBodySegment:
    def __init__(self, x=None, y=None):
        if x is None:
            self.x = randint(0, MAX_SNAKE_X)
        else:
            self.x = x

        if y is None:
            self.y = randint(0, MAX_SNAKE_Y)

        else:
            self.y = y


class Snake:
    def __init__(self, body=None, skin=None, control_scheme=WASD_CONTROL_SCHEME):
        self.control_scheme = control_scheme
        self.alive = True
        if randint(0, 1):
            self.dx = choice((-1, 1))
            self.dy = 0

        else:
            self.dx = 0
            self.dy = choice((-1, 1))
        self.body = []
        if body is None:
            first = SnakeBodySegment()
            self.body.append(first)
            self.body.append(SnakeBodySegment(first.x - self.dx, first.y - self.dy))

        else:
            self.body = body

        self.tick_last_time = time()

        if skin is None:
            if type(DEFAULT_SKIN) == str:
                self.skin = SNAKE_DEFAULT_SKINS[DEFAULT_SKIN]

            elif type(DEFAULT_SKIN) == int:
                self.skin = list(SNAKE_DEFAULT_SKINS.values())[DEFAULT_SKIN]

        else:
            self.skin = skin
        self.hud = SnakeHUD()

    def draw(self, scr):
        # body = self.body[::-1]
        for i in range(len(self.body)):
            snake_body_segment = self.body[i]
            x = snake_body_segment.x
            y = snake_body_segment.y

            pg.draw.rect(scr, self.skin.get_color_for_index(i),
                         pg.Rect(TILE * x, TILE * y, TILE, TILE))

            pg.draw.rect(scr, self.skin.get_color_for_index(0),
                         pg.Rect(TILE * x, TILE * y, TILE, TILE), 1)

    def draw_hitbox(self, scr):
        for i in range(len(self.body)):
            snake_body_segment = self.body[i]
            x = snake_body_segment.x
            y = snake_body_segment.y

            pg.draw.rect(scr, 'green',
                         pg.Rect(TILE * x, TILE * y, TILE, TILE), 1)

    def dead(self):
        self.alive = False
        self.dead_time = time()

    def move(self):
        head = self.body[0]
        del self.body[-1]

        self.body.insert(0, SnakeBodySegment(head.x + self.dx, head.y + self.dy))

    def get_move_timeout(self):
        return SNAKE_SLOWLY_MOVE_TIMEOUT

    def try_move_snake(self):
        if self.alive:
            now_ms = time()

            if (now_ms - self.tick_last_time) > self.get_move_timeout():
                self.tick_last_time = now_ms
                self.move()

    def add_segment(self, count=1):
        try:
            nasloyenie = self.body[0] == self.body[1]

        except IndexError:
            nasloyenie = False
        if self.alive and (len(self.body) >= 2 or len(self.body) == 1) and not nasloyenie:

            for i in range(count):
                snake_end = self.body[-1]
                self.body.append(copy(snake_end))

    def control(self, keys):
        if self.alive:
            new_dx, new_dy = None, None
            if keys[self.control_scheme['up']]:
                new_dx = 0
                new_dy = -1

            if keys[self.control_scheme['down']]:
                new_dx = 0
                new_dy = 1

            if keys[self.control_scheme['left']]:
                new_dx = -1
                new_dy = 0

            if keys[self.control_scheme['right']]:
                new_dx = 1
                new_dy = 0

            if not new_dx is None and not new_dy is None and new_dx != self.dx * -1 and new_dy != self.dy * -1:
                self.dx = new_dx
                self.dy = new_dy

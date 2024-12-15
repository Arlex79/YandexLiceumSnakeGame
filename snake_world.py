from snake import *
from time import time
from random import randint
from hud import HUD
from apple import Apple
from background import *


class SnakeWorld:
    def __init__(self):
        self.snakes = []
        self.apples = []
        self.inGameHud = HUD()
        self.bg = GridBackground()
        self.game_type = None

        self.isDrawHitbox = True
        self.isDrawSprites = False


    def new_game(self, game_type='single',
                 skins=[SnakeSkin('white', 'black', 'white'), SnakeSkin('red', 'green', 'blue', 'red')]):
        self.game_type = game_type
        self.snakes = []
        self.apples = [Apple() for i in range(NUMBERS_OF_APPLES)]
        if game_type == 'single':
            self.snakes.append(Snake(skin=skins[0], control_scheme=WASD_CONTROL_SCHEME))
        elif game_type == 'dual':
            self.snakes = [Snake(skin=skins[0], control_scheme=WASD_CONTROL_SCHEME),
                           Snake(skin=skins[1], control_scheme=ARROWS_CONTROL_SCHEME)]
        else:
            assert False
    def one_snake_is_alive(self):
        for snake in self.snakes:
            if snake.alive:
                return True

        return False
    def add_random_coords_snake(self):
        x = randint(0, MAX_SNAKE_X)
        y = randint(0, MAX_SNAKE_Y)

    def control_by_keyboard(self, keys):
        for snake in self.snakes:
            snake.control(keys)

    def move_snakes(self):
        for snake in self.snakes:
            snake.move()

    def move_snakes(self):
        for snake in self.snakes:
            snake.try_move_snake()

    def add_apple_to_map(self):
        notAllowCoords = []
        for snake in self.snakes:
            for segment in snake.body:
                notAllowCoords.append((segment.x, segment.y))

        while True:
            apple_x, apple_y = randint(0, MAX_SNAKE_X), randint(0, MAX_SNAKE_Y)
            if (apple_x, apple_y) not in notAllowCoords:
                self.apples.append(Apple(apple_x, apple_y))
                break

    def check_snakes_eat_apples(self):
        add_apples_count = 0
        for snake in self.snakes:
            head_x, head_y = snake.body[0].x, snake.body[0].y
            for apple in self.apples:
                if head_x == apple.x and head_y == apple.y:
                    snake.add_segment(apple.size)
                    self.apples.remove(apple)
                    add_apples_count += 1

                    break

        for i in range(add_apples_count):
            self.add_apple_to_map()

    def check_snakes_dead(self):
        deadCoords = []
        for snake in self.snakes:
            for segment in snake.body:
                deadCoords.append((segment.x, segment.y))
        deadSnakeList = []
        for snake in self.snakes:
            if len(snake.body) > 2 and snake.alive:
                head = (snake.body[0].x, snake.body[0].y)
                numberOfColision = 0
                for coords in deadCoords:
                    if head == coords:
                        numberOfColision += 1

                if numberOfColision > 1:
                    print('dead!!!')
                    deadSnakeList.append(snake)
                    snake.dead()

    def draw(self, scr):
        self.bg.draw(scr)
        for snake in self.snakes:
            snake.draw(scr)

        for apple in self.apples:
            apple.draw(scr)

        self.inGameHud.draw(scr)

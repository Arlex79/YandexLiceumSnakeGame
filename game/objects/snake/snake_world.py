from game.objects.apples.apple import Apple
from game.objects.apples.boost_apple import BoostApple
from game.objects.displays.background import *
from game.objects.snake.snake import *
from game.objects.displays.wall import *


class SnakeWorld:
    def __init__(self):
        self.inGameHud = InfoHUD()
        self.bg = GridBackground()
        self.game_type = None

        self.isDrawHitbox = True
        self.isDrawSprites = True

    def new_game(self, game_type='single', skins=[]):
        """Метод для инициализации новой игры"""
        self.game_type = game_type
        self.snakes = []
        self.apples = [Apple() for _ in range(NUMBERS_OF_APPLES)]
        self.boost_apples = [BoostApple() for _ in range(NUMBERS_OF_BOOST_APPLES)]
        self.walls = [Wall(randint(0, MAX_SNAKE_X), randint(0, MAX_SNAKE_Y)) for _ in range(NUMBERS_OF_WALLS)]

        # Добавляем змеи согласно типу игры
        if game_type == 'single':
            self.snakes.append(Snake(skin=skins[0], control_scheme=WASD_CONTROL_SCHEME))
        elif game_type == 'dual':
            self.snakes = [Snake(skin=skins[0], control_scheme=WASD_CONTROL_SCHEME),
                           Snake(skin=skins[1], control_scheme=ARROWS_CONTROL_SCHEME)]
        else:
            assert False

    def one_snake_is_alive(self):
        """Метод для проверки, есть ли как минимум одна живая змея"""
        for snake in self.snakes:
            if snake.alive:
                return True
        return False

    def control_by_keyboard(self, keys):
        """Метод для управления змеями с помощью клавиатуры"""
        for snake in self.snakes:
            snake.control(keys)

    def move_snakes(self):
        """Метод для перемещения всех змей"""
        for snake in self.snakes:
            snake.move()

    def move_snakes(self):
        """Метод для перемещения змей"""
        for snake in self.snakes:
            snake.try_move_snake()

    def add_apple_to_map(self, isBoost=False):
        """Метод для добавления яблока на карту, избегая координат змей"""
        bad_coords = []
        for wall in self.walls:
            bad_coords.append((wall.x, wall.y))
        for snake in self.snakes:
            for segment in snake.body:
                bad_coords.append((segment.x, segment.y))

        while True:
            """Генерация случайных координат для яблока"""
            apple_x, apple_y = randint(0, MAX_SNAKE_X), randint(0, MAX_SNAKE_Y)
            if (apple_x, apple_y) not in bad_coords:
                if isBoost:
                    self.apples.append(BoostApple(apple_x, apple_y))
                else:
                    self.apples.append(Apple(apple_x, apple_y))
                break

    def check_snakes_eat_apples(self):
        """Метод для проверки, съели ли змеи яблоки"""
        add_apples_count = add_boost_apples_count = 0
        for snake in self.snakes:
            head_x, head_y = snake.body[0].x, snake.body[0].y
            for apple in self.apples:
                if head_x == apple.x and head_y == apple.y:
                    snake.add_segment(apple.size)
                    self.apples.remove(apple)
                    add_apples_count += 1
                    break

            for boost_apple in self.boost_apples:
                if head_x == boost_apple.x and head_y == boost_apple.y:
                    snake.add_segment(boost_apple.size)
                    self.boost_apples.remove(boost_apple)
                    add_boost_apples_count += 1
                    break

        for i in range(add_apples_count):
            self.add_apple_to_map()
        for i in range(add_boost_apples_count):
            self.add_apple_to_map(isBoost=True)

    def check_snakes_dead(self):
        """Метод для проверки, мертвы ли змеи"""
        deadCoords = []
        for snake in self.snakes:
            for segment in snake.body:
                deadCoords.append((segment.x, segment.y))
        for wall in self.walls:
            deadCoords.append((wall.x, wall.y))

        for snake in self.snakes:
            head = (snake.body[0].x, snake.body[0].y)
            if head[0] < 0 or head[1] < 0 or head[0] >= MAX_SNAKE_X or head[
                1] >= MAX_SNAKE_Y:
                snake.dead()
            if len(snake.body) > 2 and snake.alive:
                numberOfColision = 0

                for coords in deadCoords:
                    if head == coords:
                        numberOfColision += 1

                if numberOfColision > 1:
                    snake.dead()

    def draw(self, scr, fps):
        """Метод для отрисовки мира змей"""
        self.bg.draw(scr)  # Отрисовываем фон
        for snake in self.snakes + self.apples + self.boost_apples + self.walls:
            if self.isDrawSprites:
                snake.draw(scr)
            if self.isDrawHitbox:
                snake.draw_hitbox(scr)

        # for apple in self.apples:
        #     if self.isDrawSprites:
        #         apple.draw(scr)
        #     if self.isDrawHitbox:
        #         apple.draw_hitbox(scr)
        #
        # for wall in self.walls:
        #     if self.isDrawSprites:
        #         wall.draw(scr)
        #     if self.isDrawHitbox:
        #         wall.draw_hitbox(scr)
        #
        # for boost_apple in self.boost_apples:
        #     if self.isDrawSprites:
        #         boost_apple.draw(scr)
        #     if self.isDrawHitbox:
        #         boost_apple.draw_hitbox(scr)

        self.inGameHud.draw(scr, *self.snakes, fps=fps)

from game.objects.hud import InfoHUD
from game.objects.apple import Apple
from game.objects.background import *
from game.objects.snake.snake import *


class SnakeWorld:
    def __init__(self):
        self.snakes = []  # Список для хранения объектов змей
        self.apples = []  # Список для хранения объектов яблок
        self.inGameHud = InfoHUD()  # Создаем HUD для отображения информации во время игры
        self.bg = GridBackground()  # Создаем объект фона игры
        self.game_type = None  # Задача для хранения типа игры

        # Флаги для отрисовки хитбоксов и спрайтов
        self.isDrawHitbox = False
        self.isDrawSprites = True

    def new_game(self, game_type='single', skins=[SnakeSkin('white', 'black', 'white'),
                                                  SnakeSkin('red', 'green', 'blue', 'red')]):
        """Метод для инициализации новой игры"""
        self.game_type = game_type  # Устанавливаем тип игры
        self.snakes = []  # Очищаем список змей
        self.apples = [Apple() for i in range(NUMBERS_OF_APPLES)]  # Генерируем яблоки

        # Добавляем змеи согласно типу игры
        if game_type == 'single':
            self.snakes.append(Snake(skin=skins[0], control_scheme=WASD_CONTROL_SCHEME))  # Один игрок
        elif game_type == 'dual':
            self.snakes = [Snake(skin=skins[0], control_scheme=WASD_CONTROL_SCHEME),  # Два игрока
                           Snake(skin=skins[1], control_scheme=ARROWS_CONTROL_SCHEME)]
        else:
            assert False  # Если тип игры не распознан, вызываем ошибку

    def one_snake_is_alive(self):
        """Метод для проверки, есть ли как минимум одна живая змея"""
        for snake in self.snakes:
            if snake.alive:  # Если змея жива
                return True
        return False  # Если все змеи мертвы

    def add_random_coords_snake(self):
        """Метод для добавления случайных координат для змеи"""
        x = randint(0, MAX_SNAKE_X)  # Генерируем случайный X
        y = randint(0, MAX_SNAKE_Y)  # Генерируем случайный Y

    def control_by_keyboard(self, keys):
        """Метод для управления змеями с помощью клавиатуры"""
        for snake in self.snakes:
            snake.control(keys)  # Передаем нажатые клавиши змеям

    def move_snakes(self):
        """Метод для перемещения всех змей"""
        for snake in self.snakes:
            snake.move()  # Двигаем каждую змею

    def move_snakes(self):
        """Метод для перемещения змей"""
        for snake in self.snakes:
            snake.try_move_snake()  # Попробовать переместить змею

    def add_apple_to_map(self):
        """Метод для добавления яблока на карту, избегая координат змей"""
        notAllowCoords = []  # Список недопустимых координат для яблок
        for snake in self.snakes:
            for segment in snake.body:
                notAllowCoords.append((segment.x, segment.y))  # Добавляем координаты тела змеи

        while True:
            """Генерация случайных координат для яблока"""
            apple_x, apple_y = randint(0, MAX_SNAKE_X), randint(0, MAX_SNAKE_Y)
            if (apple_x, apple_y) not in notAllowCoords:
                self.apples.append(Apple(apple_x, apple_y))  # Добавляем яблоко, если координаты допустимы
                break  # Выход из цикла

    def check_snakes_eat_apples(self):
        """Метод для проверки, съели ли змеи яблоки"""
        add_apples_count = 0  # Счетчик добавленных яблок
        for snake in self.snakes:
            head_x, head_y = snake.body[0].x, snake.body[0].y  # Получаем координаты головы змеи
            for apple in self.apples:
                if head_x == apple.x and head_y == apple.y:  # Если змея съела яблоко
                    snake.add_segment(apple.size)  # Увеличиваем змею на размер яблока
                    self.apples.remove(apple)  # Удаляем яблоко из списка
                    add_apples_count += 1  # Увеличиваем счетчик
                    break  # Выход из внутреннего цикла, чтобы не проверять остальные яблоки

        # Добавляем новые яблоки на карту по количеству съеденных
        for i in range(add_apples_count):
            self.add_apple_to_map()

    def check_snakes_dead(self):
        """Метод для проверки, мертвы ли змеи"""
        deadCoords = []  # Список координат тела змей
        for snake in self.snakes:
            for segment in snake.body:
                deadCoords.append((segment.x, segment.y))  # Добавляем координаты тела

        deadSnakeList = []  # Список для мертвых змей
        for snake in self.snakes:
            head = (snake.body[0].x, snake.body[0].y)  # Получаем координаты головы
            if head[0] < 0 or head[1] < 0 or head[0] >= MAX_SNAKE_X or head[
                1] >= MAX_SNAKE_Y:  # Проверяем столкновение со стенами
                snake.dead()
            if len(snake.body) > 2 and snake.alive:  # Проверяем, жива ли змея и имеет ли она более 2 сегментов
                numberOfColision = 0  # Счетчик столкновений

                for coords in deadCoords:
                    if head == coords:  # Если голова сталкивается с телом другой змеи
                        numberOfColision += 1

                if numberOfColision > 1:  # Если есть несколько пересечений
                    snake.dead()  # Вызываем метод, чтобы отметить змею как мертвую

    def draw(self, scr):
        """Метод для отрисовки мира змей"""
        self.bg.draw(scr)  # Отрисовываем фон
        for snake in self.snakes:
            if self.isDrawSprites:
                snake.draw(scr)  # Отрисовываем каждую змею
            if self.isDrawHitbox:
                snake.draw_hitbox(scr)  # Отрисовываем хитбокс

        for apple in self.apples:
            if self.isDrawSprites:
                apple.draw(scr)  # Отрисовываем каждое яблоко
            if self.isDrawHitbox:
                apple.draw_hitbox(scr) # Отрисовываем хитбокс


        self.inGameHud.draw(scr, *self.snakes)  # Отрисовываем интерфейс HUD

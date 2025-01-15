from game.objects.snake.snake import *
from game.additional.settings import *
from game.objects.snake.snake_world import SnakeWorld
from game.objects.background import Background
import csv


class Game:
    def __init__(self):
        pg.init()
        self.isDrawHitbox = True
        self.isDrawSprites = False
        self.scr = pg.display.set_mode(size)
        self.clock = pg.time.Clock()
        self.cheat = True
        self.running = True
        self.snake_world = SnakeWorld()
        self.inMenuBg = Background()
        self.state = 'main menu'
        self.activeGameType = 'single'
        self.csv_settings_file_path = "game/additional/settings.csv"
        self.read_settings()

    def update_skins(self):
        self.skins = []
        for i in self.skins_ids:
            self.skins.append(get_skin(int(i)))

    def read_settings(self):
        self.skins_ids = []
        with open(self.csv_settings_file_path, encoding="utf8") as csvfile:
            reader = csv.reader(csvfile, delimiter='=', quotechar='"')
            for index, row in enumerate(reader):
                if row[0] == "player1skin":
                    self.skins_ids.append(int(row[1]))

                elif row[0] == "player2skin":
                    self.skins_ids.append(int(row[1]))

        self.update_skins()

    def new_game(self, game_type='single'):  # type = single / dual
        self.running = True
        self.state = 'game'
        self.snake_world.new_game(game_type, skins=self.skins)

    def control(self):
        self.snake_world.control_by_keyboard()

    def draw_game(self):
        self.snake_world.draw(self.scr)

    def draw_multiline_text(self, text):
        spl_text = text.split('\n')
        for i in range(len(spl_text)):
            self.draw_text(spl_text[i], 10, (FONT_HEIGHT_SPACE * i) + FIRST_LINE_SPACE, color='white')

    def draw(self):
        self.scr.fill(BG_COLOR)

        if self.state == 'game':
            self.draw_game()

        if self.state == 'game over':
            self.inMenuBg.draw(self.scr)
            text = "Игра окончена!\n\nНажми Q для выхода в главное меню\nНажми пробел, чтобы играть снова"
            self.draw_multiline_text(text)

        if self.state == 'main menu':
            self.inMenuBg.draw(self.scr)
            text = f"""         Змейка
Нажмите 1 или 2 для выбора количества игроков
Нажмите пробел чтобы играть

Игроков: {self.get_game_type()}

Скин игрока 1 (wasd): {self.skins[0]}
Скин игрока 2 (стрелки): {self.skins[1]}"""

            self.draw_multiline_text(text)

    def get_game_type(self):
        match self.activeGameType:
            case 'single':
                return 1
            case 'dual':
                return 2

            case _:
                return self.activeGameType

    def draw_text(self, text, x=0, y=0, color='white', size=DEFAULT_FONT_SIZE, font_type='Courier New'):
        font = pg.font.SysFont(None, size)
        img = font.render(text, True, color)
        self.scr.blit(img, (x, y))

    def one_tick(self):
        if self.state == 'game':
            self.snake_world.move_snakes()
            self.snake_world.check_snakes_eat_apples()
            self.snake_world.check_snakes_dead()

    def game_over(self):
        self.state = 'game over'

    def try_edit_skin(self, skin_id, sdvig):
        if sdvig == 1:
            if self.skins_ids[skin_id] < len(SNAKE_DEFAULT_SKINS) - 1:
                self.skins_ids[skin_id] += 1
        elif sdvig == -1:
            if self.skins_ids[skin_id] > 0:
                self.skins_ids[skin_id] -= 1
        self.update_skins()

    def mainloop(self):
        while self.running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
                elif (event.type == pg.KEYDOWN):
                    if self.state == 'main menu':

                        if (event.key == pg.K_w):
                            self.try_edit_skin(0, 1)

                        elif (event.key == pg.K_s):
                            self.try_edit_skin(0, -1)
                        if (event.key == pg.K_UP):
                            self.try_edit_skin(1, 1)

                        elif (event.key == pg.K_down):
                            self.try_edit_skin(1, -1)
            keys = pg.key.get_pressed()
            self.one_tick()

            if self.state == 'game':
                if self.snake_world.one_snake_is_alive():
                    pos = pg.mouse.get_pos()
                    self.snake_world.control_by_keyboard(keys)
                    if keys[pg.K_r]:
                        self.new_game(self.activeGameType)
                    if keys[pg.K_y]:
                        for snake in self.snake_world.snakes:
                            snake.add_segment()

                    if keys[pg.K_q]:
                        self.state = 'main menu'

                else:
                    self.state = 'game over'

            elif self.state == 'game over':
                if keys[pg.K_q]:
                    self.state = 'main menu'

                elif keys[pg.K_SPACE]:
                    self.new_game(self.activeGameType)

            elif self.state == 'main menu':
                if keys[pg.K_SPACE]:
                    self.new_game(self.activeGameType)

                elif keys[pg.K_1]:
                    self.activeGameType = 'single'

                elif keys[pg.K_2]:
                    self.activeGameType = 'dual'


                elif keys[pg.K_ESCAPE]:
                    self.running = False

            self.draw()

            pg.display.flip()
            self.clock.tick(FPS)
        pg.quit()


if __name__ == '__main__':
    ga = Game()
    ga.mainloop()

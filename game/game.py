from game.objects.snake.snake import *
from game.additional.settings import *
from game.objects.snake.snake_world import SnakeWorld
from game.objects.background import Background
import csv
import sqlite3
from datetime import datetime as dt


class Game:
    def __init__(self):
        pg.init()
        pg.display.set_caption("Snake - Змейка")

        self.scr = pg.display.set_mode(size)
        self.clock = pg.time.Clock()
        self.cheat = True
        self.running = True
        self.snake_world = SnakeWorld()
        self.snake_world.isDrawHitbox = False
        self.snake_world.isDrawSprites = True
        self.inMenuBg = Background()
        self.state = 'main menu'
        self.activeGameType = 'single'
        self.csv_settings_file_path = "game/additional/settings.csv"
        self.read_settings()

        self.db_con = sqlite3.connect("game/game_records.sqlite")

        self.singleplayer_records = []
        self.dualplayer_records = []
        self.load_records()

    def get_time(self):
        time = dt.now()
        return time.strftime("%H:%M %d.%m.%Y")

    def load_records(self):
        self.singleplayer_records = []
        self.dualplayer_records = []
        cur = self.db_con.cursor()
        result_singleplayer = cur.execute("""SELECT * FROM singleplayer ORDER BY score DESC
        """).fetchall()
        for elem in result_singleplayer:
            self.singleplayer_records.append(elem)

        result_dualplayer = cur.execute("""SELECT * FROM dualplayer ORDER BY score1 + score2 DESC
        """).fetchall()
        for elem in result_dualplayer:
            self.dualplayer_records.append(elem)

    def log_record(self, game_type='single', score1=0, score2=0):
        time_now = self.get_time()
        cur = self.db_con.cursor()
        if game_type == 'single':
            cur.execute(f"""INSERT INTO singleplayer(date, score) VALUES('{time_now}', {score1}) 
                   """)
        elif game_type == "dual":
            cur.execute(f"""INSERT INTO dualplayer(date, score1, score2) 
            VALUES('{time_now}', {score1}, {score2}) 
                               """)
        self.db_con.commit()

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

    def write_settings(self):
        import csv
        with open(self.csv_settings_file_path, 'w', newline='') as f:
            writer = csv.writer(f, delimiter="=")
            writer.writerows([["player1skin", self.skins_ids[0]], ["player2skin", self.skins_ids[1]]])

    def new_game(self, game_type='single'):  # type = single / dual
        self.running = True
        self.state = 'game'
        self.snake_world.new_game(game_type, skins=self.skins)

    def control(self):
        self.snake_world.control_by_keyboard()

    def draw_game(self):
        self.snake_world.draw(self.scr, int(self.clock.get_fps()))

    def draw_multiline_text(self, text):
        spl_text = text.split('\n')
        for i in range(len(spl_text)):
            self.draw_text(spl_text[i], 10, (FONT_HEIGHT_SPACE * i) + FIRST_LINE_SPACE, color='white')

    def draw(self):
        self.scr.fill(BG_COLOR)

        if self.state == 'game':
            self.draw_game()

        elif self.state == 'game over':
            self.inMenuBg.draw(self.scr)
            text = "Игра окончена!\n\nНажми Q для выхода в главное меню\nНажми пробел, чтобы играть снова"
            self.draw_multiline_text(text)
        elif self.state == "records view":
            self.inMenuBg.draw(self.scr)
            singleplayers = ""
            for i, v in enumerate(self.singleplayer_records[:10]):
                singleplayers += f"{str(i + 1).rjust(2)}. {v[1]} - {v[2]}\n"
            dualplayers = ""
            for i, v in enumerate(self.dualplayer_records[:10]):
                dualplayers += f"{str(i + 1).rjust(2)}. {v[1]} - {v[2]}:{v[3]}\n"
            text = f'''Просмотр игровых рекордов
Нажмите Q для возврата в главное меню

Однопользовательская игра:
{singleplayers}
Двупользовательская игра:
{dualplayers}

            '''
            self.draw_multiline_text(text)
        elif self.state == 'main menu':
            self.inMenuBg.draw(self.scr)
            text = f"""Змейка

Нажмите 1 или 2 для выбора количества игроков
Нажмите пробел чтобы играть
Нажмите E для просмотра рекордов

Игроков: {self.get_game_type()}

Скин игрока 1 (wasd): {self.skins[0]}
Скин игрока 2 (стрелки): {self.skins[1]}

Github: github.com/Arlex79/YandexLiceumSnakeGame"""

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
        self.write_settings()

    def finish_game(self):
        if self.activeGameType == 'single':
            self.log_record(self.activeGameType,
                            self.snake_world.snakes[0].getScore())
        elif self.activeGameType == 'dual':
            self.log_record(self.activeGameType,
                            self.snake_world.snakes[0].getScore(),
                            self.snake_world.snakes[1].getScore())
        self.load_records()

    def mainloop(self):
        while self.running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
                elif event.type == pg.KEYDOWN:
                    if self.state == 'main menu':
                        if event.key == pg.K_w:
                            self.try_edit_skin(0, 1)

                        elif event.key == pg.K_s:
                            self.try_edit_skin(0, -1)
                        if event.key == pg.K_UP:
                            self.try_edit_skin(1, 1)

                        elif event.key == pg.K_DOWN:
                            self.try_edit_skin(1, -1)

                    if self.state == 'main menu':
                        if event.key == pg.K_e:
                            self.state = 'records view'

                        elif event.key == pg.K_1:
                            self.activeGameType = 'single'

                        elif event.key == pg.K_2:
                            self.activeGameType = 'dual'


                        elif event.key == pg.K_q:
                            self.running = False

                    elif self.state == 'game over':
                        if event.key == pg.K_q:
                            self.state = 'main menu'

                    if self.state == 'records view':
                        if event.key == pg.K_q:
                            self.state = 'main menu'

            keys = pg.key.get_pressed()
            self.one_tick()

            if self.state == 'game':
                if self.snake_world.one_snake_is_alive():

                    self.snake_world.control_by_keyboard(keys)
                    if keys[pg.K_r]:
                        self.new_game(self.activeGameType)
                    if keys[pg.K_y]:
                        for snake in self.snake_world.snakes:
                            snake.add_segment()

                    if keys[pg.K_q]:
                        self.finish_game()
                        self.state = 'main menu'

                else:
                    self.state = 'game over'
                    self.finish_game()

            elif self.state == 'records view':
                pass

            elif self.state == 'game over':
                if keys[pg.K_SPACE]:
                    self.new_game(self.activeGameType)

            elif self.state == 'main menu':
                if keys[pg.K_SPACE]:
                    self.new_game(self.activeGameType)

            self.draw()

            pg.display.flip()
            self.clock.tick(FPS)
        pg.quit()
        self.db_con.close()


if __name__ == '__main__':
    ga = Game()
    ga.mainloop()
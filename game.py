import pygame as pg
from snake import *
from settings import *
from snake_world import SnakeWorld
from time import time
from background import Background

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
        self.inNenuBg = Background()
        self.state = 'main menu'
        self.activeGameType = 'single'
        self.skins = [get_skin(0), get_skin(60)]


    def new_game(self, game_type='single'):  # type = single / duo
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
            self.inNenuBg.draw(self.scr)
            text = "Игра окончена!\n\nНажми Q для выхода в главное меню\nНажми пробел, чтобы играть снова"
            self.draw_multiline_text(text)

        if self.state == 'main menu':
            self.inNenuBg.draw(self.scr)
            text = f"""----------< Змейка >----------\n\nНажми 1 для выбора однопользовательской игры\nНажми 2 для выбора двупользовательской игры\n
Нажми пробел чтобы играть в режиме {self.get_russian_game_type()}!\n\nверсия 0.1"""

            self.draw_multiline_text(text)
    def get_russian_game_type(self):
        match self.activeGameType:
            case 'single':
                return 'однопользовательская игра'
            case 'dual':
                return 'двупользовательская игра'

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

    def mainloop(self):

        while self.running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False

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

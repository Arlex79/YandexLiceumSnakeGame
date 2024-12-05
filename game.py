import pygame as pg

from settings import *


class Game:
    def __init__(self):
        pg.init()
        self.scr = pg.display.set_mode(size)
        self.clock = pg.time.Clock()
        self.cheat = True
        self.running = True
        self.state = 'main menu'

    def new_game(self):
        self.running = True
        self.state = 'game'

    def draw_game(self):
        self.draw_multiline_text("""GAME!!!""")

    def draw_multiline_text(self, text):
        spl_text = text.split('\n')
        for i in range(len(spl_text)):
            self.draw_text(spl_text[i], 10, (FONT_HEIGHT_SPACE * i) + FIRST_LINE_SPACE, color='white')

    def draw(self):
        self.scr.fill(BG_COLOR)
        if self.state == 'game':
            self.draw_game()

        if self.state == 'game over':
            text = "GAME OVER!\nPREES SPACE TO PLAY"
            self.draw_multiline_text(text)

        if self.state == 'main menu':
            text = f"MAIN MENU\nPREES SPACE TO PLAY\n" \
                   f"PREES R TO RESTART"
            self.draw_multiline_text(text)

    def draw_text(self, text, x=0, y=0, color='white', size=DEFAULT_FONT_SIZE, font_type='Courier New'):
        font = pg.font.SysFont(None, size)
        img = font.render(text, True, color)
        self.scr.blit(img, (x, y))

    def one_tick(self):
        if self.state == 'game':
            pass

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
                pos = pg.mouse.get_pos()
                if keys[pg.K_r]:
                    self.new_game()
                if keys[pg.K_q]:
                    self.state = 'main menu'

            elif self.state == 'game over':
                if keys[pg.K_SPACE]:
                    self.new_game()

            elif self.state == 'main menu':
                if keys[pg.K_SPACE]:
                    self.new_game()

            self.draw()

            pg.display.flip()
            self.clock.tick(30)
        pg.quit()


if __name__ == '__main__':
    ga = Game()
    ga.mainloop()

from time import time
from game.additional.settings import *


class HUD:
    def __init__(self):
        self.start_time = time()
        self.font = pg.font.SysFont(None, DEFAULT_FONT_SIZE)

    def draw_text(self, scr, text, x=0, y=0, color='white', size=DEFAULT_FONT_SIZE, font_type='Courier New'):
        font = pg.font.SysFont(None, size)
        img = font.render(text, True, color)
        scr.blit(img, (x, y))

    def draw_multiline_text(self, scr, text):
        spl_text = text.split('\n')
        for i in range(len(spl_text)):
            self.draw_text(scr, str(spl_text[i]), 10, (FONT_HEIGHT_SPACE * i) + FIRST_LINE_SPACE,
                           color='white')

    def draw(self, scr):
        pass


class InfoHUD(HUD):
    def __init__(self):
        super().__init__()

    def draw(self, scr, snake1, snake2=None, fps=None):
        snake1text = f"Змея 1 (wasd): {snake1.getScore()}"
        if not snake2 is None:
            snake2text = f"Змея 2 (стрелки): {snake2.getScore()}"
        else:
            snake2text = ""
        self.draw_multiline_text(scr, f'''Игра Змейка FPS: {fps}
{snake1text}
{snake2text}''')

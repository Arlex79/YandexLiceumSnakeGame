from time import time
from game.additional.settings import *


class HUD:
    def __init__(self):
        self.start_time = time()
        self.font = pg.font.SysFont(None, DEFAULT_FONT_SIZE)

    def draw_text(self, scr, text, x=0, y=0, color='white', the_size=DEFAULT_FONT_SIZE, font_type='Courier New'):
        """Рисует текст на заданной поверхности."""
        font = pg.font.SysFont(None, the_size)
        img = font.render(text, True, color)
        scr.blit(img, (x, y))

    def draw_multiline_text(self, scr, text):
        """Рисует многострочный текст на заданной поверхности."""
        spl_text = text.split('\n')
        for i in range(len(spl_text)):
            self.draw_text(scr, str(spl_text[i]),  10, (FONT_HEIGHT_SPACE * i) + FIRST_LINE_SPACE,
                           color='white')

    def draw(self, scr):
        """Отрисовка HUD."""
        pass


class InfoHUD(HUD):
    def __init__(self):
        super().__init__()

    def draw(self, scr,  snake1, snake2=None, fps=None):
        """Рисует информацию о состоянии игры на заданной поверхности."""
        snake1text = f"Змея 1 (wasd): {snake1.getScore()}"
        if snake2 is not None:
            snake2text = f"Змея 2 (стрелки): {snake2.getScore()}"
        else:
            snake2text = ""
        self.draw_multiline_text(scr, f'''Игра Змейка FPS: {fps}
{snake1text}
{snake2text}''')


class SnakeHUD(HUD):
    def __init__(self):
        super().__init__()

    def draw(self, scr):
        """Рисует текст "Snake hud" на заданной поверхности."""
        self.draw_multiline_text(scr, '''Snake hud''')

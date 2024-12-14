from time import time
from settings import *
class HUD:
    def __init__(self):
        self.start_time = time()

    def draw_text(self, scr, text, x=0, y=0, color='white', size=DEFAULT_FONT_SIZE, font_type='Courier New'):
        font = pg.font.SysFont(None, size)
        print(f'{text}')
        img = font.render(text, True, color)
        scr.blit(img, (x, y))

    def draw_multiline_text(self, scr, text):
        spl_text = text.split('\n')
        for i in range(len(spl_text)):
            self.draw_text(scr, str(spl_text[i]), 10, (FONT_HEIGHT_SPACE * i) + FIRST_LINE_SPACE, color='white')
    def draw(self, scr):
        self.draw_multiline_text(scr, '''Game at play\nPrees Y!''')

from time import time
from settings import *
class HUD:
    def __init__(self):
        self.start_time = time()
        self.font = pg.font.SysFont(None, DEFAULT_FONT_SIZE)

    def draw_text(self, scr, text, font, x=0, y=0, color='white', size=DEFAULT_FONT_SIZE, font_type='Courier New'):

        img = font.render(text, True, color)
        scr.blit(img, (x, y))

    def draw_multiline_text(self, scr, text):
        spl_text = text.split('\n')
        for i in range(len(spl_text)):
            self.draw_text(scr, str(spl_text[i]), self.font, 10, (FONT_HEIGHT_SPACE * i) + FIRST_LINE_SPACE, color='white')
    def draw(self, scr):
        self.draw_multiline_text(scr, '''Game at play\nPrees Y!''')
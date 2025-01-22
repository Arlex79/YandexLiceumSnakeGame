from game.additional.settings import *



class Wall:
    def __init__(self, x=None, y=None, size=1, color=WALL_COLOR):
        self.x = x
        self.y = y

        self.size = size
        self.color = color

    def draw(self, scr):
        pg.draw.rect(scr, self.color, pg.Rect(TILE * self.x, TILE * self.y, TILE, TILE))

    def draw_hitbox(self, scr):
        pg.draw.rect(scr, "violet", pg.Rect(TILE * self.x, TILE * self.y, TILE, TILE), 1)

    def get_position(self):
        return self.x, self.y

    def is_collided(self, snake_head):
        return self.x == snake_head.x and self.y == snake_head.y

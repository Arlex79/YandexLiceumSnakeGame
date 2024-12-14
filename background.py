class Background:
    def __init__(self, color='#333d48', image_filename=None):
        self.color = color
        self.image_filename = image_filename

    def draw(self, scr):
        scr.fill(self.color)
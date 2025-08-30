from config import *

class Singer:
    def __init__(self, pos):
        self.size = 100, 200
        self.color = 'red'
        self.rect = Rect(*pos, *self.size)
        self.sound  = None

    def reset(self):
        draw.rect(window, self.color, self.rect)

    def start_singing(self):
        if self.sound:
            self.sound.play(-1)

    def stop_singing(self):
        if self.sound:
            self.sound.stop()

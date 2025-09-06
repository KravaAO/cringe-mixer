from config import *

# --- КАРТИНКИ ---
image_size = 160, 160
IDLE_1_IMG = transform.scale(image.load('assets/images/singer/idle_1.png'), image_size)
IDLE_2_IMG = transform.scale(image.load('assets/images/singer/idle_2.png'), image_size)

SINGING_1_IMG = transform.scale(image.load('assets/images/singer/singing_1.png'), image_size)
SINGING_2_IMG = transform.scale(image.load('assets/images/singer/singing_2.png'), image_size)
SINGING_3_IMG = transform.scale(image.load('assets/images/singer/singing_3.png'), image_size)


class Singer:
    def __init__(self, pos):
        self.size = 160, 160
        self.color = 'red'
        self.rect = Rect(*pos, *self.size)
        self.sound  = None
        self.wait = 20
        self.idle_frames = [IDLE_1_IMG, IDLE_2_IMG]
        self.singing_frames = [SINGING_1_IMG, SINGING_2_IMG, SINGING_3_IMG]
        self.current_img = 0

    def reset(self, is_singing=False):
        if self.wait == 0:
            if not self.sound:
                if self.current_img + 1 < len(self.idle_frames):
                    self.current_img += 1
                else:
                    self.current_img = 0
                self.wait = 60
            else:
                if self.current_img + 1 < len(self.singing_frames):
                    self.current_img += 1
                else:
                    self.current_img = 0
                self.wait = 20
        else:
            self.wait -= 1

        if not self.sound:
            window.blit(self.idle_frames[self.current_img], (self.rect.x, self.rect.y))
        else:
            if is_singing:
                window.blit(self.singing_frames[self.current_img], (self.rect.x, self.rect.y))
            else:
                window.blit(self.idle_frames[0], (self.rect.x, self.rect.y))

       #draw.rect(window, self.color, self.rect, 2)

    def start_singing(self):
        if self.sound:
            self.sound.set_volume(0.1)
            self.sound.play(-1)

    def stop_singing(self):
        if self.sound:
            self.sound.stop()

from config import *


class Button:
    font = font.Font(None, 30)
    def __init__(self, pos, size, btn_color='grey', border_radius=15, text=None, text_color='black',img_path=None, img_size=None, sound_path=None):
        self.rect = Rect(*pos, *size)
        self.color = btn_color
        self.text_color = text_color
        self.img = img_path
        self.text = text
        self.border_radius = border_radius
        if text:
            self.text = self.font.render(text, 1, text_color)
        if img_path and img_size:
            self.img = transform.scale(image.load(img_path), img_size)
        elif img_path:
            self.img = image.load(img_path)
        self.sound = sound_path

    def click(self, pos):
        if self.rect.collidepoint(pos): return True
        return False

    def reset(self):
        if self.img and self.text:
            window.blit(self.img, (self.rect.x, self.rect.y))
            window.blit(self.text, (self.rect.x, self.rect.y))
        elif self.img:
            window.blit(self.img, (self.rect.x, self.rect.y))
        else:
            draw.rect(window, self.color, self.rect, border_radius=self.border_radius)

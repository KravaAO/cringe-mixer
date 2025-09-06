from pygame import *

init()
mixer.init()
WIDTH = 1200
HEIGHT = 800
window_size = WIDTH, HEIGHT
window  = display.set_mode(window_size)
clock = time.Clock()

PLAY_STOP_BTN_SIZE = 100, 100

# --- ПІДКЛЮЧЕННЯ КАРТИНОК ---
BG_IMG = transform.scale(image.load('assets/images/bg.png'), window_size)
PLAY_BUTTON_PATH = 'assets/images/ui/play.png'

PLAY_BUTTON_IMG = transform.scale(image.load('assets/images/ui/play.png'), PLAY_STOP_BTN_SIZE)
STOP_BUTTON_IMG = transform.scale(image.load('assets/images/ui/stop.png'), PLAY_STOP_BTN_SIZE)
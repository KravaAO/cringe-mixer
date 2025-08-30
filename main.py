from config import *
from Button import Button
from singer import Singer

buttons = [
    Button((50, 500), (50, 50), sound_path='assets/sounds/sound_1.wav'),
    Button((150, 500), (50, 50), sound_path='assets/sounds/sound_2.wav'),
    Button((250, 500), (50, 50), sound_path='assets/sounds/sound_3.wav'),
]

singers = [
    Singer((150,  250)),
    Singer((350, 250)),
    Singer((550, 250)),
]

play_btn = Button((1000, 20), (100, 100))
running = True
singing = False
sound_path = None
sound_play = False
while running:
    for e in event.get():
        if e.type == QUIT:
            quit()
        if e.type == MOUSEBUTTONDOWN:
            for btn in buttons:
                if btn.click(e.pos):
                    sound_path = btn.sound
                    print(btn.sound)
            for singer in singers:
                if singer.rect.collidepoint(e.pos) and sound_path:
                    singer.sound = mixer.Sound(sound_path)
                    singer.color = 'blue'
                    print('присвохди мелодію', sound_path)
                    sound_path = None
            if play_btn.click(e.pos):
                singing = True
                if not sound_play:
                    sound_play = True
                else:
                    sound_play = False

    window.fill((100, 100, 100))

    for btn in buttons:
        btn.reset()
    for singer in singers:
        singer.reset()
    play_btn.reset()
    display.update()
    clock.tick(60)
    if not sound_play:
        for singer in singers:
            singer.stop_singing()
    if singing:
        for singer in singers:
            singer.start_singing()
        singing = False

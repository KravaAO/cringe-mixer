from config import *
from Button import Button
from singer import Singer

buttons = [
    Button((50,  700), (50, 50), sound_path='assets/sounds/sound_1.wav'),
    Button((150, 700), (50, 50), sound_path='assets/sounds/sound_2.wav'),
    Button((250, 700), (50, 50), sound_path='assets/sounds/sound_3.wav'),
    Button((350, 700), (50, 50), sound_path='assets/sounds/mutant_frog-1.ogg'),
]

singers = [
    Singer((200,  390)),
    Singer((400,  390)),
    Singer((600,  390)),
    Singer((800,  390)),
]

play_btn = Button((550, 200), PLAY_STOP_BTN_SIZE, img_path=PLAY_BUTTON_PATH, img_size=PLAY_STOP_BTN_SIZE)
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
                    if not singer.sound:
                        singer.sound = mixer.Sound(sound_path)
                        singer.color = 'blue'
                        print('присвохди мелодію', sound_path)
                        sound_path = None
            if play_btn.click(e.pos):
                singing = True

                if not sound_play:
                    play_btn.img = STOP_BUTTON_IMG
                    sound_play = True
                else:
                    sound_play = False
                    play_btn.img = PLAY_BUTTON_IMG

    window.fill((100, 100, 100))
    window.blit(BG_IMG, (0, 0))
    for btn in buttons:
        btn.reset()
    for singer in singers:
        singer.reset(sound_play)
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

import pygame
import random

songs = ['doom_02. Rip & Tear.mp3',
         '[MV] ロキ _ Roki (English Rap Cover) - Calliope Mori.mp3',
         'YOASOBI「怪物」_スターアニマル (ときのそら・星街すいせい・大空スバル・尾丸ポルカ・博衣こより・沙花叉クロヱ) cover.mp3',]

SONG_END = pygame.USEREVENT + 1
def playing_music(i):
    pygame.mixer.music.set_endevent(SONG_END)
    pygame.mixer.music.load(songs[i])
    pygame.mixer.music.play(0)


pygame.init()
screen = pygame.display.set_mode((400, 300))
running = True
i = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                pygame.mixer.music.stop()
                i += 1
                if i > len(songs) - 1:
                    i = 0
                playing_music(i)
            elif event.key == pygame.K_LEFT:
                pygame.mixer.music.stop()
                i -= 2
                if i > 0 or i<0:
                    i = len(songs) -2    

                playing_music(i)
        if event.type == SONG_END:
            i += 1
            if i > len(songs) - 1:
                i = 0
            playing_music(i)
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_SPACE]:
        playing_music(i)
    if pressed[pygame.K_UP]:
        pygame.mixer.music.pause()
    if pressed[pygame.K_DOWN]:
        pygame.mixer.music.unpause()

    pygame.display.flip()
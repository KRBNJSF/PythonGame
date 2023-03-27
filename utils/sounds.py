import pygame.mixer

from settings import Settings


class Sounds:
    bg_music = pygame.mixer.Sound(Settings.MUSIC_PREFIX + "bg_music.wav")
    bg_music.set_volume(.1)

    collect = pygame.mixer.Sound(Settings.MUSIC_PREFIX + "collect.mp3")
    collect.set_volume(.1)

    win = pygame.mixer.Sound(Settings.MUSIC_PREFIX + "victory.wav")
    win.set_volume(.1)

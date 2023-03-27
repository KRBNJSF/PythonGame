import pygame

from settings import Settings


class Utils:
    def convertHeight(self):
        pass

    def play_music(self):
        pygame.mixer.music.load(Settings.MUSIC_PREFIX + self)
        pygame.mixer.music.set_volume(1)
        pygame.mixer.music.play()

    def pause_music(self):
        pygame.mixer.music.pause(self)

    def stop_music(self):
        pygame.mixer.music.stop()

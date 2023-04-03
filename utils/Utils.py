import pygame

from settings import Settings


class Utils:
    def convertHeight(self):
        pass

    def play_music(self):
        pygame.mixer.music.load(Settings.MUSIC_PREFIX + self)
        pygame.mixer.music.set_volume(.1)
        pygame.mixer.music.play(-1)

    @staticmethod
    def pause_music():
        pygame.mixer.music.pause()

    @staticmethod
    def stop_music():
        pygame.mixer.music.stop()

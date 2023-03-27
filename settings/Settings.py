import pygame

pygame.init()
pygame.mixer.init()

my_font = pygame.font.SysFont("Comic Sans MS", 40)
small_font = pygame.font.SysFont("Comic Sans MS", 20)
restart_font = pygame.font.SysFont("Comic Sans MS", 80)

isRunning = True
isGame = True

SCREEN_WIDTH = pygame.display.Info().current_w
SCREEN_HEIGHT = pygame.display.Info().current_h
SCALE = 3
seconds = 1.3

BLACK = (0, 0, 0)
BACKGROUND_COLOR = (136, 89, 47)

IMG_PREFIX = "./assets/"
MUSIC_PREFIX = "./assets/music/"

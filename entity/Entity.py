import pygame


class Entity:

    def __init__(self, x, y, width, height, image):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = image

    def drawObject(self, path):
        img = pygame.image.load("assets/" + path).convert_alpha()
        img = pygame.transform.flip(self.image, self.direction, False)
        img = pygame.transform.scale(self.image, (self.width, self.height))

import pygame


class Player:
    MAX_SCORE = 10

    def __init__(self, x, y, width, height, score, direction, velocity, boost, image, isPressed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.score = score
        self.direction = direction
        self.velocity = velocity
        self.boost = boost
        self.image = image
        self.isPressed = isPressed

    def drawObject(self, path):
        img = pygame.image.load("assets/" + path).convert_alpha()
        img = pygame.transform.flip(self.image, self.direction, False)
        img = pygame.transform.scale(self.image, (self.width, self.height))

class Entity:
    X = 0
    Y = 0

    def __init__(self, height, width, x, y, score, image, direction, velocity):
        self.height = height
        self.width = width
        self.x = x
        self.y = y
        self.score = score
        self.image = image
        self.direction = direction
        self.velocity = velocity

    def drawObject(self):
        pass

class Entity:
    X = 0
    Y = 0

    def __init__(self, height, width, x, y, score, image, direction, velocity, boost):
        self.height = height
        self.width = width
        self.x = x
        self.y = y
        self.score = score
        self.image = image
        self.direction = direction
        self.velocity = velocity
        self.boost = boost

    def drawObject(self):
        pass

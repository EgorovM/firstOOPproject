class Bullet:
    def __init__(self, x, y, traektory, speed=10):
        """
        x, y int - current position
        Traektory tuple(3) - (A, B, C) of equency
        """

        self.x = x
        self.y = y
        self.speed = speed
        self.traektory = traektory

    def getCoords(self):
        """
        return tuple of coords
        """

        return (self.x, self.y)

    def run(self):
        A, B, C = self.traektory

        self.x += self.speed
        self.y = -(A*self.x + C) / B

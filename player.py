import portalGun
import bullet
import config
import math
import api

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.portalGun = portalGun.PortalGun()

    def goLeft(self):
        self.x -= 1

    def goRight(self):
        self.x += 1

    def goUp(self):
        self.y -= 1

    def goDown(self):
        self.y += 1

    def shoot(self, x, y):
        curr_y = int((self.y + 0.5) * config.CELL_HEIGHT)
        curr_x = int((self.x + 0.5) * config.CELL_WIDTH)

        A, B, C = api.getLineEq(
            x,
            y,
            curr_x,
            curr_y,
        )

        speed = math.copysign(1, x - curr_x) * 20

        self.portalGun._bullet = bullet.Bullet(curr_x, curr_y, (A, B, C), speed)
        self.portalGun.changePortal()

    def getCoords(self):
        return self.x, self.y

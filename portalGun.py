import config
import api

class Portal:
    def __init__(self, id, x=-1, y=-1, color=config.GREEN):
        self.id = id
        self._x = x
        self._y = y
        self._color = color
        self.activate = False

    def changeCoords(self, x, y):
        self._x = x
        self._y = y

    def getId(self):
        return self.id

    def __eq__(self, other):
        return self.id == other.getId()

    def display(self):
        print(f"Portal №{self.id}")
        print(f"x = {self._x}, y = {self._y}")
        print()

class PortalGun:
    def __init__(self, ):
        self.portal1 = Portal(1, color=config.GREEN)
        self.portal2 = Portal(2, color=config.RED)
        self._bullet = None

        self.curr_portal = self.portal1

    def pastePortal(self, x, y):
        self.curr_portal.changeCoords(x, y)
        self.curr_portal.activate = True

    def changePortal(self):
        print(self.curr_portal.display())
        if self.curr_portal == self.portal1:
            self.curr_portal = self.portal2
        else:
            self.curr_portal = self.portal1

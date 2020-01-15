import pygame
import config
import api

class Game:
    def __init__(self, player):
        self.grid = [
            [1,1,1,1,1,1,1],
            [1,0,0,0,1,0,1],
            [1,0,0,0,0,0,1],
            [1,1,1,0,0,1,1],
            [1,1,1,1,0,0,1],
            [1,0,0,0,0,0,1],
            [1,1,1,1,1,1,1],
        ]

        self.player = player
        self.screen = pygame.display.set_mode(config.WINDOW_SIZE)

    def drawGrid(self, Bullet=None):
        for row in range(7):
            for column in range(7):
                color = config.WHITE

                if self.grid[row][column] == 1:
                    color = config.BLACK

                pygame.draw.rect(
                    self.screen,
                    color,
                    [(config.CELL_WIDTH) * column ,
                    (config.CELL_HEIGHT) * row,
                    config.CELL_WIDTH,
                    config.CELL_HEIGHT]
                )

        if not self.player.portalGun._bullet is None:
            bullet = self.player.portalGun._bullet

            row, col = api.getCellByCoords(bullet.x, bullet.y)

            if row >= 0 and row < len(self.grid[0]) and col >= 0 and col < len(self.grid) and self.grid[col][row] == 1:
                self.player.portalGun.pastePortal(row, col)
                bullet = None
            else:
                pygame.draw.circle(self.screen, config.RED, (int(bullet.x), int(bullet.y)), 3)
                bullet.run()

        if self.player.portalGun.portal1.activate:
            portal = self.player.portalGun.portal1

            pygame.draw.rect(
                self.screen,
                portal._color,
                [(config.CELL_WIDTH) * portal._x,
                 (config.CELL_HEIGHT) * portal._y,
                 config.CELL_WIDTH,
                 config.CELL_HEIGHT]
            )

        if self.player.portalGun.portal2.activate:
            portal = self.player.portalGun.portal2

            pygame.draw.rect(
                self.screen,
                portal._color,
                [(config.CELL_WIDTH) * portal._x,
                 (config.CELL_HEIGHT) * portal._y,
                 config.CELL_WIDTH,
                 config.CELL_HEIGHT]
            )

        #person
        pygame.draw.rect(
            self.screen,
            config.RED,
            [(config.CELL_WIDTH) * self.player.x,
             (config.CELL_HEIGHT) * self.player.y,
             config.CELL_WIDTH,
             config.CELL_HEIGHT]
        )

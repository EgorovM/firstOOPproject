import pygame
import config
import player
import game
import api

pygame.init()
pygame.display.set_caption(config.GAMENAME)

player = player.Player(1,1)

game = game.Game(player)
game.screen.fill(config.BLACK)

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            curr_y, curr_x = game.player.getCoords()

            if event.key == pygame.K_w:
                if game.grid[curr_x - 1][curr_y] == 0:
                    player.goUp()
            if event.key == pygame.K_d:
                if game.grid[curr_x][curr_y + 1] == 0:
                    player.goRight()
            if event.key == pygame.K_s:
                if game.grid[curr_x + 1][curr_y] == 0:
                    player.goDown()
            if event.key == pygame.K_a:
                if game.grid[curr_x][curr_y - 1] == 0:
                    player.goLeft()
                    
        if event.type == pygame.MOUSEBUTTONUP:
            x, y = pygame.mouse.get_pos()
            player.shoot(x, y)

    game.screen.fill(config.BLACK)

    game.drawGrid()

    pygame.display.update()

pygame.quit()

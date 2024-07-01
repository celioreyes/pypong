"""
Multiplayer Pong Game with player stats and a leaderboard(?)

- Player 1 and Player 2
- Player 1 is controlled by the arrow keys
- Player 2 is controlled by the WASD keys (or network)
- Anon account for online
- Server uses sqllite to store player stats
- Server version of the game to just sync the game state



"""

import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player = pygame.Rect((300, 250, 50, 50))

run = True
while run:
    # Clear the screen
    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, (255, 0, 0), player)
    
    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True:
        player.move_ip(-1, 0)
    elif key[pygame.K_d] == True:
        player.move_ip(1, 0)
    elif key[pygame.K_w] == True:
        player.move_ip(0, -1)
    elif key[pygame.K_s] == True:
        player.move_ip(0, 1)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update() 

pygame.quit()
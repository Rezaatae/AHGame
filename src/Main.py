import pygame

# Initialize the pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

# title and icon
pygame.display.set_caption("AHGame")
icon = pygame.image.load("shuttle.png")
pygame.display.set_icon(icon)

# player

playerImg = pygame.image.load("mission (1).png")
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0

def player(x, y):
    screen.blit(playerImg, (x, y))

# Game loop
running = True
while running:

    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # check if key stroke presses is left or right
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.1
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.1
            if event.key == pygame.K_UP:
                playerY_change = -0.1
            if event.key == pygame.K_DOWN:
                playerY_change = 0.1

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerX_change = 0
                playerY_change = 0

    playerY += playerY_change
    playerX += playerX_change
    player(playerX, playerY)
    pygame.display.update()
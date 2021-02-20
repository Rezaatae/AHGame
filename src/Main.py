import pygame

# Initialize the pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

# title and icon
pygame.display.set_caption("AHGame")
icon = pygame.image.load("shuttle.png")
pygame.display.set_icon(icon)


# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    pygame.display.update()
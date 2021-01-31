import pygame
pygame.init()

screen = pygame.display.set_mode((600, 600))
image = pygame.image.load("down1.png").convert_alpha()
image.set_colorkey((255,255,255))
while True:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    screen.blit(image, (0, 0))
    pygame.display.update()

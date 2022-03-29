import pygame

screen = pygame.display.set_mode((800,600))

bg = pygame.image.load("game_over.png")


run = True 
while run:
    screen.blit(bg,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
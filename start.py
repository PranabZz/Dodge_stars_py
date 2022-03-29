import pygame

screen = pygame.display.set_mode((800,600))

bg1 = pygame.image.load("start.png")

run = True 
while run:
    screen.blit(bg1,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            import main
            run = False
    pygame.display.update()
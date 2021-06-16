import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))

screen.fill((0,0,0))

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == MOUSEBUTTONDOWN:
            # draw background first (however)
            screen.fill((0,0,0))

            # draw your other layers (mouse image)

            # draw the circle
            color = (255,255,255)
            posx,posy = pygame.mouse.get_pos()
            pygame.draw.circle(screen, color, (posx,posy), 50)

    pygame.display.update()
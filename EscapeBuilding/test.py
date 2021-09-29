import pygame,time
pygame.init()
ld = pygame.image.load("locked-door.png")
clock = pygame.time.Clock()
win = pygame.display.set_mode((1920,1080))

pygame.display.set_caption("Game")
while True:
    clock.tick(27)
    win.blit(ld, (600, 600))
    pygame.display.update()
#!/usr/bin/python3

import pygame
pygame.init()

win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("First Game")

x = 50 # X position of rectangle init pos
y = 450 # Y position of rectangle init pos
width = 40 # Width of rectangle
height = 60 # Height of rectangle
vel = 5 # Velocity of rectangle
run = True # Should pygame work or not

isJump = False # Are we jumping or not?
jumpCount = 10 # Y position change of rectangle when jumping

while run: # While program is running
    pygame.time.delay(100) # delay the time to slow down program
    for event in pygame.event.get(): # Get events
        if event.type == pygame.QUIT: # Has the window been closed?
            run = False # Close the game
    keys = pygame.key.get_pressed() # Grab the keys that are pressed
    #if not(isJump): # If not jumping
    if keys[pygame.K_LEFT] and x > vel: # If left key pressed
        x -= vel # reduce x position by vel
    if keys[pygame.K_RIGHT] and x < 500 - width - vel: # If right key pressed
        x += vel # increase x position by vel
    if keys[pygame.K_UP] and y > vel: # If up key pressed
        y -= vel # reduce y position by vel
    if keys[pygame.K_DOWN] and y < 500 - height - vel: # If down key pressed
        y += vel # increase y position by vel
    if keys[pygame.K_SPACE]: # If space key pressed
        isJump = True # Jump
    if isJump: # If jumping
        if jumpCount >= -10: # When jumping
            neg = 1 # Direct value to go up
            if jumpCount < 0: # If intended to go down
                neg = -1 # Direct value to go down
            y -= (jumpCount ** 2)*0.5*neg # Move the character up by jumpCount. The squared is to make the square decelerate as you go up, and accelerate as you go down. Multiply to reduce the total jump height to make it more natural.
            jumpCount -= 1 # Decrease jumpCount
        else: # When jump is complete
            isJump = False # Jump is not happening
            jumpCount = 10 # Resetting jump velocity
    win.fill((0, 0, 0))
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    pygame.display.update()
pygame.QUIT()
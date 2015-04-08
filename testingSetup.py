import sys
import pygame
from pygame.locals import *

 
FNAME = "target.png"
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

PLAYER_SPEED_PY = -3
PLAYER_SPEED_NY = 3
PLAYER_SPEED_PX = 3
PLAYER_SPEED_NX = -3

#Initalize the Program

pygame.init()

#Create the Screen

WIDTH =  800       
HEIGHT = 600
screen= pygame.display.set_mode((WIDTH,HEIGHT), 0, 32)

pygame.display.flip() 



player = pygame.image.load (FNAME).convert()
screen.blit (player, (100, 100))
pygame.display.update()



y = 300
x = 100
y_dir = 0
x_dir = 0
 

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_UP:
                y_dir = PLAYER_SPEED_PY
            if event.key == K_DOWN:
                y_dir = PLAYER_SPEED_NY
            if event.key == K_RIGHT:
                x_dir = PLAYER_SPEED_PX
            if event.key == K_LEFT:
                x_dir = PLAYER_SPEED_NX

        if event.type == KEYUP:
            if event.key == K_UP or event.key == K_DOWN:
                y_dir = 0
            if event.key == K_LEFT or event.key == K_RIGHT:
                x_dir = 0
 

        #time_passed = clock.tick()
        #time_passed_seconds = time_passed / 1000.0
        #distance = time_passed_seconds * speed



      #reset x and y pixel the sprite should be located at before blitting them
        #old_y = y
    y += y_dir #* distance

 
        #old_x = x

    x += x_dir #* distance

 

        #redraw screen in black and refresh location of sprite

    screen.fill ((BLUE))

    screen.blit (player, (x, y))

    pygame.display.update()

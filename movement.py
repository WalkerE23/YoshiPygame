'''
YOSHI ATTACK! (name pending....)

By: Elliott Walker!
New York Univerity Polytechninc Institute

honorary credit to Robert "Ludqvist+Gaborik+Callahan" Schwartzberg
and Andrew "thagrizzlybear" Madison

'''

####www.discoveryplayground.com/computer-programming-for-kids/rgb-colors/
##http://pixlr.com/editor/

import sys
import pygame
import math
from pygame.locals import *

BNAME = "clouds.png"
FNAME = "NormalYoshi1.png"
FNAME2 = "ToungeYoshi1.png"
FNAME3 = "YoshiJump1.png"
FNAME4 = "YoshiBlock6.png"
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YWHITE = (253,253,253)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BEIGE= (205, 175, 149)


FPS = 100
TIME_TOUNGE_HELD = 30
TIME_BLOCK_HELD = 60



y = 300
x = 100
y_dir = 0
x_dir = 0

PLAYER_SPEED_PY = -6
PLAYER_SPEED_NY = 6
PLAYER_SPEED_PX = 3
PLAYER_SPEED_NX = -3

GRAVITY = -.2

#Initalize the Program

pygame.init()
pygame.mouse.set_visible(1)
clock = pygame.time.Clock()


#Create the Screen

WIDTH =  1200       
HEIGHT = 800
screen= pygame.display.set_mode((WIDTH,HEIGHT), 0, 32)




pygame.display.flip() 

#####################################################
###     Initiate Graphics              ##############

background = pygame.image.load(BNAME).convert()

player = pygame.image.load(FNAME)
player.set_colorkey(BLUE)
player = player.convert_alpha()
playerBackwards = pygame.transform.flip(player, True, False)

playerAlt = pygame.image.load(FNAME2)
playerAlt.set_colorkey(BLUE)
playerAlt = playerAlt.convert_alpha()
playerAltBackwards = pygame.transform.flip(playerAlt, True, False)

playerJump = pygame.image.load(FNAME3)
playerJump.set_colorkey(BLUE)
playerJump = playerJump.convert_alpha()
playerJumpBackwards = pygame.transform.flip(playerJump, True, False)

playerBlock = pygame.image.load(FNAME4)
playerBlock.set_colorkey(BLUE)
playerBlock = playerBlock.convert_alpha()
playerBlockBackwards = pygame.transform.flip(playerBlock, True, False)

##############################



playerHeight = player.get_height()
playerAltHeight = playerAlt.get_height()
playerBlockHeight = playerBlock.get_height()

playerWidth = player.get_width()
playerAltWidth = player.get_width()
playerBlockWidth = player.get_width()


screen.blit (player, (x, y))
pygame.display.update()

############################
### GAMEPLAY SWITCHES ######

loopCounter = 0

heldEKey = False

facingRight = True

toungeTimer = None
toungeOut = False

grounded = False
jumpsLeft = 2 #number of jumps allowed.. ie, "double-jump"

blocking = False
blockTimer = None

##########################

while True:

    screen.blit (background, (0,-300))
    #screen.fill((GREEN))
    pygame.draw.rect(screen, WHITE, (0,750, 1200, 50))
    pygame.draw.rect(screen, WHITE, (-1,0,0,800))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

        if event.type == KEYDOWN:
            
            if event.key == K_SPACE:
                if (jumpsLeft > 0):
                    y_dir = PLAYER_SPEED_PY
                    jumpsLeft -= 1
                
                
            if event.key == K_DOWN:
                blocking = True
                blockTimer = loopCounter
                
               
            if (event.key == K_RIGHT) and (toungeTimer == None):
                x_dir = PLAYER_SPEED_PX
                facingRight = True
                
                
            if (event.key == K_LEFT) and (toungeTimer == None):
                x_dir = PLAYER_SPEED_NX
                facingRight = False
                

            if (event.key == K_e) and not (toungeOut):
                heldEKey = True
                toungeOut = True
                toungeTimer = loopCounter
                if (not facingRight):
                    x -= 60

                
                
                
        if event.type == KEYUP:               
                
            if event.key == K_LEFT or event.key == K_RIGHT:
                x_dir = 0
            if event.key == K_DOWN:
                blocking = False

            ##Avoid Button-Mashing##    
            #if event.key == K_e:
                #heldEKey = False
                #toungeTimer = None

    loopCounter += 1
    
    if toungeTimer != None:
        if loopCounter >(toungeTimer + TIME_TOUNGE_HELD):
            heldEKey = False
            toungeTimer = None
            toungeOut = False
            if (not facingRight):
                if toungeTimer != None:
                    x -= 60
                else:
                    x += 60

    if blockTimer != None:
        if loopCounter > (blockTimer + TIME_BLOCK_HELD):
            blocking = False
            blockingTimer = None

                
    y += y_dir
    x += x_dir
#####################################
### MANAGE/BLIT/DISPLAY GRAPHICS####
    if facingRight:
        if not grounded:
            if heldEKey:
                screen.blit (playerAlt, (x,y))
            else:
                screen.blit (playerJump, (x,y))
        else:
            if heldEKey:
                screen.blit (playerAlt, (x,y))
            elif blocking:
                screen.blit(playerBlock, (x,y))
            else:
                screen.blit (player, (x,y))

    else:
        if not grounded:
            if heldEKey:
                screen.blit(playerAltBackwards, (x,y))
            else:
                screen.blit(playerJumpBackwards, (x,y))

        else:
            if heldEKey:
                screen.blit (playerAltBackwards, (x,y))
            elif blocking:
                screen.blit (playerBlockBackwards, (x,y))
            else:
                screen.blit (playerBackwards, (x,y))
##################################
##LOWEST BORDERS + GRAVITY
    if heldEKey:
        #is alternate form
        if ((y + playerAltHeight) > 750):
            y = 750 - playerAltHeight
            grounded = True
            
        else:
            y_dir -= GRAVITY
            grounded = False

    else:
        if ((y + playerHeight) > 750):
            y = 750 - playerHeight
            grounded = True

        else:
            y_dir -= GRAVITY
            grounded = False

    if (grounded):

        jumpsLeft = 2

###############################
### SIDE BORDERS ##############
    if heldEKey:
        if ((x) < 0):
            x = -50
        if ((x) > 1178):
            x = 1178
    else:
        if ((x) < 0):
            x = 0
        if ((x) > 1178):
            x = 1178
################################  
            


 

    clock.tick(FPS)

    pygame.display.update()

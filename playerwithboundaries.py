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
import random
from pygame.locals import *


BNAME = "clouds.png"
FNAME = "NormalYoshi1.png"
FNAME2 = "ToungeYoshi1.png"
FNAME3 = "YoshiJump1.png"
FNAME4 = "YoshiBlock6.png"

YRNAME1 = "YoshiRun1.png"
YRNAME2 = "YoshiRun2.png"
YRNAME3 = "YoshiRun3.png"
YRNAME4 = "YoshiRun4.png"
YRNAME5 = "YoshiRun5.png"
YRNAME6 = "YoshiRun6.png"

ONAME1 = "baddie1.png"

RNAME =  "RockObject1.png"
RNAME2 = "RockObject2.png"
RNAME3 = "RockObject3.png"
RNAME4 = "RockObject4.png"
RNAME5 = "RockObject5.png"
RNAME6 = "RockObject6.png"

RNAME7 = "RockObject7.png"

PNAME = "platform1.png"
PNAME2 = "platform2.png"
PNAME3 = "platform3.png"
PNAME4 = "platform3.png"


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YWHITE = (253,253,253)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BEIGE= (205, 175, 149)


FPS = 60
TIME_TOUNGE_HELD = 30
TIME_BLOCK_HELD = 60



y = 750
x = 500
y_dir = 0
x_dir = 0

xR = random.randint(100, 1000)
yR = 0

PLAYER_SPEED_PY = -6
PLAYER_SPEED_NY = 6
PLAYER_SPEED_PX = 3
PLAYER_SPEED_NX = -3

rockSpeed = 6

GRAVITY = -.2

#Initalize the Program

pygame.init()
pygame.mouse.set_visible(1)
clock = pygame.time.Clock()


#Create the Screen

WIDTH =  1400       
HEIGHT = 800
screen= pygame.display.set_mode((WIDTH,HEIGHT), 0, 32)

pygame.display.flip() 

#####################################################
###     Initiate Graphics              ##############

background = pygame.image.load(BNAME).convert()

player = pygame.image.load(FNAME)
player.set_colorkey(BLUE)
player = player.convert_alpha()
playerHeight = player.get_height()
playerWidth = player.get_width()

playerBackwards = pygame.transform.flip(player, True, False)

playerAlt = pygame.image.load(FNAME2)
playerAlt.set_colorkey(BLUE)
playerAlt = playerAlt.convert_alpha()
playerAltHeight = playerAlt.get_height()
playerAltWidth = player.get_width()
playerAltBackwards = pygame.transform.flip(playerAlt, True, False)
playerABH = playerAltBackwards.get_height()
playerABW = playerAltBackwards.get_width()

playerJump = pygame.image.load(FNAME3)
playerJump.set_colorkey(BLUE)
playerJump = playerJump.convert_alpha()
playerJumpBackwards = pygame.transform.flip(playerJump, True, False)

playerBlock = pygame.image.load(FNAME4)
playerBlock.set_colorkey(BLUE)
playerBlock = playerBlock.convert_alpha()
playerBlockHeight = playerBlock.get_height()
playerBlockWidth = player.get_width()
playerBlockBackwards = pygame.transform.flip(playerBlock, True, False)

playerRun1 = pygame.image.load(YRNAME1)
playerRun1.set_colorkey(BLUE)
playerRun1 = playerRun1.convert_alpha()
playerRun1Back = pygame.transform.flip(playerRun1, True, False)

playerRun2 = pygame.image.load(YRNAME2)
playerRun2.set_colorkey(BLUE)
playerRun2 = playerRun2.convert_alpha()
playerRun2Back = pygame.transform.flip(playerRun2, True, False)

playerRun3 = pygame.image.load(YRNAME3)
playerRun3.set_colorkey(BLUE)
playerRun3 = playerRun3.convert_alpha()
playerRun3Back = pygame.transform.flip(playerRun3, True, False)

playerRun4 = pygame.image.load(YRNAME4)
playerRun4.set_colorkey(BLUE)
playerRun4 = playerRun4.convert_alpha()
playerRun4Back = pygame.transform.flip(playerRun4, True, False)

playerRun5 = pygame.image.load(YRNAME5)
playerRun5.set_colorkey(BLUE)
playerRun5 = playerRun5.convert_alpha()
playerRun5Back = pygame.transform.flip(playerRun5, True, False)

playerRun6 = pygame.image.load(YRNAME6)
playerRun6.set_colorkey(BLUE)
playerRun6 = playerRun6.convert_alpha()
playerRun6Back = pygame.transform.flip(playerRun6, True, False)

playerRunList = [playerRun1,playerRun2,playerRun3,playerRun4,playerRun5,playerRun6]


######################################
#####     BADGUYS ####################


baddie1 = pygame.image.load(ONAME1)
baddie1.set_colorkey(BLUE)
baddie1 = baddie1.convert_alpha()
baddie1Backwards = pygame.transform.flip(baddie1, True, False)

enemyList = []


class Baddie(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = baddie1
        self.imageBackwards = pygame.transform.flip(baddie1, True, False)
        self.height = self.image.get_height()
        self.width = self.image.get_width()
        self.xb = random.randint(50,1350)
        self.yb = 702
        self.yb_dir = 0
        self.xb_dir = 0
        self.posSpeed = 3.5
        self.negSpeed = -3.5

        enemyList.append(self)
        
        #self.rect = pygame.Rect((self.xb,self.yb),(self.width,self.height))
        
        self.baddieWalking = True        
        self.baddieReachedRightSide = False
        self.baddieReachedLeftSide = True

    def testForEnd(self):        
        if (self.xb > 1350):
            self.baddieReachedRightSide = True
            self.baddieReachedLeftSide = False
        if (self.xb < 0):
            self.baddieReachedLeftSide = True
            self.baddieReachedRightSide = False

    def baddieRect(self):

        self.rect = pygame.Rect((self.xb,self.yb),(self.width,self.height))

    def killed(self):

        enemyList.remove(self)
        
        
    def move(self):
        if self.baddieWalking:
            if self.baddieReachedLeftSide:
                self.xb_dir = self.posSpeed
                screen.blit(self.image, (self.xb,self.yb))
            else:
                self.xb_dir = self.negSpeed
                screen.blit(self.imageBackwards, (self.xb,self.yb))

    def update(self):
        self.move()
                



#####FALLING ROCKS #######
rock1 = pygame.image.load(RNAME)
rock1.set_colorkey(BLUE)
rock1 = rock1.convert_alpha()

rock2 = pygame.image.load(RNAME2)
rock2.set_colorkey(BLUE)
rock2 = rock2.convert_alpha()

rock3 = pygame.image.load(RNAME3)
rock3.set_colorkey(BLUE)
rock3 = rock3.convert_alpha()

rock4 = pygame.image.load(RNAME4)
rock4.set_colorkey(BLUE)
rock4 = rock4.convert_alpha()

rock5 = pygame.image.load(RNAME5)
rock5.set_colorkey(BLUE)
rock5 = rock5.convert_alpha()

rock6 = pygame.image.load(RNAME6)
rock6.set_colorkey(BLUE)
rock6 = rock6.convert_alpha()

rock7 = pygame.image.load(RNAME7)
rock7.set_colorkey(BLUE)
rock7 = rock7.convert_alpha()

rocks = [rock1,rock2,rock3,rock4,rock5,rock6,rock7]

##### PLATFORMS #######
platform1 = pygame.image.load(PNAME)
#platform1Rect = pygame.Rect((??????????),(platform1.get_width(), platform1.get_height()))
platform2 = pygame.image.load(PNAME2)
P2X = 200
P2Y = 500
platform2Rect = pygame.Rect((P2X+3,P2Y),(platform2.get_width()-6, 10))

platform3 = pygame.image.load(PNAME3)
P3X = 0
P3Y = 650
platform3Rect = pygame.Rect((P3X+3,P3Y),(platform3.get_width()-6, 10))

platform4 = pygame.image.load(PNAME4)
P4X = 420
P4Y = 650
platform4Rect = pygame.Rect((P4X+3,P4Y),(platform4.get_width() - 6, 10))


####################################
def evenOrOdd( number ):
    if number%2 == 0:
        return True

def fire():

    fireTimer = (loopCounter%500)

    if fireTimer == 0:
        print "FFFFFIIIIIIIRRRRRREEEEEEEE"

def singleBaddie(name):

    name.baddieRect()
    name.testForEnd()
    name.update()
    name.yb += name.yb_dir
    name.xb += name.xb_dir

    




###################################


screen.blit (player, (x, y))
b1 = Baddie()
screen.blit(b1.image, (b1.xb,b1.yb))
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

chosenRock = rocks[random.randint(0,6)]
rockInAir = True

running = False

runCounter = None

alive = True


##########################

while alive:

    screen.blit (background,(0,-300))
    #screen.fill((GREEN))
    pygame.draw.rect(screen, WHITE, (0,750, 1400, 50))
    screen.blit(platform2, (P2X,P2Y))
    screen.blit(platform3, (P3X,P3Y))
    screen.blit(platform4, (P4X,P4Y))
        
        
        
    
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
                running = True
                
                
            if (event.key == K_LEFT) and (toungeTimer == None):
                x_dir = PLAYER_SPEED_NX
                facingRight = False
                running = True
                

            if (event.key == K_e) and not (toungeOut):
                heldEKey = True
                toungeOut = True
                toungeTimer = loopCounter
                if (not facingRight):
                    x -= 60

                
                
                
        if event.type == KEYUP:
                
            if event.key == K_LEFT or event.key == K_RIGHT:
                x_dir = 0
                running = False
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
    yR += rockSpeed



##########################################
########### RECTS!! ####################

    if facingRight:
            playerRect = pygame.Rect((x ,y),(playerWidth, playerHeight))
            playerPlatformRect = pygame.Rect((x,(y+playerHeight-2)), (playerWidth,2))

    else:
        if heldEKey:
            playerPlatformRect = pygame.Rect((x + 60,(y+playerHeight-2)), (playerWidth,2))
        else:
            playerPlatformRect = pygame.Rect((x,(y+playerHeight-2)), (playerWidth,2))
            playerRect = pygame.Rect((x,y),(playerWidth,playerHeight))

    playerAltRect = pygame.Rect((x,y),(playerAltWidth,playerAltHeight))


###########################################
##### Platforms #####

    if (y_dir < 0):
        pass
    
    if (y_dir > 0) and (y > (P2Y-50)):
        if playerPlatformRect.colliderect(platform2Rect):
            y_dir  = 0
            y = P2Y-playerHeight+2
            grounded = True
            jumpsLeft = 2
            
    if (y_dir > 0) and (y > (P3Y-50)):
        if playerPlatformRect.colliderect(platform3Rect):
            y_dir = 0
            y = P3Y-playerHeight+2
            grounded = True
            jumpsLeft = 2
            
    if (y_dir > 0) and (y > (P4Y-50)):
        if playerPlatformRect.colliderect(platform4Rect):
            y_dir = 0
            y = P4Y-playerHeight+2
            grounded = True
            jumpsLeft = 2  
    
    
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
            #elif PkillB:
                
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

##############
## BAD GUY ###
    
    singleBaddie(b1)
    if heldEKey:
        if playerAltRect.colliderect(b1.rect):
            PkillB = True
            
        

    
    
        

                
##################################
##LOWEST BORDERS + GRAVITY
    if heldEKey:
        #is alternate form
        if ((y + playerAltHeight) > 750):
            y = 750 - playerAltHeight
            grounded = True
            y_dir = 0
            
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
        if ((x) > 1378):
            x = 1378
    else:
        if ((x) < 0):
            x = 0
        if ((x) > 1378):
            x = 1378
################################

    

        

    fire()

    clock.tick(FPS)
    

    pygame.display.update()

'''
YOSHI ATTACK! (or some other name...)

By: Elliott Walker!
New York Univerity Polytechninc Institute

support from Robert "Ludqvist+Gaborik+Callahan" Schwartzberg
and Andrew "thagrizzlybear" Madison

'''

####www.discoveryplayground.com/computer-programming-for-kids/rgb-colors/
##http://pixlr.com/editor/

import sys
import pygame
import math
import random
import glob
from pygame.locals import *


BNAME = "clouds.png"
BNAME2 = "grass1.png"
BNAME3 = "column1.png"
BNAME4 = "smallLightBrick1.png"
BNAME5 = "smallMediumBrick1.png"
BNAME6 = "smallDarkBrick1.png"
BNAME7 = "goldTile.png"
BNAME8 = "greenTile.png"

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
ONAME2 = "baddie2.png"
ONAME3 = "baddie3.png"
ONAME4 = "baddie4.png"
ONAME5 = "baddie5.png"
ONAME6 = "baddie6.png"
ONAME7 = "baddie7.png"
ONAME8 = "baddie8.png"
ONAME9 = "baddie9.png"
ONAME10 = "baddie10.png"
ONAME11 = "baddie11.png"
ONAME12 = "baddie12.png"
ONAME13 = "baddie13.png"
ONAME14 = "baddie14.png"
ONAME15 = "baddie15.png"
ONAME16 = "baddie16.png"


RNAME =  "RockObject1.png"
RNAME2 = "RockObject2.png"
RNAME3 = "RockObject3.png"
RNAME4 = "RockObject4.png"
RNAME5 = "RockObject5.png"
RNAME6 = "RockObject6.png"

RNAME7 = "RockObject7.png"

PNAME = "platform1.png"
PNAME2 = "platform2.png"
PNAME3 = "tiledPlatform.png"
PNAME4 = "tiledPlatform.png"
PNAME5 = "platform2Alt.png"
PNAME6 = "redBlock.png"


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YWHITE = (253,253,253)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BEIGE= (205, 175, 149)


FPS = 80
loopCounter = 0
TIME_TOUNGE_HELD = 10
TIME_BLOCK_HELD = 80
BADDIE_RESPAWN = loopCounter%250

NUMBER_OF_BADGUYS = 6

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
print(pygame.version.ver)


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

baddie2 = pygame.image.load(ONAME2)
baddie2.set_colorkey(BLUE)
baddie2 = baddie2.convert_alpha()
baddie2Backwards = pygame.transform.flip(baddie2, True, False)

baddie3 = pygame.image.load(ONAME3)
baddie3.set_colorkey(BLUE)
baddie3 = baddie3.convert_alpha()
baddie3Backwards = pygame.transform.flip(baddie3, True, False)

baddie4 = pygame.image.load(ONAME4)
baddie4.set_colorkey(BLUE)
baddie4 = baddie4.convert_alpha()
baddie4Backwards = pygame.transform.flip(baddie4, True, False)

baddie5 = pygame.image.load(ONAME5)
baddie5.set_colorkey(BLUE)
baddie5 = baddie5.convert_alpha()
baddie5Backwards = pygame.transform.flip(baddie5, True, False)

baddie6 = pygame.image.load(ONAME6)
baddie6.set_colorkey(BLUE)
baddie6 = baddie6.convert_alpha()
baddie6Backwards = pygame.transform.flip(baddie6, True, False)

baddie7 = pygame.image.load(ONAME7)
baddie7.set_colorkey(BLUE)
baddie7 = baddie7.convert_alpha()
baddie7Backwards = pygame.transform.flip(baddie7, True, False)

baddie8 = pygame.image.load(ONAME8)
baddie8.set_colorkey(BLUE)
baddie8 = baddie8.convert_alpha()
baddie8Backwards = pygame.transform.flip(baddie8, True, False)

baddie9 = pygame.image.load(ONAME9)
baddie9.set_colorkey(BLUE)
baddie9 = baddie9.convert_alpha()
baddie9Backwards = pygame.transform.flip(baddie9, True, False)

baddie10 = pygame.image.load(ONAME10)
baddie10.set_colorkey(BLUE)
baddie10 = baddie10.convert_alpha()
baddie10Backwards = pygame.transform.flip(baddie10, True, False)

baddie11 = pygame.image.load(ONAME11)
baddie11.set_colorkey(BLUE)
baddie11 = baddie11.convert_alpha()
baddie11Backwards = pygame.transform.flip(baddie11, True, False)

baddie12 = pygame.image.load(ONAME12)
baddie12.set_colorkey(BLUE)
baddie12 = baddie12.convert_alpha()
baddie12Backwards = pygame.transform.flip(baddie12, True, False)

baddie13 = pygame.image.load(ONAME13)
baddie13.set_colorkey(BLUE)
baddie13 = baddie13.convert_alpha()
baddie13Backwards = pygame.transform.flip(baddie13, True, False)

baddie14 = pygame.image.load(ONAME14)
baddie14.set_colorkey(BLUE)
baddie14 = baddie14.convert_alpha()
baddie14Backwards = pygame.transform.flip(baddie14, True, False)

baddie15 = pygame.image.load(ONAME15)
baddie15.set_colorkey(BLUE)
baddie15 = baddie15.convert_alpha()
baddie15Backwards = pygame.transform.flip(baddie15, True, False)

baddie16 = pygame.image.load(ONAME16)
baddie16.set_colorkey(BLUE)
baddie16 = baddie16.convert_alpha()
baddie16Backwards = pygame.transform.flip(baddie16, True, False)

enemyList = []



class Baddie(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = baddie7
        self.imageBackwards = pygame.transform.flip(baddie7, True, False)
        self.height = baddie1.get_height()
        self.width = baddie1.get_width()
        bspawn = random.randint(0,1)
        if bspawn == 1:
            self.xb = random.randint(-200,0)
        else:
            self.xb = random.randint(1400,1800)
        #self.xb = random.randint(0,1550)
        self.yb = 702
        self.yb_dir = 0
        self.xb_dir = 0
        self.posSpeed = 3.5
        self.negSpeed = -3.5

        enemyList.append(self)
        
        self.baddieWalking = True        
        self.baddieReachedRightSide = False
        self.baddieReachedLeftSide = True


        #screen.blit(self.img, (self.xb,self.yb))
        

        #self.image = [baddie1,baddie2,baddie3,baddie4,baddie5,baddie6,baddie7,baddie8,baddie9,baddie10,baddie11,baddie12,baddie13,baddie14,baddie15,baddie16]


    def testForEnd(self):        
        if (self.xb > 1350):
            self.baddieReachedRightSide = True
            self.baddieReachedLeftSide = False
        if (self.xb < 0):
            self.baddieReachedLeftSide = True
            self.baddieReachedRightSide = False

    def baddieRect(self):

        self.rect = pygame.Rect((self.xb,self.yb),(self.width,self.height))
        self.baddieKillRect = pygame.Rect((self.xb,self.yb),((self.width/8),self.height))
        self.baddieKillAltRect = pygame.Rect((self.xb+55,self.yb),((self.width/8),self.height))

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
grassBase1 = pygame.image.load(BNAME2)
grassBase1 = grassBase1.convert_alpha()
GBX1 = 0
GBY1 = 750
grassBase2 = pygame.image.load(BNAME2)
grassBase2 = grassBase2.convert_alpha()
GBX2 = 95
GBY2 = 750
grassBase3 = pygame.image.load(BNAME2)
grassBase3 = grassBase3.convert_alpha()
GBX3 = 190
GBY3 = 750
grassBase4 = pygame.image.load(BNAME2)
grassBase4 = grassBase4.convert_alpha()
GBX4 = 285
GBY4 = 750
grassBase5 = pygame.image.load(BNAME2)
grassBase5 = grassBase5.convert_alpha()
GBX5 = 380
GBY5 = 750
grassBase6 = pygame.image.load(BNAME2)
grassBase6 = grassBase6.convert_alpha()
GBX6 = 475
GBY6 = 750
grassBase7 = pygame.image.load(BNAME2)
grassBase7 = grassBase7.convert_alpha()
GBX7 = 570
GBY7 = 750
grassBase8 = pygame.image.load(BNAME2)
grassBase8 = grassBase8.convert_alpha()
GBX8 = 665
GBY8 = 750
grassBase9 = pygame.image.load(BNAME2)
grassBase9 = grassBase9.convert_alpha()
GBX9 = 760
GBY9 = 750
grassBase10 = pygame.image.load(BNAME2)
grassBase10 = grassBase10.convert_alpha()
GBX10 = 855
GBY10 = 750
grassBase11 = pygame.image.load(BNAME2)
grassBase11 = grassBase11.convert_alpha()
GBX11 = 950
GBY11 = 750
grassBase12 = pygame.image.load(BNAME2)
grassBase12 = grassBase12.convert_alpha()
GBX12 = 1045
GBY12 = 750
grassBase13 = pygame.image.load(BNAME2)
grassBase13 = grassBase13.convert_alpha()
GBX13 = 1140
GBY13 = 750
grassBase14 = pygame.image.load(BNAME2)
grassBase14 = grassBase14.convert_alpha()
GBX14 = 1235
GBY14 = 750
grassBase15 = pygame.image.load(BNAME2)
grassBase15 = grassBase15.convert_alpha()
GBX15 = 1330
GBY15 = 750


lightBrick1 = pygame.image.load(BNAME4)
lightBrick1.set_colorkey(BLUE)
lightBrick1 = lightBrick1.convert_alpha()
medBrick1 = pygame.image.load(BNAME5)
medBrick1.set_colorkey(BLUE)
medBrick1 = medBrick1.convert_alpha()
darkBrick1 = pygame.image.load(BNAME6)
darkBrick1.set_colorkey(BLUE)
darkBrick1 = darkBrick1.convert_alpha()
goldTile = pygame.image.load(BNAME7)
goldTile.set_colorkey(BLUE)
goldTile = goldTile.convert_alpha()
redBlock = pygame.image.load(PNAME6)
redBlock.set_colorkey(BLUE)
redBlock = redBlock.convert_alpha()
greenTile = pygame.image.load(BNAME8)
greenTile = greenTile.convert_alpha()




platform1 = pygame.image.load(PNAME)
#platform1Rect = pygame.Rect((??????????),(platform1.get_width(), platform1.get_height()))
platform2 = pygame.image.load(PNAME2)
P2X = 0
P2Y = 490
platform2Rect = pygame.Rect((P2X+3,P2Y),(platform2.get_width()-6, 10))

platform3 = pygame.image.load(PNAME3)
P3X = 0
P3Y = 650
platform3Rect = pygame.Rect((P3X+3,P3Y),(platform3.get_width()-6, 10))

platform4 = pygame.image.load(PNAME4)
P4X = 420
P4Y = 650
platform4Rect = pygame.Rect((P4X+3,P4Y),(platform4.get_width() - 6, 10))

platform5 = lightBrick1
P5X = 850
P5Y = 685
platform5Rect = pygame.Rect((P5X+3,P5Y),(((platform5.get_width() - 6)*3), 10))

platform6 = lightBrick1
P6X = 914
P6Y = 620
platform6Rect = pygame.Rect((P6X+3,P6Y),(((platform6.get_width() - 6)*2), 10))

platform7 = lightBrick1
P7X = 978
P7Y = 555
platform7Rect = pygame.Rect((P7X+3,P7Y),(platform7.get_width() - 6, 10))

platform8 = pygame.image.load(PNAME2)
P8X = 100
P8Y = 400
platform8Rect = pygame.Rect((P8X+3,P8Y),(platform8.get_width() - 6, 10))

platform9 = pygame.image.load(PNAME2)
P9X = 0
P9Y = 305
platform9Rect = pygame.Rect((P9X+3,P9Y),(platform9.get_width() - 6, 10))

platform10 = pygame.image.load(PNAME5)
P10X = 100
P10Y = 210
platform10Rect = pygame.Rect((P10X+3,P10Y),(platform10.get_width() - 6, 10))

platform11 = pygame.image.load(PNAME2)
P11X = 0
P11Y = 130
platform11Rect = pygame.Rect((P11X+3,P11Y),(platform11.get_width() - 6, 10))

platform12 = goldTile
P12X = 192
P12Y = 50
platform12Rect = pygame.Rect((P12X+3,P12Y),(((platform12.get_width())*4),10))

platform13 = redBlock
P13X = 500
P13Y = 80
platform13Rect = pygame.Rect((P13X+3,P13Y),(platform13.get_width(), 10))

platform14 = redBlock
P14X = 700
P14Y = 100
platform14Rect = pygame.Rect((P14X+3,P14Y),(platform14.get_width(), 10))

platform15 = redBlock
P15X = 900
P15Y = 80
platform15Rect = pygame.Rect((P15X+3,P15Y),(platform15.get_width(), 10))


####################################
def displayGrass():

    screen.blit(grassBase1, (GBX1,GBY1))
    screen.blit(grassBase2, (GBX2,GBY2))
    screen.blit(grassBase3, (GBX3,GBY3))
    screen.blit(grassBase4, (GBX4,GBY4))
    screen.blit(grassBase5, (GBX5,GBY5))
    screen.blit(grassBase6, (GBX6,GBY6))
    screen.blit(grassBase7, (GBX7,GBY7))
    screen.blit(grassBase8, (GBX8,GBY8))
    screen.blit(grassBase9, (GBX9,GBY9))
    screen.blit(grassBase10, (GBX10,GBY10))
    screen.blit(grassBase11, (GBX11,GBY11))
    screen.blit(grassBase12, (GBX12,GBY12))
    screen.blit(grassBase13, (GBX13,GBY13))
    screen.blit(grassBase14, (GBX14,GBY14))
    screen.blit(grassBase15, (GBX15,GBY15))

def displayStairs():
    screen.blit(lightBrick1, (850,685))
    screen.blit(lightBrick1, (914,620))
    screen.blit(lightBrick1, (978,555))
    screen.blit(medBrick1, (914,685))
    screen.blit(medBrick1, (978,620))
    screen.blit(darkBrick1, (978,685))
    screen.blit(goldTile, (192,50))
    screen.blit(goldTile, (224,50))
    screen.blit(goldTile, (256,50))
    screen.blit(goldTile, (288,50))
    screen.blit(redBlock, (500,80))
    screen.blit(redBlock, (700, 100))
    screen.blit(redBlock, (900, 80))
    screen.blit(greenTile, (1250, 50))
    screen.blit(greenTile, (1280, 50))
    screen.blit(greenTile, (1310, 50))
    screen.blit(greenTile, (1340, 50))
    screen.blit(greenTile, (1370, 50))
        
    
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

def addBaddie():
    badGuy = Baddie()
    

    




###################################


screen.blit (player, (x, y))
#b1 = Baddie()
#screen.blit(b1.image, (b1.xb,b1.yb))
pygame.display.update()


############################
### GAMEPLAY SWITCHES ######



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

PkillB = False



##########################

while alive:

    screen.blit (background,(0,-300))
    #screen.fill((GREEN))
    pygame.draw.rect(screen, WHITE, (0,750, 1400, 50))
    displayStairs()
    displayGrass()
    screen.blit(platform2, (P2X,P2Y))
    screen.blit(platform3, (P3X,P3Y))
    screen.blit(platform4, (P4X,P4Y))
    screen.blit(platform8, (P8X,P8Y))
    screen.blit(platform9, (P9X,P9Y))
    screen.blit(platform10, (P10X,P10Y))
    screen.blit(platform11, (P11X,P11Y))

    
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

    playerAltRect = pygame.Rect((x+90,y),(playerAltWidth/4,playerAltHeight))
    playerAltBackwardsRect = pygame.Rect((x,y), (playerAltWidth/4,playerAltHeight))
    playerBlockRect = pygame.Rect((x,y), (playerBlockWidth,playerBlockHeight))


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

    if (y_dir > 0) and (y > (P5Y-50)):
        if playerPlatformRect.colliderect(platform5Rect):
            y_dir = 0
            y = P5Y-playerHeight+2
            grounded = True
            jumpsLeft = 2

    if (y_dir > 0) and (y > (P6Y-50)):
        if playerPlatformRect.colliderect(platform6Rect):
            y_dir = 0
            y = P6Y-playerHeight+2
            grounded = True
            jumpsLeft = 2

    if (y_dir > 0) and (y > (P7Y-50)):
        if playerPlatformRect.colliderect(platform7Rect):
            y_dir  = 0
            y = P7Y-playerHeight+2
            grounded = True
            jumpsLeft = 2

    if (y_dir > 0) and (y > (P8Y-50)):
        if playerPlatformRect.colliderect(platform8Rect):
            y_dir  = 0
            y = P8Y-playerHeight+2
            grounded = True
            jumpsLeft = 2

    if (y_dir > 0) and (y > (P9Y-50)):
        if playerPlatformRect.colliderect(platform9Rect):
            y_dir  = 0
            y = P9Y-playerHeight+2
            grounded = True
            jumpsLeft = 2

    if (y_dir > 0) and (y > (P10Y-50)):
        if playerPlatformRect.colliderect(platform10Rect):
            y_dir  = 0
            y = P10Y-playerHeight+2
            grounded = True
            jumpsLeft = 1


    if (y_dir > 0) and (y > (P11Y-50)):
        if playerPlatformRect.colliderect(platform11Rect):
            y_dir  = 0
            y = P11Y-playerHeight+2
            grounded = True
            jumpsLeft = 2

    if (y_dir > 0) and (y > (P12Y-50)):
        if playerPlatformRect.colliderect(platform12Rect):
            y_dir  = 0
            y = P12Y-playerHeight+2
            grounded = True
            jumpsLeft = 2

    if (y_dir > 0) and (y > (P13Y-50)):
        if playerPlatformRect.colliderect(platform13Rect):
            y_dir  = 0
            y = P13Y-playerHeight+2
            grounded = True
            jumpsLeft = 2

    if (y_dir > 0) and (y > (P14Y-50)):
        if playerPlatformRect.colliderect(platform14Rect):
            y_dir  = 0
            y = P14Y-playerHeight+2
            grounded = True
            jumpsLeft = 2

    if (y_dir > 0) and (y > (P15Y-50)):
        if playerPlatformRect.colliderect(platform15Rect):
            y_dir  = 0
            y = P15Y-playerHeight+2
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
    
    if (not (len(enemyList) >= NUMBER_OF_BADGUYS)):
        if ((BADDIE_RESPAWN) == 0):
            addBaddie()
            

    else:
        for item in enemyList:
            singleBaddie(item)
            if facingRight:
                if heldEKey:
                    if playerAltRect.colliderect(item.rect):
                        PkillB = True
                    if PkillB:
                        PkillB = False
                        enemyList.remove(item)
                elif blocking:
                    if playerBlockRect.colliderect(item.rect):
                        pass

                else:
                    if playerRect.colliderect(item.baddieKillRect):
                        #alive = False#############################
                        pass
            else:
                if heldEKey:
                    if playerAltBackwardsRect.colliderect(item.rect):
                        PkillB = True
                    if PkillB:
                        PkillB = False
                        enemyList.remove(item)

                elif blocking:
                    if playerBlockRect.colliderect(item.rect):
                        pass

                else:
                    if playerRect.colliderect(item.baddieKillAltRect):
                        #alive = False            ##########################################
                        pass
                    

                            
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

    

        

    #fire()

    clock.tick(FPS)    

    pygame.display.update()

if not alive:
    pygame.quit()

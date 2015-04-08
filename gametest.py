



import pygame, sys

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

SCREEN_SIZE  = (800, 600)

mif = "target.png"

pygame.init()

screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)

player = pygame.image.load(mif).convert_alpha()

pygame.display.set_caption("HELLO? anyone?")

clock = pygame.time.Clock()

screen.fill(WHITE)

escape = True
while escape:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            escape = False
            pygame.quit()
            sys.exit()


    #screen.fill(BLUE)

    #x,y = pygame.mouse.get_pos()
    #x -= player.get_width()/2
    #y -= player.get_height()/2

    y = 300
    x = 100
    y_dir = 0
    x_dir = 0

    while True:

        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    y_dir = 1
                if event.key == pygame.K_s:
                    y_dir = -1
                if event.key == pygame.K_a:
                    x_dir = -1
                if event.key == pygame.K_d:
                    x_dir = 1

            if event.type == pygame.KEYUP:
                if (event.key == pygame.K_w) or (event.key == pygame.K_s):
                    y_dir = 0
                if (event.type == pygame.K_a) or (event.key == pygame.K_d):
                    x_dir = 0
            
                    

    screen.blit(player , (x,y))

    clock.tick(50)

    pygame.display.flip()

    
    


                

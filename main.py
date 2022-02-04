import pygame
from pygame.locals import *
from mapHandler import *
import sys

 
 
#pygame init
pygame.init()
DISPLAYSURF = pygame.display.set_mode((1920, 1080), DOUBLEBUF)    #set the display mode, window title and FPS clock
pygame.display.set_caption('Le jeu bg')
FPSCLOCK = pygame.time.Clock()


#map init
map_init()
map_data = getMap()             
displayMap(DISPLAYSURF)
 
 
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
    pygame.display.flip()
    FPSCLOCK.tick(30)
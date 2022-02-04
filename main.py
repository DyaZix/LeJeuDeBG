import pygame
from pygame.locals import *
from mapHandler import *
import sys

 
 
#pygame init
pygame.init()
WINDOW = pygame.display.set_mode((1920, 1080), DOUBLEBUF)    #set the display mode, window title and FPS clock
pygame.display.set_caption('Le jeu bg')
FPSCLOCK = pygame.time.Clock()


#map init
map_init()
map_data = getMap() 
loadTextures()            
displayMap(WINDOW)

#music init & start
file = 'terraria.mp3'
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(file)
pygame.mixer.music.play(-1)     # If the loops is -1 then the music will repeat indefinitely.
pygame.mixer.music.set_volume(0.06)
 
 
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
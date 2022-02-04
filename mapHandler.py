import pygame
from pygame.locals import *
import random


#caracteristics
MAP_LENGTH = 26
MAP_WIDTH = 26
EXT_WALLS_SIZE = 3
PATH_SIZE = int((MAP_LENGTH * MAP_WIDTH)*3)

#map data values /!\AND/!\ textures[] index
WALL = 1
GRASS = 0


#data declaration   map_data = 2D list
map_data = []

#here will be stored the loaded images
textures = []

def map_init():
    
    #   map example
    #   GRASS = 0   &   WALL = 1 

    """"
    map_data = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]  
    """
    
    #map data initialisation
    for row in range(MAP_WIDTH):
        row = []
        for row_nb in range(MAP_LENGTH):
            row.append(1)
            
        map_data.append(row)
        
    pathMaking() 
    
    
#pathMaking algorithm
#creates the navigable area on the map
def pathMaking():
    row = int(MAP_WIDTH/2)
    row_nb = int(MAP_LENGTH/2)
    
    map_data[int(MAP_WIDTH/2)][int(MAP_LENGTH/2)] = GRASS
    
    for PATH_iterator in range(PATH_SIZE):
        row, row_nb = step(row, row_nb)
        

#moves the position of the path algorithm in a coherent direction
def step(row, row_nb):
    
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4
    

    while True:
        
        PATHChoice = random.randint(1, 4)           #   1 = up      2 = down    3 = left    4 = right
        
        if PATHChoice == UP:
            row += 1
            
        elif PATHChoice == DOWN:
            row -= 1
        
        elif PATHChoice == LEFT:
            row_nb -= 1
        
        else:
            row_nb += 1

        if row != (0 + EXT_WALLS_SIZE) and row != (MAP_WIDTH-EXT_WALLS_SIZE) and row_nb != (0 + EXT_WALLS_SIZE) and row_nb != (MAP_LENGTH-EXT_WALLS_SIZE):
            break
        else:
            if PATHChoice == UP:
                row -= 1
            
            elif PATHChoice == DOWN:
                row += 1
            
            elif PATHChoice == LEFT:
                row_nb += 1
            
            else:
                row_nb -= 1

    map_data[row][row_nb] = GRASS
    
    return row, row_nb;
    
    
def printMap():
    for row in range(MAP_WIDTH):
        print(map_data[row][:])     

def getMap():
    return map_data    


def displayMap(DISPLAYSURF):
    
    TILEWIDTH       = 64  #holds the tile width and height
    TILEHEIGHT      = 64
    TILEHEIGHT_HALF = TILEHEIGHT /2
    TILEWIDTH_HALF  = TILEWIDTH /2
    
    for row_nb, row in enumerate(map_data):              #for every row of the map...
        for col_nb, tile in enumerate(row):
            if tile == WALL:
                tileImage = textures[WALL]
            elif tile == GRASS:
                tileImage = textures[GRASS]
            cart_x = row_nb * TILEWIDTH_HALF
            cart_y = col_nb * TILEHEIGHT_HALF  
            iso_x = (cart_x - cart_y) 
            iso_y = (cart_x + cart_y)/2
            centered_x = DISPLAYSURF.get_rect().centerx + iso_x
            centered_y = DISPLAYSURF.get_rect().centery/2 + iso_y
            DISPLAYSURF.blit(tileImage, (centered_x, centered_y))   #display the actual tile

def loadTextures():
    wall_texture  = pygame.image.load('Assets/wall.png').convert_alpha() 
    grass_texture = pygame.image.load('Assets/grass.png').convert_alpha()
    
    textures.append(grass_texture)
    textures.append(wall_texture)
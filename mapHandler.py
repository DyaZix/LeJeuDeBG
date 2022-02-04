import pygame
from pygame.locals import *
import sys
import random


WALL = 1
GRASS = 0

MAP_LENGTH = 26
MAP_WIDTH = 26

EXT_WALLS_SIZE = 3

map_data = []

GRASS_SIZE = int((MAP_LENGTH * MAP_WIDTH)*3)

def map_init():
    
    #   map example
    #   GRASS = 0   &   WALL = 1 

    """"
    map_data = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]  
    """
    
    
    for row in range(MAP_WIDTH):
        row = []
        for row_nb in range(MAP_LENGTH):
            row.append(1)
        map_data.append(row)
        
    pathMaking() 
    
    
            

def pathMaking():
    row = int(MAP_WIDTH/2)
    row_nb = int(MAP_LENGTH/2)
    
    map_data[int(MAP_WIDTH/2)][int(MAP_LENGTH/2)] = GRASS
    
    for GRASS_iterator in range(GRASS_SIZE):
        row, row_nb = step(row, row_nb)

    
def step(row, row_nb):
    
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4
    

    while True:
        
        GRASSChoice = random.randint(1, 4)           #   1 = up      2 = down    3 = left    4 = right
        
        if GRASSChoice == UP:
            row += 1
            
        elif GRASSChoice == DOWN:
            row -= 1
        
        elif GRASSChoice == LEFT:
            row_nb -= 1
        
        else:
            row_nb += 1

        if row != (0 + EXT_WALLS_SIZE) and row != (MAP_WIDTH-EXT_WALLS_SIZE) and row_nb != (0 + EXT_WALLS_SIZE) and row_nb != (MAP_LENGTH-EXT_WALLS_SIZE):
            break
        else:
            if GRASSChoice == UP:
                row -= 1
            
            elif GRASSChoice == DOWN:
                row += 1
            
            elif GRASSChoice == LEFT:
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
    
    
    wall_texture  = pygame.image.load('Assets/wall.png').convert_alpha() 
    grass_texture = pygame.image.load('Assets/grass.png').convert_alpha()
    
    for row_nb, row in enumerate(map_data):              #for every row of the map...
        for col_nb, tile in enumerate(row):
            if tile == WALL:
                tileImage = wall_texture
            elif tile == GRASS:
                tileImage = grass_texture
            cart_x = row_nb * TILEWIDTH_HALF
            cart_y = col_nb * TILEHEIGHT_HALF  
            iso_x = (cart_x - cart_y) 
            iso_y = (cart_x + cart_y)/2
            centered_x = DISPLAYSURF.get_rect().centerx + iso_x
            centered_y = DISPLAYSURF.get_rect().centery/2 + iso_y
            DISPLAYSURF.blit(tileImage, (centered_x, centered_y))   #display the actual tile

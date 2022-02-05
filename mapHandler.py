import pygame
from pygame.locals import *
import random
from camera import *
import sys

class mapHandler:
    
    
    def __init__(self):

        #caracteristics
        self.MAP_LENGTH = 300
        self.MAP_WIDTH = 300
        self.EXT_WALLS_SIZE = 1
        self.PATH_SIZE = int(((self.MAP_LENGTH * self.MAP_WIDTH)))

        #map data values /!\AND/!\ textures[] index
        self.WALL = 1
        self.GRASS = 0


        #data declaration   map_data = 2D list
        self.map_data = []


        #textures caracteristics
        self.TILEWIDTH       = 64  #holds the tile width and height
        self.TILEHEIGHT      = 64
        self.TILEHEIGHT_HALF = self.TILEHEIGHT /2
        self.TILEWIDTH_HALF  = self.TILEWIDTH /2


        #here will be stored the loaded images
        self.textures = []
        
        self.map_areas_init()
        

    def map_areas_init(self):
        
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
        for row in range(self.MAP_WIDTH):
            row = []
            for row_nb in range(self.MAP_LENGTH):
                row.append(1)
                
            self.map_data.append(row)
            
        self.pathMaking() 
    
    
    #pathMaking algorithm
    #creates the navigable area on the map
    def pathMaking(self):
        row = int(self.MAP_WIDTH/2)
        row_nb = int(self.MAP_LENGTH/2)
        
        self.map_data[int(self.MAP_WIDTH/2)][int(self.MAP_LENGTH/2)] = self.GRASS
        
        self.path(row, row_nb)
        
        
    def path(self, row, row_nb):
        path_size = self.PATH_SIZE

        for PATH_iterator in range(path_size):
            if (PATH_iterator%10 == 0):
                for i in range(12):
                    row, row_nb = self.step(row, row_nb)
            row, row_nb = self.step(row, row_nb)
        
            

    #moves the position of the path algorithm in a coherent direction
    def step(self, row, row_nb):
        
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
                
            #if the current path position is not into the exterior walls
            if row != (0 + self.EXT_WALLS_SIZE) and row != (self.MAP_WIDTH - self.EXT_WALLS_SIZE) and row_nb != (0 + self.EXT_WALLS_SIZE) and row_nb != (self.MAP_LENGTH - self.EXT_WALLS_SIZE):
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

        self.map_data[row][row_nb] = self.GRASS
        
        return row, row_nb;
        
        
    def printMap(self):
        for row in range(self.MAP_WIDTH):
            print(self.map_data[row][:])     

    def getMap(self):
        return self.map_data    

    #converts the 2D cartesian map to an isometric one and displays it
    def displayMap(self, WINDOW, camera):
        
        WINDOW.fill((0, 0, 0))
        
        #!TODO search into the map using camera coordinates
        #iterates throught the map data
        for row_nb, row in enumerate(self.map_data):    
            for col_nb, tile in enumerate(row):
                
                #Cartesian position of the texture
                cart_x = row_nb * self.TILEWIDTH_HALF
                cart_y = col_nb * self.TILEHEIGHT_HALF  
                
                #Isometric position of the texture
                iso_x  = (cart_x - cart_y) 
                iso_y  = (cart_x + cart_y)/2
                
                
                if iso_x >= int(camera.getXPosition() - (1920/2 + self.TILEWIDTH_HALF)) and iso_y >= int(camera.getYPosition() - (1080/2 + self.TILEHEIGHT_HALF)):
                    
                    if iso_x <= int(camera.getXPosition() + 1920/2) and  iso_y <= int(camera.getYPosition() + 1080/2):
                        #choosing the texture to display
                        if tile == self.WALL:
                            tileImage = self.textures[self.WALL]
                        elif tile == self.GRASS:
                            tileImage = self.textures[self.GRASS]
                        
                        #pos = center of the texture
                        centered_x = WINDOW.get_rect().centerx + iso_x
                        centered_y = WINDOW.get_rect().centery/2 + iso_y
                        
                        #displays the texture    
                        #31 30
                        
                        WINDOW.blit(tileImage, (centered_x - camera.getXPosition(), centered_y - camera.getYPosition() + 300))  
                    elif iso_x > int(camera.getXPosition() + 1920/2) and  iso_y > int(camera.getYPosition() + 1080/2):
                        break

    def loadTextures(self):
        
        #load each textures
        wall_texture  = pygame.image.load('Assets/wall.png').convert_alpha() 
        grass_texture = pygame.image.load('Assets/grass.png').convert_alpha()
        
        #add each textures to the textures list
        self.textures.append(grass_texture)
        self.textures.append(wall_texture)
'''This is the file that manages our levels'''
from settings import * 
from sprites import Sprite
from player import Player

class Level:
    def __init__(self,tmx_map):
        # get the surface from the main game loop so we can have access to it and draw on it here
        self.display_surface = pygame.display.get_surface()
        
        #groups of sprites 
        self.all_sprites = pygame.sprite.Group()
        
        
        # pass the map to the setup
        self.setup(tmx_map)
        
    def setup(self,tmx_map):
        # looping through the tmx map layer named Terrain
        for x,y,surf in tmx_map.get_layer_by_name('Terrain').tiles():
            # creating a basic sprite to display the images on our map layers
            # the x and y value are positions in a grid 
            # there for we need to multiply it by the game tile size 
            # or size of the images in our game
            Sprite((x * TILE_SIZE,y* TILE_SIZE),surf,self.all_sprites)
            
        for obj in tmx_map.get_layer_by_name('Objects'):
            if obj.name == 'player':
                Player(pos=(obj.x,obj.y),groups=self.all_sprites)
            
        
    def run(self,dt):
        ''' Run our level class mostly draw the level and its objects'''
        #this will update all the sprites that are in the same group
        self.all_sprites.update(dt)
        self.display_surface.fill('black')
        #draw all sprites onto the surface
        self.all_sprites.draw(self.display_surface)
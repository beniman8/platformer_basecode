''' This is the class that takes care of the players Sprite'''

from settings import *


class Player(pygame.sprite.Sprite):
    ''' This is the player Sprite'''

    def __init__(self, pos, groups):
        super().__init__(groups)

        self.image = pygame.Surface((25, 64))
        self.image.fill("red")
        #rectangle that goes around the image
        self.rect = self.image.get_frect(center=pos)
        
        #movement of the player
        self.direction = vector()
        self.speed = 200
        
        
    def input(self):
        ''' These are the controls for the player'''
        keys = pygame.key.get_pressed()
        input_vector = vector(0,0)
        input_vector.x = int(keys[pygame.K_RIGHT])-int(keys[pygame.K_LEFT])
        self.direction = input_vector.normalize() if input_vector else input_vector
        
        
    def move(self,dt):
        '''This is the movement of the player'''
        
        self.rect.topleft += self.direction * self.speed * dt
        
    def update(self,dt):
        ''' this update gets called on the main.py file with all the other groups'''
        self.input()
        self.move(dt)

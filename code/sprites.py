'''  
This is the sprites or images that are uploaded into the game .
This is a simple base class for visible game objects
https://www.pygame.org/docs/ref/sprite.html



'''

from settings import *


class Sprite(pygame.sprite.Sprite):

    # Constructor. Pass in the pos, surface and groups of the sprite,
    # and its x and y position
    def __init__(self, pos,surf,groups):
        # Call the parent class (Sprite) init method
        super().__init__(groups)

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface((TILE_SIZE,TILE_SIZE))
        self.image.fill('white')

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_frect(topleft=pos)

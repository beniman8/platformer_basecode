"""This is where our main game loop goes"""

from settings import *
from level import Level
from pytmx.util_pygame import load_pygame
from os.path import join

class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOWS_WIDTH, WINDOWS_HEIGHT))
        pygame.display.set_caption(GAME_TITLE)
        self.clock = pygame.time.Clock()
        
        
        # loading tmx map built using Tiled
        self.tmx_maps = {0: load_pygame(join('data','levels','omni.tmx'))}

        # creating our starting level
        self.current_stage = Level(self.tmx_maps[0]) # we are passing the map to the level

    def run(self):

        while True:
            # controlling the frame rate per seconds 
            dt = self.clock.tick()/1000

            # looping around all the possible events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # updating the display screen in the game loop
            self.current_stage.run(dt)
            pygame.display.update()


# make sure this is the file that needs to run
if __name__ == "__main__":
    game = Game()
    game.run()

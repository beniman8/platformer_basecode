"""This is where our main game loop goes"""

from settings import *
from level import Level


class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOWS_WIDTH, WINDOWS_HEIGHT))
        pygame.display.set_caption(GAME_TITLE)

        # creating our starting level
        self.current_stage = Level()

    def run(self):

        while True:

            # looping around all the possible events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # updating the display screen in the game loop
            self.current_stage.run()
            pygame.display.update()


# make sure this is the file that needs to run
if __name__ == "__main__":
    game = Game()
    game.run()

#Creating a Pygame window and responding to the user input
import sys
import pygame
from alien_game.settings import Settings
from alien_game.utils import Ship


class AlienInvasion:
    """ Overall class to manage game assets and behaviors"""

    def __init__(self):
        """Intialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode( (self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        self.bg_image = pygame.image.load(r"alien_game\images\bg_img.bmp")
        self.bg_image = pygame.transform.smoothscale(self.bg_image, self.screen.get_size())
        #self.bg_color = (230,230,230)
        

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            #Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            #redraw the screen during each pass through the loop.
            #self.screen.fill(self.settings.bg_color)
            self.screen.blit(self.bg_image, (0,0))
            self.ship.blitme()

            #Make the most recently drawn screen visible.
            pygame.display.flip()
            self.clock.tick(60)


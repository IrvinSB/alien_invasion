import pygame

class Ship:
    """A class to manage the ship"""
    def __init__(self,ai_game):
        self.screen = ai_game.screen
        self.screen_rect= ai_game.screen.get_rect()

        #load the ship image and get its rect
        self.image = pygame.image.load('alien_game\images\ship.bmp')
        self.image = pygame.transform.smoothscale(self.image, (102, 102))


        self.rect = self.image.get_rect()

        #Start each new ship at the bottom center of the screen   
        self.rect.midbottom = self.screen_rect.midbottom
    
    def blitme(self):
        """Draw ship at its current location"""
        self.screen.blit(self.image, self.rect)


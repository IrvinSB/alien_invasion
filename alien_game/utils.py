import pygame
from pygame.sprite import Sprite

class Ship:
    """A class to manage the ship"""
    def __init__(self,ai_game):
        self.screen = ai_game.screen
        self.screen_rect= ai_game.screen.get_rect()

        #load the ship image and get its rect
        self.image = pygame.image.load('alien_game\images\ship.bmp')
        self.image = pygame.transform.smoothscale(self.image, (54, 54))


        self.rect = self.image.get_rect()

        #Start each new ship at the bottom center of the screen   
        self.rect.midbottom = self.screen_rect.midbottom
        self.moving_right = False
        self.moving_left = False
        self.settings = ai_game.settings
    
    def blitme(self):
        """Draw ship at its current location"""
        self.screen.blit(self.image, self.rect)

    def updateme(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.settings.ship_speed
            #print(f"right Ship position: {self.rect.x} ")

        if self.moving_left and self.rect.left > 0:
            self.rect.x -= self.settings.ship_speed
            #print(f"left Ship position: {self.rect.x}")

class Bullet(Sprite):
    """A class to manage bullets fired"""

    def __init__(self, ai_game):
        """Create a bullet object at the ships current position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        #Create a bullet rect at (0,0) and then set the correct position
        self.rect = pygame.Rect(0,0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        #store the bullets position as float.
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet up the screen"""
        #Update the exact position of the bullet
        self.y -= self.settings.bullet_speed
        #Update the rect position.
        self.rect.y = self.y 

    def draw_bullet(self):
        """Draw the bullet to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)



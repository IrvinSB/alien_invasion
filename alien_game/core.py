#Creating a Pygame window and responding to the user input
import sys
import pygame
from alien_game.settings import Settings
from alien_game.utils import Ship , Bullet


class AlienInvasion:
    """ Overall class to manage game assets and behaviors"""

    def __init__(self):
        """Intialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()
        self.clock = pygame.time.Clock()

       # self.screen = pygame.display.set_mode( (self.settings.screen_width,self.settings.screen_height))
       
        self.screen = pygame.display.set_mode( (0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height =self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.bg_image = pygame.image.load(r"alien_game\images\bg_img.bmp")
        self.bg_image = pygame.transform.smoothscale(self.bg_image, self.screen.get_size())
        #self.bg_color = (230,230,230)
        
        

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.ship.updateme()
            self._update_bullets()
            self._update_screen()
            self.clock.tick(60)

    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)


    def _check_events(self):
       """Watch for keyboard and mouse events."""
       for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._keyups_events(event)
                
    def _keydown_events(self,event):
        """Actions for key presses"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

            

    
    def _keyups_events(self,event):
        """Action for key ups"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False


        

    def _update_screen(self):
        """Redraw the screen during each pass through the loop"""
        self.screen.blit(self.bg_image, (0,0))  #instead of filling the screen with bg color, fills with image
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme() 

        #Make the most recently drawn screen visible.
        pygame.display.flip()
        pass

    def _fire_bullet(self):
        """create new bullet and add it to the sprite group"""
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
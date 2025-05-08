#Creating a Pygame window and responding to the user input
import sys
from time import sleep
import pygame
from alien_game.settings import Settings
from alien_game.utils import Ship , Bullet , Alien, GameStats


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
        self.game_active = True
        pygame.display.set_caption("Alien Invasion")
        self.stats = GameStats(self)
        self.ship = Ship(self)
        self.aliens = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.bg_image = pygame.image.load(r"alien_game\images\bg_img.bmp")
        self.bg_image = pygame.transform.smoothscale(self.bg_image, self.screen.get_size())
        #self.bg_color = (230,230,230)
        self._create_fleet()
        
        
        

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()

            if self.game_active:
                self.ship.updateme()
                self._update_bullets()
                self._update_aliens()
            

            self._update_screen()
            self.clock.tick(60)

    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self._check_bullet_alien_collisions()
        
        
    
    def _check_bullet_alien_collisions(self):
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, False,True)
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()

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

    def _create_fleet(self):
        """Create aliens"""
        alien = Alien(self)
        alien_width,alien_height = alien.rect.size

        current_x = alien_width
        current_y = alien_height -60
        while current_y <(self.settings.screen_height - 4*alien_height):
            while current_x < (self.settings.screen_width - 2*alien_width):
                self._create_alien(current_x,current_y)
                current_x += 2*alien_width
            current_x = alien_width
            current_y += 1.1*alien_height
        
    def _create_alien(self, x_position, y_position):
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)


    def _update_screen(self):
        """Redraw the screen during each pass through the loop"""
        self.screen.blit(self.bg_image, (0,0))  #instead of filling the screen with bg color, fills with image
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme() 
        self.aliens.draw(self.screen)

        #Make the most recently drawn screen visible.
        pygame.display.flip()
        pass

    def _fire_bullet(self):
        """create new bullet and add it to the sprite group"""
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()

        #look for alien ship collisions
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        self._check_alien_bottom()
        

    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += alien.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1 

    def _ship_hit(self):
        if self.stats.ships_left >0:
            self.stats.ships_left -=1 
            self.bullets.empty()
            self.aliens.empty()

            self._create_fleet()
            self.ship.center_ship()
            sleep(0.5)
        else:
            self.game_active = False

        

    def _check_alien_bottom(self):
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                self._ship_hit()
                break

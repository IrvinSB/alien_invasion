class Settings:
    """To store all settings for the alien invasion game"""

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0,8,20)
        self.ship_speed = 2
        #Bullet settings
        self.bullet_speed = 3.0
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = (255,255,255)
        self.bullet_allowed = 4
        self.alien_speed = 2.0
        self.fleet_drop_speed = 10
        #fleet direction 1 is right -1 is going left
        self.fleet_direction = 1
        self.ship_limit = 3



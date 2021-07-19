class Settings:
    """ creating settings which has all the settings of our game"""
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 51)

        self.ship_speed = 1.5
        
        self.bullet_speed = 1.5
        self.bullets_allowed = 9

        self.alien_speed = 1.0
        self.fleet_drop_speed = 10

        self.fleet_direction = 1
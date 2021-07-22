class Settings:
    """ creating settings which has all the settings of our game"""
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 51)

        self.bullets_allowed = 9

        self.fleet_drop_speed = 10


        self.ship_limit = 3

        self.speedup_scale = 1.1
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.alien_speed = 1.0
        self.ship_speed = 1.5
        self.fleet_direction = 1
        self.bullet_speed = 1.5
        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale 
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)
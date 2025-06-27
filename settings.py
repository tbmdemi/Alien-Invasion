from datetime import datetime
class Settings:
    """A class to store all setting for AI"""
    def __init__(self):

        # Screen
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed = 0.25

        # Bullet settings
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3

        # Alien settings
        self.alien_speed = 0.1
        self.fleet_drop_speed = 0.1
        self.ship_limit = 3
        # fleet direction of 1 represent right, -1 represents left
        self.fleet_direction = 1

        # How quickly the game speeds up
        self.speedup_scale = 1.1
        self.score_scale = 1.5

        # Scoring
        self.alien_points = 50
        self.initialize_dynamic_settings()

    def _status(self):
        print("Setting ready at {now}".format(now = datetime.now()))

    def initialize_dynamic_settings(self):

        """Initialize settings that change throughout the game"""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        # fleet_direction of 1 represents right, -1 represents left
        self.fleet_direction = 1

    def increase_speed(self):
        """Increase speed settings"""

        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)
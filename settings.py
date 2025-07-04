from datetime import datetime
class Settings:
    """A class to store all settings for Alien Invasion."""
    
    def __init__(self):
        # Screen settings
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
        # Fleet direction of 1 represents right, -1 represents left
        self.fleet_direction = 1

        # Speed and score scaling
        self.speedup_scale = 1.1
        self.score_scale = 1.5

        # Scoring
        self.alien_points = 50
        
        # Initialize dynamic settings
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        # Fleet direction of 1 represents right, -1 represents left
        self.fleet_direction = 1

    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
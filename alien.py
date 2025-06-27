import pygame
from datetime import datetime
from pygame.sprite import Sprite
import os


class Alien(Sprite):
    """A class to represent a single alien in the fleet"""

    def resource_path(filename):
        return os.path.join(os.path.dirname(__file__), "image", filename)

    ALIEN_IMAGE_DIRECTORY = resource_path("alien.bmp")

    def __init__(self, ai_game):
        """Initialize the alien and set its starting position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.WHITE = (255, 255, 255)

        # Load the alien image and set its rect attribute
        self.image = pygame.image.load(self.ALIEN_IMAGE_DIRECTORY).convert()
        self.rect = self.image.get_rect()

        self.image.set_colorkey(self.WHITE)
        # Start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position
        self.x = float(self.rect.x)

        self._status()

    def _status(self):
        print("ALIEN ready at {time}".format(time = datetime.now()))
    
    def update(self):
        """Move the alien to the right"""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x

    def check_edges(self):
        """Return true if alien is at edge of screen"""
        screen_rect = self.screen.get_rect()

        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True 
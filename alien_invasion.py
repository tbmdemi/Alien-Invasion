import sys
import pygame
from time import sleep

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game and create game resources."""
        pygame.init()

        self.settings = Settings()
        self.settings._status()
        self.stats = GameStats(self)

        self.screen = pygame.display.set_mode((0,0),
                                              pygame.FULLSCREEN)
        self.settings.screen_height = self.screen.get_rect().height
        self.settings.screen_width = self.screen.get_rect().width

        # Set name for the window
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

        self.aliens = pygame.sprite.Group()
        self._create_fleet()


    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self.bullets.update()
                self._update_alien()
                self._update_bullet()
            self._update_screen()


    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._handle_keydown(event)
            elif event.type == pygame.KEYUP:
                self._handle_keyup(event)

    def _handle_keydown(self, event):
        """Handle keydown events."""
        match event.key:
            case pygame.K_RIGHT:
                self.ship.moving_right = True
            case pygame.K_LEFT:
                self.ship.moving_left = True
            case pygame.K_UP:
                self.ship.moving_up = True
            case pygame.K_DOWN:
                self.ship.moving_down = True
            case pygame.K_q:
                sys.exit()
            case pygame.K_SPACE:
                self._fire_bullet()

    def _handle_keyup(self, event):
        """Handle keyup events."""
        match event.key:
            case pygame.K_RIGHT:
                self.ship.moving_right = False
            case pygame.K_LEFT:
                self.ship.moving_left = False
            case pygame.K_UP:
                self.ship.moving_up = False
            case pygame.K_DOWN:
                self.ship.moving_down = False

    def _update_screen(self):
        """Update the screen and draw all elements."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.aliens.draw(self.screen)
        
        pygame.display.flip()

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group"""
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet) 

    def _update_bullet(self):
        # Get rid of bullets that have disappear
            for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)

            self._check_bullet_alien_collison()

    def _check_bullet_alien_collison(self):
        """Respond to bullet-alien collisions"""
        collisions = pygame.sprite.groupcollide(
                self.bullets, self.aliens, True, True
            )

        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()

    def _create_fleet(self):
        """Create the fleet of aliens"""
        alien = Alien(self)
        alien_height, alien_width = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_alien_x = available_space_x // (2 * alien_width)

        # Determine the number of rows of aliens that fit on the screen
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height -
                             (3 * alien_height) - ship_height)
        
        number_rows = available_space_y // (2 * alien_height)

        # Create the full fleet of aliens
        for row in range(number_rows):
            for alien_number in range(number_alien_x):
                self._create_aliens(alien_number, row)

    def _create_aliens(self, alien_number, row_number):
        """Create an alien and place it in a row"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien_height+ 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _update_alien(self):
        """Check if the fleet is at an edge
            then update the positions of all aliens in the fleet"""
        self._check_fleet_edges()
        self.aliens.update()

        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            print("Ship hit!!!")
            self._ship_hit()

        # Look for aliens hitting the bottom of the screen
        self._check_alien_bottom()

    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop  the entire fleet and change the fleet's direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _ship_hit(self):
        """Respond to the ship being hit by an alien"""

        if self.stats.ships_left > 0 :
            # Decrement ships left
            self.stats.ships_left -= 1

            # Get rid of any remaining aliens and bullets
            self.aliens.empty()
            self.bullets.empty()

            # Create an new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()

            # Pause
            sleep(0.5)

        else:
            self.stats.game_active = False

    def _check_alien_bottom(self):
        """Check if any aliens have reached the bottom of the screen"""
        screen_rect = self.screen.get_rect()

        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:

                # Treat this the same as if the ship got it
                self._ship_hit()
                break
if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
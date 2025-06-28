class GameStats:
    """Track statistics for Alien Invasion"""

    def __init__(self, ai_game):
        """Initialize statistics"""
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = False

        # High score 
        self.high_score = 0

    def reset_stats(self):
        """Initialize statistics that can be change during the game"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
        self.aliens_shot = 0
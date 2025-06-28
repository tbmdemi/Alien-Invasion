# Alien Invasion Game

A classic space shooter game built with Python and Pygame, featuring smooth gameplay, scoring system, and progressive difficulty.

**Author:** Trịnh Bình Minh - Student at University of Engineering and Technology (UET)

## 🎮 Game Overview

Alien Invasion is a retro-style arcade game where you control a spaceship defending Earth from an alien invasion. Shoot down waves of aliens, earn points, and try to achieve the highest score possible!

## ✨ Features

- **Smooth Controls**: Use arrow keys to move your ship in all directions
- **Progressive Difficulty**: Game speed increases with each level
- **Scoring System**: Track your score, high score, and aliens destroyed
- **Multiple Lives**: Start with 3 ships, lose them all and game over
- **Level Progression**: Clear all aliens to advance to the next level
- **High Score Tracking**: Your best score is saved between sessions
- **Fullscreen Mode**: Immersive gaming experience

## 🎯 How to Play

### Controls
- **Arrow Keys**: Move ship (Up, Down, Left, Right)
- **Spacebar**: Fire bullets
- **Q**: Quit game
- **Mouse**: Click "Play" button to start new game

### Objective
- Destroy all aliens in each wave
- Avoid being hit by aliens
- Survive as long as possible to achieve high scores
- Each level increases in difficulty

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.10 or higher
- Pygame library

### Installation Steps

1. **Clone or download the project**
   ```bash
   # Navigate to the project directory
   cd "Alien Invasion"
   ```

2. **Install Pygame** (if not already installed)
   ```bash
   pip install pygame
   ```

3. **Run the game**
   ```bash
   python alien_invasion.py
   ```

## 📁 Project Structure

```
Alien Invasion/
├── alien_invasion.py      # Main game file
├── settings.py            # Game configuration and settings
├── game_stats.py          # Statistics tracking
├── ship.py               # Player ship class
├── alien.py              # Alien enemy class
├── bullet.py             # Bullet projectile class
├── button.py             # UI button class
├── score_board.py        # Score display system
├── test_game.py          # Basic functionality tests
├── image/                # Game assets
│   ├── ship.bmp          # Player ship sprite
│   └── alien.bmp         # Alien enemy sprite
└── README.md             # This file
```

## 🎮 Game Mechanics

### Ship Movement
- The ship moves smoothly using floating-point precision
- Movement speed is configurable in settings
- Ship is constrained to screen boundaries

### Alien Fleet
- Aliens move in formation across the screen
- When reaching screen edges, fleet drops down and changes direction
- Fleet speed increases with each level

### Bullet System
- Limited number of bullets on screen at once
- Bullets travel upward and disappear at screen top
- Collision detection with aliens

### Scoring
- Points awarded for each alien destroyed
- Point values increase with each level
- High score is tracked and displayed

### Lives System
- Start with 3 ships
- Lose a ship when hit by alien or alien reaches bottom
- Game over when all ships are lost

## ⚙️ Configuration

Game settings can be modified in `settings.py`:

```python
# Screen settings
self.screen_width = 1200
self.screen_height = 800

# Ship settings
self.ship_speed = 1.5

# Bullet settings
self.bullet_speed = 3.0
self.bullet_allowed = 3

# Alien settings
self.alien_speed = 1.0
self.fleet_drop_speed = 0.1

# Difficulty scaling
self.speedup_scale = 1.1
self.score_scale = 1.5
```

## 🧪 Testing

Run the test file to verify your Python environment:

```bash
python test_game.py
```

This will check:
- Python version compatibility
- Pygame installation
- Basic functionality

## 🐛 Troubleshooting

### Common Issues

1. **"No module named 'pygame'"**
   - Solution: Install pygame with `pip install pygame`

2. **"FileNotFoundError: No file 'image/ship.bmp'"**
   - Solution: Make sure you're running the game from the correct directory
   - Run from parent directory: `python "Alien Invasion/alien_invasion.py"`

3. **Game runs too fast/slow**
   - Solution: Adjust speed settings in `settings.py`

4. **Screen resolution issues**
   - Solution: Modify screen dimensions in `settings.py`

## 🎨 Customization

### Adding New Features
- **Power-ups**: Modify `ship.py` to add special abilities
- **Different alien types**: Extend `alien.py` with new enemy classes
- **Sound effects**: Add audio files and pygame.mixer integration
- **Background music**: Implement continuous soundtrack

### Visual Modifications
- Replace sprite images in the `image/` folder
- Adjust colors in `settings.py`
- Modify UI elements in `button.py` and `score_board.py`

## 📝 Code Quality

The codebase follows clean code principles:
- Clear variable and function naming
- Comprehensive documentation
- Modular design with separate classes
- Consistent formatting and style
- Error handling and edge cases

## 🤝 Contributing

Feel free to contribute improvements:
1. Fork the project
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- Built with Python and Pygame
- Inspired by classic arcade games
- Clean code principles applied throughout
- **Developer:** Trịnh Bình Minh - UET Student

---

**Enjoy playing Alien Invasion!** 🚀👾

*Developed by Trịnh Bình Minh - University of Engineering and Technology (UET)* 
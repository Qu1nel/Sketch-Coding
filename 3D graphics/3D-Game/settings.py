from math import tan, pi

__all__ = (
    'WIDTH', 'HEIGHT', 'FPS',
    'HALF_WIDTH', 'HALF_HEIGHT', 'TILE',
    'WHITE', 'BLACK', 'RED', 'GREEN', 'BLUE', 'DARKGRAY', 'PURPLE',
    'player_pos', 'player_angle', 'player_speed', 'sensitivity',
    'FOV', 'HALF_FOV', 'NUM_RAY', 'MAX_DEPTH', 'DELTA_ANGLE', 'DIST', 'PROJ_RATIO', 'SCALE'
)
# game settings
FPS = 120
WIDTH = 1664
HEIGHT = 928
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
TILE = 32

# player
player_pos = (HALF_WIDTH, HALF_HEIGHT)
player_angle = 0
player_speed = 2
sensitivity = 0.03

# ray casting settings
FOV = pi / 3
HALF_FOV = FOV / 2
NUM_RAY = 90
MAX_DEPTH = 700
DELTA_ANGLE = FOV / NUM_RAY
DIST = NUM_RAY / (2 * tan(HALF_FOV))
PROJ_RATIO = DIST * TILE * 10
SCALE = WIDTH // NUM_RAY

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (220, 0, 0)
GREEN = (0, 220, 0)
BLUE = (0, 0, 220)
DARKGRAY = (110, 110, 110)
PURPLE = (120, 0, 120)

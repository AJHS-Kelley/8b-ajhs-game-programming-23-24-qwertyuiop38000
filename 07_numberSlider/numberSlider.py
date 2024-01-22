# Number Slider, v0.0, William Castengera

import sys, random, pygame
# sys module provides access to system resources (i.e. Operating System Commands)

from pygame.locals import *
# Allows us to call functions from pygame using just the function name instead of module.function()
# Example: We can use draw() instead of pygame.draw() 

# Constants For Game Board
BOARDWIDTH = 4 # COLUMNS
BOARDHEIGHT = 4 # ROWS
TILESIZE = 80 # MEASURED IN PIXELS
WINDOWWIDTH = 640 # MEASURED IN PIXELS
WINDOWHEIGHT = 480 # MEASURED IN PIXELS
FPS = 30
BLANK = None
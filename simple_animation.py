# Simple Animation with PyGame, Areillee Butler, 2:32, 12/09/21, v0.5

import pygame, sys, time 
from pygame.locals import *

# Setup PyGame 
pygame.init()

# Setup the Window 
WINDOWWIDTH = 400 
WINDOWHEIGHT = 400 
windowSurfacw = pygame. display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_captioon('Animation Example!')

# Setup the direction varibales. 
DOWNLEFT = 'downleft'
DOWNRIGHT = 'downright'
UPLEFT = 'upleft'
UPRIGHT = 'upright'

MOVESPEED = 4

# Setup color values. 
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


# Setup the box data. 
b1 = {'rect':pygame.Rect(300, 80, 50, 100), 'color':RED, 'dir':UPRIGHT}
B2 = {'rect':pygame.Rect(200, 200, 20, 20), 'color':GREEN, 'dir':UPLEFT}
B3 = {'rect':pygame.Rect(100, 150, 60, 60), 'color':BLUE, 'dir':DOWNLEFT}
boxes = [b1, b2, b3]

# Run the game loop. 
while True: 
    # check for QUIT event. 
    for event in pygame.event.get():
        if event.type == QUIT: 
            pygame.quit()
            sys.exit()

            

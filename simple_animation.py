# Simple Animation with PyGame, Areillee Butler, 2:11, 12/09/21, v0.1

import pygame, sys, time 
from pygame.locals import *

# Setup PyGame 
pygame.init()

# Setup the Window 
WINDOWWIDTH = 400 
WINDOWHEIGHT = 400 
windowSurfacw = pygame. display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_captioon('Animation Example!')
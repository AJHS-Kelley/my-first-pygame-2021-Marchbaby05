# Simple Animation with PyGame, Areillee Butler, 2:16, 12/09/21, v0.2

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
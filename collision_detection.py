#PyGame Collision Detection practice, Butler Areillee, Janurary 15, 2022, 2:32PM, v0.2

import pygame, sys, random
from pygame.locals import *

# Setup PyGame 
pygame.init()
mainClock = pygame.time.Clock()

# Setup the PyGame window
WINDOWWIDTH = 400
WINDOWHEIGHT = 400 
windoSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('collision Detection 2022')
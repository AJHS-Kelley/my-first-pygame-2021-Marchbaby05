# My First PyGame, Areillee Butler, 12/1/21 2:10pm, v0.10

import pygame, sys 
from pygame.locals import *

# Start PyGame
pygame.init()

# Setup our window. 1 
windowSurface = pygame.display.set_mode((500, 400), 0, 32) 
pygame.display.set_caption('Hello, world') 

# Setup Colors
BLACK = (0,0,0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
FLOWERPINK = (255, 204, 255)
# Setup font. 
basicFont = pygame.font.SysFont(None, 48)

# Setup text.
text = basicFont.render('Hello, world' , True, WHITE, BLUE)
textReact = text.get_rect()
textRect.centerx = windowSurface.get_rect().centerx 
textRect.centery = windowSurface.get_rect().centery


#  Fill in the background 
windowSurface.fill(FLOWERPINK)

#  Draw a polygon onto the screen. 
pygame.draw.polygon(windowSurface, FLOWERPINK, ((146, 0), (291, 106), (236, 277)(56, 277), (0,106))) 

# Draw lines on the screen. 
pygame.draw.line(windowSurface,  BLUE,  (60,60,) (120, 60), 4) 
pygame.draw.line(windowSurface,  RED,  (0,150,) (60, 75), 1) 
pygame.draw.line(windowSurface,  WHITE,  (75,60,) (60, 75), 2) 

# Draw a circle. 
pygame.draw.circle(windowSurface, BLACK, (300,50), 20, 0) 

# draw an ellipse. 
pygame.draw.ellipse(windowSurface, RED, (300, 250, 40, 80), 1)

# Draw the text rectangle. 
pygame.draw.rect(windowSurface, RED, (textRect.left - 20, textRect.top - 20, textRect.width + 40, textRect.height + 40))

# Create Pixel Array
pixArray = pygame.pixelArray(windowSurface) 
pixelArray[480][380] = BLUE 
del pixArray 

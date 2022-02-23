#**Quick_Pygame_Template**********
#**This is a basic window with color and if using Pydroid3 screen can be rotated*********************************#**Add classes, functions, or just add basic shapes!*************************
#**Play around and have fun!!!********

import pygame
import random
from os import *


# Make path to Graphics
#img_dir = path.join(path.dirname(__file__), 'images/')
# Make path to Sounds
#snd_dir = path.join(path.dirname(__file__), 'sounds/')
#If you plan on using seperate folders for sounds and images uncomment lines 11 and 13 and add your own img & snd folders**************************

# initialize pygame and create window
pygame.init()
SCREEN = WIDTH, HEIGHT = 288, 512
info = pygame.display.Info()
width = info.current_w
height = info.current_h
if width >= height:
	win  = pygame.display.set_mode(SCREEN, pygame.NOFRAME)
else:
#Set fullscreen mode for mobile
	win = pygame.display.			set_mode(SCREEN, pygame.NOFRAME | pygame.SCALED | pygame.FULLSCREEN)
pygame.mixer.init()
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

#Define colors(variables)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
INDIGO = (75, 0, 130)
VIOLET = (238, 130, 238)
SILVER = (192, 192, 192)
GOLD = (255, 215, 0)

# Game loop
running = True
while running:
    # keep loop running at right  speed
 
    # Process events (input)
    for event in pygame.event.get():
        # check for closing the window
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
        	if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
        		running = False
        		
    # Update

    # Draw/ Render
    win.fill(GOLD)
    
    # *after drawing everything else, flip the display
    pygame.display.flip()

pygame.quit()
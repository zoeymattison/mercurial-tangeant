# Import GUI - pygame
# Import exit - sys

import pygame
from sys import exit
pygame.init()

# Set the default window size
# draw the screen
# set the window title
WINDOW_SIZE=(640,480)
WINDOW_BG=(20,15,30)
screen=pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Mercurial Tangeant")

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
    screen.fill(WINDOW_BG)
    pygame.display.update()
    
# Time to draw something
# screen=pygame.display.set_mode(WINDOW_SIZE) does two things:
# 1. Creates the visible window
# 2. Returns a pygame "surface" object representing its drawable
# area. The returned "object" is stored in the variable "screen"
# A "surface" is essentially a rectangular canvas made of pixels
# It can draw other things like text, borders, menus and other
# surfaces onto it (not into it)

# RGB colours
# Colours are commonly represented using 3 integers (a thruple?)
# (red, green, blue)
# Each component ranges from 0 to 255
# (0,0,0) Black
# (255,255,255) White
# (255,0,0) Red
# (0,255,0) Green
# (0,0,255) Blue

# Shocker it's still called a tuple lol

# Created a named colour
# WINDOW_BG=(20,15,30)
# Then use surface.fill()
# In this case, "surface" is to be replaced with the actual
# variable that the drawing is being stored in.
# "screen" is the surface for this (the only one)
# screen.fill(WINDOW_BG)
# It should be placed at the end of the loop but before the
# display update call.
# Why do we fill the screen during every loop iteration instead
# of only once before the loop?
# Maybe because if it gets overwritten it will never go back to
# the default?

# Pixels remain on the surface until something draws over them
# When an object mvoes, its pixels from the previous frame
# don't disappear automatically
# Each frame will eventually work like painting:
# 1. Clear the previous ptaining with the background colour
# 2. Draw everything in its current position
# 3. Present the finished drawing
# 4. Repeat
# Without clearing, moving text and objects would have trails
# behind

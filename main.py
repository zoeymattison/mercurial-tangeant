# Imports
# -- Pygame: Main GUI drawer
# -- Sys: To use exit()

import pygame
from sys import exit

# Initialize Pygame
pygame.init()

# Set the Clock
# pygame.time.Clock()
# Purpose: Creates an object that tracks and regulates time
# between loop iterations.
# Arguments: None
# Return value: a new Clock object
# Store the object in the variable clock
# Creating it does not limit anything. You also have to use its
# tick() method once per loop, at the bottom, after the display
# It is not like sleep as it involves measuring time between
# the last tick as opposed to just adding a delay
# It also returns the total elapsed time in ms
# object.tick(FPS)
# Note: it's uppercase Clock, not clock

clock=pygame.time.Clock()

# Set the window size, colour and FPS cap
WINDOW_SIZE=(640,480)
WINDOW_BG=(20,98,58)
FPS=60

# Drawing text takes 3 stages:
# Font definition -> Renfered text surface -> draw surface
# onto screen

# First, add a font size

FONT_SIZE=32

# Draw the main window and set the window title
screen=pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Mercurial Tangeant")

# Main process loop
while True:
    for event in pygame.event.get():
        # If the quit event is seen (like clicking X)
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()

    # Fill in the background colour
    screen.fill(WINDOW_BG)

    # Update the display
    pygame.display.update()

    # clock.tick(FPS)
    # Purpose: Measures the time since the previous call and waits
    # if the loop finished too quickly
    # Argument: the maximum number of iterations per second (60)
    # Returns: The number of milliseconds since the preceding
    # call to tick().
    # Called once per loop iteration
    clock.tick(FPS)
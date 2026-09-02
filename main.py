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
# Font definition >> Rendered text surface >> draw surface
# onto screen

# First, add a font size
# Then create a font object
# pygame.font.Font()
# Purpose: creates a font object used to render text
# First argument: the font file ("None" uses the built-in one)
# Second arg.: The font size in pixels
# Returns a font object
# !!It does not draw or display text by itself!!

FONT_SIZE=32
font=pygame.font.Font(None,FONT_SIZE)

# Add a text colour
TEXT_COLOUR=(255,255,255)

# font.render()
# Method converts a Python string into a surface
# Its arguments are:
# 1. The string
# 2. Antialiasing (True / False)
# 3. The colour (TEXT_COLOUR)
# 4. Background fill (omitted here)

opening_text=font.render(
    "Your alarm cuts through the silence...",
    True,
    TEXT_COLOUR
)

awake_text=font.render(
    "Silencing the alarm, you climb out of bed and stretch...",
    True,
    TEXT_COLOUR
)

# create a variable to store the current text on-screen
# starting with the first text. This is a "state".
current_text=opening_text

# Draw the main window and set the window title
screen=pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Mercurial Tangeant")

def choose_text(event,current_surface,next_surface):
    if event.type==pygame.KEYDOWN:
        if event.key==pygame.K_z:
            return next_surface
    return current_surface

# Main process loop
while True:
    for event in pygame.event.get():
        # If the quit event is seen (like clicking X)
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
        current_text=choose_text(event,current_text,awake_text)

    # Fill in the background colour
    screen.fill(WINDOW_BG)

    # screen.blit()
    # "blit" means copying pixels from one surface onto another
    # "screen" is the destination surface
    # "opening_text" is the source surface
    # (20,20) is the destination position
    # The return value is a Rect describing the changed area which does not need to be
    # stored at this time.
    # The coordinate system of pygame uses X and Y, in pixels (increasing)
    # Horizontal = X positive
    # Vertical = Y positive
    # from 0,0 in the top left corner
    # Coordinates can also be negative, placing text outside of the screen area
    
    # screen.blit(opening_text,(20,20))
    # change to state variable
    screen.blit(current_text,(20,20))

    # The drawing order matters
    # 1. Fill background
    # 2. Blit text onto the background
    # 3. Update the display
    # (ie. If you fill the background after adding the text, then the text will be
    # overwritten with the background colour))

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
# Test opening pygame window
# Import pygame's tools so the file can use them!
# pygame.init() initializes pygame's systems
# pygame.display.set_mode((640, 480)) creates a window

import pygame
pygame.init()

# There are two sets of parentheses doing different jobs
# Outer parentheses call the function set_mode()
# Inner parentheses create a tuple! (640, 480)
# So, the function receives one argument: a tuple containing two
# values.
# This is equivalent:
# window_size = (640, 480)
# screen = pygame.display.set_mode(window_size)

WINDOW_SIZE = (640, 480)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Mercurial Tangeant")

# In pygame's logic, set_mode is a function that receives
# one tuple containing the width and height.

pygame.time.wait(3000)

# .wait takes a numeric value in milliseconds

pygame.quit()

# .quit shuts it down

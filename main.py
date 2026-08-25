# Version 0.0.1

import pygame

# The safest way to close the code / window is actually to use the system
# call, "exit". So we need to import it here. Now the code will end, rather
# than hitting a conidition that can't run (no video update error message from
# pygame.display.update()

from sys import exit

pygame.init()
WINDOW_SIZE=(640,480)
screen=pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Mercurial Tangeant")

# in order to run a game with pygame, we need the code to never end, and loop
# back on itself until told to quit. For that reason, we use a while loop that
# is just set to True:

while True:
    # draw all elements
    # update everything
    # Event loop
    # pygame.event.get() gets us all the pygame "events"(?)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    # !!IMPORTANT!! you must write pygame.display.update() at the top
    # the update function constantly updates the game display (screen) with
    # whatever is drawn in here.
    pygame.display.update()

    # This is the basic framework. The window can now be opened and closed,
    # and doesn't exhibit any kind of stall or hang, since right now it's
    # waiting for an "event", which, in this case is closing the window.
    
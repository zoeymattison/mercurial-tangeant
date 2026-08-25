import pygame
pygame.init()
WINDOW_SIZE=(640,480)
screen=pygame.display.set_mode(WINDOW_SIZE)

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
    # !!IMPORTANT!! you must write pygame.display.update() at the top
    # the update function constantly updates the game display (screen) with
    # whatever is drawn in here.
    pygame.display.update()

    # This is the basic framework. The window can now be opened and closed,
    # and doesn't exhibit any kind of stall or hang, since right now it's
    # waiting for an "event", which, in this case is closing the window.
    
# Version 0.0.1

import pygame

# The safest way to close the code / window is actually to use the system
# call, "exit". So we need to import it here. Now the code will end, rather
# than hitting a condition that can't run (no video update error message from
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
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
    # !!IMPORTANT!! you must include this
    # the update function constantly updates the game display (screen) with
    # whatever is drawn in here.
    pygame.display.update()

    # This is the basic framework. The window can now be opened and closed,
    # and doesn't exhibit any kind of stall or hang, since right now it's
    # waiting for an "event", which, in this case is closing the window.
    

# What the loop is doing
# WHile True:
# True is a Boolean value. Because it never changes, this loop
# repeats indefinitely unless something inside explicitely exits
# the program. This is how we keep the window open, rather than
# having it be a process that starts and ends on its own
# The code isn't waiting for an event, it is repeatedl checking
# for events as quickly as the computer can run the loop.
# It's wise to implement an FPS cap. But do we need one
# Since there won't be any animations?

# pygame.event.get()
# Purpose: Retrieves events pygame has collected since the previous
# check.
# Arguments: None in the current context
# Return value: a collection of event objects
# Important behaviour: it removes the returned events from
# pygame's event queue

# Events
# An event can represent things such as closing the window,
# pressing or releasing a key,
# mouse activity
# rezising the window
# controller input
# This loop:
# for event in pygame.event.get():
# takes that collection and processes each event individually.
# During each repetition, event refers to one Event object

# What event.type means
# Each event has information stored inside it. Its type identified
# what kind of event occurred:
# if event.type == pygame.QUIT:
# pygame.QUIT is pygame's predefined alue for a request to close
# the window. It usually occurs when you click the window's X
# button.

# Closing the program
# pygame.quit()
# exit()
# pygame.quit() shuts down pygame's internalized systems.
# exit() raises a special Python signal called SystemExit,
# ending the udnerlying code (the "program").
# Witjout exit(), the while look continues, reaching pygame.display.update()
# after pygame's display has already been shut down, producing
# a video not initialized error (since the video is not alive anymore!)

# what pygame.display.update() does
# Its normal position is placed after drawing the screen,
# near the bottom of the loop. 
# Purpose: Makes drawing changes visible in the window
# Arguments: None here, meaning update the entire display
# Does not return any value
# Distinction: It does not draw anything and isn't what keeps
# the window responsive

# The intended order is:
# Process events
# update game state
# Draw the current frame
# show the completed frame

# TL;DR
# A while loop constantly loops and checks for changes.
# checking for pygame event input
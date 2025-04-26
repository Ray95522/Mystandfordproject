"""
File: Steeplechase.py
Name: Ray
---------------------------------
This program makes Karel crosses hurdles in a 12x12 world
"""

from karel.stanfordkarel import *


def main():
    """
    Karel crosses hurdles in a 12x12 world
    with a for loop 
    """
    for i in range(11):
       if front_is_clear():
           move()
       else:
           jump()


def jump():
    """
    pre-condition:Karel is on the left side of the wall,facing East
    post-condition:Karel is on the right side of the wall,facing East
    """

    up()
    cross()
    down()

def up():
    """
    pre-condition:Karel is on the left side of the wall,facing East
    post-condition:Karel is up at the upper left of the wall,facing North
    """
    turn_left()
    while not right_is_clear():
        move()


def turn_R():
    for i in range(3):
        turn_left()


def cross():
    """
    pre-condition:Karel is up at the upper left of the wall,facing North
    post-condition:Karel is at the upper right of the wall,facing South
    """

    turn_R()
    move()
    turn_R()


def down():
    """
    pre-condition:Karel is at the upper right of the wall,facing South
    post-condition:Karel is on the right side of the wall,facing East
    """
    while front_is_clear():
        move()
    turn_left()

# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)

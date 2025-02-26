import pygame
import sys

from Game import *

# Driver function
def Settings(difficulty, size):
    # Generate a game instance
    tictactoe = Game(difficulty,size)
    # Run the game
    tictactoe.run()
    pygame.quit()
    sys.exit()


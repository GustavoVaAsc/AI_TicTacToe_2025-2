import pygame
import sys

from Game import *

def Settings(difficulty, size):
    print(f"Difficulty: {difficulty}")
    print(f"Siz: {size}")
    tictactoe = Game(difficulty,size)
    tictactoe.run()
    pygame.quit()
    sys.exit()


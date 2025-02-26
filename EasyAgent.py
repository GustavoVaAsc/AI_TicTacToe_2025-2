from Agent import Agent
import random

class EasyAgent(Agent):
    def __init__(self):
        super().__init__()

    def checkMove(self, grid):
        available_moves = [i for i in range(1, grid.size + 1) if grid.board[i] == ' ']
        print(available_moves)
        if available_moves:
            move = random.choice(available_moves)  # Pick a random empty square
            print("Move: "+str(move))
            move -= 1
            grid.squares[move].clicked(grid.squares[move].x, grid.squares[move].y, 'x', grid, grid.x_asset)

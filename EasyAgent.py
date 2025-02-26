from Agent import Agent
import random

class EasyAgent(Agent):
    # Same initializer of father class
    def __init__(self):
        super().__init__()

    # Check if the agent can do a random move
    def checkMove(self, grid):
        # Generate available moves
        available_moves = [i for i in range(1, grid.size + 1) if grid.board[i] == ' ']
        if available_moves:
            move = random.choice(available_moves)  # Pick a random empty square
            move -= 1 # Check correct indexation
            # Execute move
            grid.squares[move].clicked(grid.squares[move].x, grid.squares[move].y, 'x', grid, grid.x_asset)

from Agent import Agent
import math

class MediumAgent(Agent):
    
    move = True
    comp_move = 0
    
    # Check for the danger moves
    danger_map = {} # Hash map
    
    def checkMove(self,grid):
        self.move = True # Initially we could move
        
        # Check if player 1 is threating us
        self.checkForThreat(grid)
        
        # Check if the game ended with victory
        if self.move:
            grid.checkForWin('o')
            
        if self.move:
            grid.checkForWin('x')
        
        # Check if there's a tie
        if not grid.is_gameover:
            grid.checkForTie()
        
        # We start checking if we could move in the center
        self.checkCentre(grid)

        # Then we check the corners
        if self.move:
            self.checkCorner(grid)
        
        # And finally the edges
        if self.move:
            self.checkEdge(grid)

        # If we determine that we could move
        if not self.move:
            # The AI moves
            for square in grid.squares:
                if square.number == self.comp_move:
                    square.clicked(square.x, square.y, 'x', grid, grid.x_asset)
                    break  # Ensure only one move is made
        
    # Function to check centre
    def checkCentre(self,grid):
        # Divide size /2
        centre_index = grid.size // 2
        # Check if cell is available
        if grid.board[centre_index] == ' ':
            self.comp_move = centre_index
            self.move = False # We could move
    
    # Function to check corners
    def checkCorner(self, grid):
        n = int(math.sqrt(grid.size))  # Determine the grid dimension (n x n)
    
        # Compute the four corner positions for variable size
        corners = [1, n, grid.size - n + 1, grid.size]
        
        # Iterate over the corners, checking if AI could move in someone
        for corner in corners:
            if grid.board[corner] == ' ':
                self.comp_move = corner
                self.move = False # AI could move
                break
    
    # Check the remaining cells
    def checkEdge(self,grid):
        # Move on the first remaining cell available
        for i in range(2,grid.size+1,2):
            if grid.board[i] == ' ':
                self.comp_move = i
                self.move = False
                break
    
    # Generate the position where AI could lose
    def generateDangerPositions(self, grid):
        for line in grid.winning_states:
            self.danger_map[tuple(line)] = line
    
    # Check if player is threating AI
    def checkForThreat(self, grid):
        # Check our danger map
        for line in self.danger_map.values():
            marks = [grid.board[pos] for pos in line]

            # If the opponent ('o') is one move away from winning
            if marks.count('o') == 2 and marks.count(' ') == 1:
                self.comp_move = line[marks.index(' ')]  # Block the winning move
                self.move = False
                return
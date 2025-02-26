from Agent import Agent
import math

class MediumAgent(Agent):
    
    move = True
    comp_move = 0
    danger_map = {}
    def checkMove(self,grid):
        self.move = True
        
        self.checkForThreat(grid)
        
        if self.move:
            grid.checkForWin('o')
            
        if self.move:
            grid.checkForWin('x')
        
        if not grid.is_gameover:
            grid.checkForTie()
        
        self.checkCentre(grid)

        if self.move:
            self.checkCorner(grid)

        if self.move:
            self.checkEdge(grid)

        if not self.move:
            for square in grid.squares:
                if square.number == self.comp_move:
                    square.clicked(square.x, square.y, 'x', grid, grid.x_asset)
                    break  # Ensure only one move is made
        
    def checkCentre(self,grid):
        centre_index = grid.size // 2
        if grid.board[centre_index] == ' ':
            self.comp_move = centre_index
            self.move = False
            
    def checkCorner(self, grid):
        n = int(math.sqrt(grid.size))  # Determine the grid dimension (n x n)
    
        # Compute the four corner positions
        corners = [1, n, grid.size - n + 1, grid.size]
        for corner in corners:
            if grid.board[corner] == ' ':
                self.comp_move = corner
                self.move = False
                break
                
    def checkEdge(self,grid):
        for i in range(2,grid.size+1,2):
            if grid.board[i] == ' ':
                self.comp_move = i
                self.move = False
                break
    
    def generateDangerPositions(self, grid):
        for line in grid.winning_states:
            self.danger_map[tuple(line)] = line
        
    def checkForThreat(self, grid):
        for line in self.danger_map.values():
            marks = [grid.board[pos] for pos in line]

            # Debugging output
            print(f"Checking line {line}: {marks}")

            # If the opponent ('o') is one move away from winning
            if marks.count('o') == 2 and marks.count(' ') == 1:
                print(f"Threat detected! Blocking at {line[marks.index(' ')]}")
                self.comp_move = line[marks.index(' ')]  # Block the winning move
                self.move = False
                return
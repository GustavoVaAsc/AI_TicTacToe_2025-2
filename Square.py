import pygame as game
#from Board import Board

# Class Square, extends Sprite class from pygame library
class Square(game.sprite.Sprite):
    # Constructor
    def __init__(self, x_id, y_id, number,image, board_size):
        super().__init__() # Call the father class constructor
        
        # Check the board size to determine the size of the square
        if board_size == 4:
            self.width = 180
            self.height = 180
        elif board_size == 5:
            self.width = 144
            self.height = 144
        else:
            self.width = 240
            self.height = 240
        
        # Set the parameters
        self.x = x_id * self.height
        self.y = y_id * self.height
        self.content = ' '
        self.number = number
        self.image = image
        self.image = game.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()
    
    # Update the square
    def update(self):
        self.rect.center = (self.x, self.y)
    
    # Check if this square is being clicked
    def clicked(self, x_val, y_val, turn, grid, image):
        if self.content == ' ': # If it's an empty cell
            if self.rect.collidepoint(x_val, y_val): # Obtaining the collide point
                self.content = turn # Check what turn is it
                grid.board[self.number] = turn # Set the move
                self.image = image # Change image
                self.image = game.transform.scale(self.image, (self.width, self.height))

                # Switch turn before AI moves
                if turn == 'x':
                    grid.turn = 'o'
                    grid.checkForWin('x')
                else:
                    grid.turn = 'x'
                    grid.checkForWin('o')
                    
                grid.move_count+=1 # Increment the moves done on the grid
                
                # Check for tie
                if not grid.is_gameover:
                    grid.checkForTie() 
                
                # AI moves
                if grid.turn == 'x' and not grid.is_gameover:
                    grid.checkMove()

                
                    
                
            
        


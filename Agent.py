# Agent super class, two agents are inherited from this

class Agent:
    move = True
    board = None
    
    # Overrideable on the children's method versions
    def checkMove(self):
        pass
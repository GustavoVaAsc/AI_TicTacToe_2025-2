<<<<<<< HEAD
class MinimaxAgent:

    #Tamaño del grid

    n=4

    #Declaración del grid

    grid=[]

    #Declaración símbolo de jugador

    symbol=[]

    player=None

    #Declaración del dp

    dp={}

    #Declaracion infinito
    INF=1e8

    #Jugador 

    def __init__(self):
        for i in range(self.n**2):
                self.grid.append('_')
        self.symbol.append('o')
        self.symbol.append('x')

    #Funcion para mostrar el grid

    def show(self):
        for i in range(self.n):
            for j in range(self.n):
                print(self.grid[i*self.n+j],end=" ")
            print()

    #Funcion para marcar una casilla del grid
=======
from Agent import Agent
import math

class MinimaxAgent(Agent):
    INF = float('inf')
    
    def __init__(self, grid):
        self.grid = grid.board
        self.n = int(math.sqrt(grid.size))
        self.symbol = ['o', 'x']
        self.dp = {}
        self.player = True

    def checkMove(self, real_board):
        self.grid = real_board.board
        self.bestMove(real_board)
    
    def mark(self, player, x, y):
        self.grid[x * self.n + y] = self.symbol[player]
>>>>>>> 6735ad5f3a14e6d4f1e7bec2cd806b801a660335

    def unmark(self, x, y):
        self.grid[x * self.n + y] = ' '

<<<<<<< HEAD
    def unMark(self,player,x,y):
        self.grid[x*self.n+y]='_'
=======
    def game_over(self):
        return all(cell != ' ' for cell in self.grid)
>>>>>>> 6735ad5f3a14e6d4f1e7bec2cd806b801a660335

    def valid_point(self, x, y):
        return 0 <= x < self.n and 0 <= y < self.n

<<<<<<< HEAD
    def gameOver(self):
        for i in range(self.n):
            for j in range(self.n):
                if(self.grid[i*self.n+j]=='_'):
                    return False
        return True

    #Función para verificar si un jugador ya gano

    def validPoint(self,x,y):
        if(x>=0 and x<self.n and y>=0 and y<self.n):
            return True
        return False
    

    def winner(self,player,x,y):

        if(self.grid[self.n*x+y]!=self.symbol[player]):
            return False
        
        #Checar vertical hacia adelante
        if(self.validPoint(x+2,y) and self.grid[self.n*(x+1)+y]==self.grid[self.n*(x+2)+y] and self.grid[self.n*(x+1)+y]==self.symbol[player]):
            return True
        
        #Checar vertical en medio
        if(self.validPoint(x+1,y) and self.validPoint(x-1,y) and self.grid[self.n*(x+1)+y]==self.grid[self.n*(x-1)+y] and self.grid[self.n*(x+1)+y]==self.symbol[player]):
            return True

        #vertical izquierda
        if(self.validPoint(x-2,y) and self.grid[self.n*(x-1)+y]==self.grid[self.n*(x-2)+y] and self.grid[self.n*(x-1)+y]==self.symbol[player]):
            return True 
        
        #Horizontal hacia arriba
        if(self.validPoint(x,y+2) and self.grid[self.n*x+y+1]==self.grid[self.n*x+y+2] and self.grid[self.n*x+y+1]==self.symbol[player]):
            return True
        
        #Horizontal hacia abajo
        if(self.validPoint(x,y-2) and self.grid[self.n*x+y-1]==self.grid[self.n*x+y-2] and self.grid[self.n*x+y-1]==self.symbol[player]):
            return True
        
        #Horizontal en medio
        if(self.validPoint(x,y+1) and self.validPoint(x,y-1) and self.grid[self.n*x+y+1]==self.grid[self.n*x+y-1] and self.grid[self.n*x+y+1]==self.symbol[player]):
            return True
        
        #Digonal positiva hacia arriba
        if(self.validPoint(x-2,y+2) and self.grid[self.n*(x-1)+y+1]==self.grid[self.n*(x-2)+y+2] and self.grid[self.n*(x-1)+y+1]==self.symbol[player]):
            return True
        #Diagonal positiva hacia abajo
        if(self.validPoint(x+2,y-2) and self.grid[self.n*(x+1)+y-1]==self.grid[self.n*(x+2)+y-2] and self.grid[self.n*(x+1)+y-1]==self.symbol[player]):
            return True
        #Diagonal positiva en medio
        if(self.validPoint(x+1,y-1) and self.validPoint(x-1,y+1) and self.grid[self.n*(x+1)+y-1]==self.grid[self.n*(x-1)+y+1] and self.grid[self.n*(x-1)+y+1]==self.symbol[player]):
            return True
        #Diagonal negativa hacia arriba
        if(self.validPoint(x+2,y+2) and self.grid[self.n*(x+1)+y+1]==self.grid[self.n*(x+2)+y+2] and self.grid[self.n*(x+1)+y+1]==self.symbol[player]):
            return True
        #Diagonal negativa hacia abajo
        if(self.validPoint(x-2,y-2) and self.grid[self.n*(x-2)+y-2]==self.grid[self.n*(x-1)+y-1] and self.grid[self.n*(x-1)+y-1]==self.symbol[player]):
            return True
        if(self.validPoint(x+1,y+1) and self.validPoint(x-1,y-1) and self.grid[self.n*(x+1)+y+1]==self.grid[self.n*(x-1)+y-1] and self.grid[self.n*(x+1)+y+1]==self.symbol[player]):
            return True
        
=======
    def winner(self, player, x, y):
        symbol = self.symbol[player]
        directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
        for dx, dy in directions:
            for shift in range(-2, 1):
                if all(self.valid_point(x + dx * (shift + i), y + dy * (shift + i)) and
                       self.grid[(x + dx * (shift + i)) * self.n + (y + dy * (shift + i))] == symbol
                       for i in range(3)):
                    return True
>>>>>>> 6735ad5f3a14e6d4f1e7bec2cd806b801a660335
        return False

    def get_state(self):
        return ''.join(self.grid)

    def minimax(self, player, alpha, beta, depth):
        if self.game_over():
            return depth * (-1 if player == self.player else 1)
        
        state = self.get_state()
        if state in self.dp:
            return self.dp[state]
        
        best_score = -self.INF if player == self.player else self.INF
        for i in range(self.n):
            for j in range(self.n):
<<<<<<< HEAD
                s+=self.grid[self.n*i+j]
        return s

    #Algoritmo minimax

    def mM(self,player,alpha,beta,depth):
        if(self.gameOver()):
            return depth*((-1)**(self.player!=player))
        x=self.INF*((-1)**(player==self.player))
        estado=self.getState()
        if(estado in self.dp):
            return self.dp[estado]
        for i in range(self.n):
            for j in range(self.n):
                if(self.grid[self.n*i+j]=='_'):
                    self.Mark(player,i,j)
                    if(self.winner(player,i,j)):
                        self.unMark(player,i,j)
                        self.dp[self.getState()]=(self.n**2+1)*((-1)**(self.player!=player))+depth*((-1)**(self.player==player))
                        return (self.n**2+1)*((-1)**(self.player!=player))+depth*((-1)**(self.player==player))
                    next=not player
                    val=self.mM(next,alpha,beta,depth+1)
                    self.unMark(player,i,j)
                    if(self.player==player):
                        x=max(x,val)
                        alpha=max(alpha,x)
                        if(beta<=alpha):
                            self.dp[self.getState()]=x
                            return x
=======
                if self.grid[i * self.n + j] == ' ':
                    self.mark(player, i, j)
                    if self.winner(player, i, j):
                        score = self.n ** 2 + 1 if player == self.player else -(self.n ** 2 + 1)
>>>>>>> 6735ad5f3a14e6d4f1e7bec2cd806b801a660335
                    else:
                        score = self.minimax(not player, alpha, beta, depth + 1)
                    self.unmark(i, j)
                    
                    if player == self.player:
                        best_score = max(best_score, score)
                        alpha = max(alpha, best_score)
                    else:
                        best_score = min(best_score, score)
                        beta = min(beta, best_score)
                    
                    if beta <= alpha:
                        self.dp[state] = best_score
                        return best_score
        
        self.dp[state] = best_score
        return best_score

<<<<<<< HEAD
    def bestMove(self):
        best=-1000
        coords=(0,0)
        for i in range(self.n):
            for j in range(self.n):
                if(self.grid[self.n*i+j]=='_'):
                    self.Mark(self.player,i,j)
                    if(self.winner(self.player,i,j)):
                        self.unMark(self.player,i,j)
                        return (i,j)
                    nxt=not self.player
                    self.dp={}
                    aux=self.mM(nxt,-self.INF,self.INF,0)
                    self.unMark(self.player,i,j)
                    if(aux>best):
                        best=aux
                        coords=(i,j) 
        return coords
                        
    def menu(self,n):
        game=MinimaxAgent()
        game.n=n
        jugador=int(input("Ingresa tu número de jugador\na)Jugador 1    b)Jugador 2\n"))-1
        if(jugador==0):
            game.player=1
        else:
            game.player=0
        while(True):
            if(jugador==0):
                game.show()
                x,y=input("Ingresa tus coordenadas en la forma x y: ").split()
                x=int(x)
                y=int(y)
                game.Mark(jugador,x,y)
                if(game.winner(jugador,x,y)):
                    game.show()
                    print("Felicidades!!! jugador")
                    return
                if(game.gameOver()):
                    print("Empate!!!")
                    return
                x,y=game.bestMove()
                game.Mark(game.player,x,y)
                if(game.winner(game.player,x,y)):
                    game.show()
                    print("Mala suerte!!! jugador")
                    return 
                if(game.gameOver()):
                    print("Empate!!!")
                    return
            else:
                x,y=game.bestMove()
                game.Mark(game.player,x,y)
                game.show()
                if(game.winner(game.player,x,y)):
                    print("Mala suerte!!! jugador")
                    return
                if(game.gameOver()):
                    print("Empate!!!")
                    return
                x,y=input("Ingresa tus coordenadas en la forma x y: ").split()
                x=int(x)
                y=int(y)
                game.Mark(jugador,x,y)
                if(game.winner(jugador,x,y)):
                    game.show()
                    print("Felicidades!!! jugador")
                    return
                if(game.gameOver()):
                    print("Empate!!!")
                    return
                     
             
=======
    def bestMove(self, real_board):
        best_score = -self.INF
        best_move = (0, 0)
        for i in range(self.n):
            for j in range(self.n):
                if self.grid[i * self.n + j] == ' ':
                    self.mark(self.player, i, j)
                    if self.winner(self.player, i, j):
                        self.unmark(i, j)
                        return (i, j)
                    
                    self.dp.clear()
                    score = self.minimax(not self.player, -self.INF, self.INF, 0)
                    self.unmark(i, j)
                    
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)
        
        move_index = best_move[0] * self.n + best_move[1]
        if real_board.board[move_index] == ' ':
            real_board.squares[move_index].clicked(
                real_board.squares[move_index].x, real_board.squares[move_index].y,
                'x', real_board, real_board.x_asset
            )
>>>>>>> 6735ad5f3a14e6d4f1e7bec2cd806b801a660335

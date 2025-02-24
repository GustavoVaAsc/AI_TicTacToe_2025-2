class Minimax:

    #Tamaño del grid

    n=4

    #Declaración del grid

    grid=[]

    #Declaración símbolo de jugador

    symbol=[]

    #Declaración del dp

    dp={}

    #Jugador 

    def __init__(self):
        for i in range(self.n):
            self.grid.append([])
            for j in range(self.n):
                self.grid[i].append('_')
        self.symbol.append('o')
        self.symbol.append('x')

    #Funcion para mostrar el grid

    def show(self):
        for i in range(self.n):
            for j in range(self.n):
                print(self.grid[i][j],end=" ")
            print()

    #Funcion para marcar una casilla del grid

    def Mark(self,player,x,y):
        self.grid[x][y]=self.symbol[player]
        
    
    #Función para desmarcar una casilla del grid

    def unMark(self,player,x,y):
        self.grid[x][y]='_'

    #Función para determinar que el juego no puede continuar

    def gameOver(self):
        for i in range(self.n):
            for j in range(self.n):
                if(self.grid[i][j]=='_'):
                    return False
        return True

    #Función para verificar si un jugador ya gano

    def validPoint(self,x,y):
        if(x>=0 and x<self.n and y>=0 and y<self.n):
            return True
        return False

    def winner(self,player,x,y):

        if(self.grid[x][y]!=self.symbol[player]):
            return False
        
        #Checar vertical hacia adelante
        if(self.validPoint(x+2,y) and self.grid[x+1][y]==self.grid[x+2][y] and self.grid[x+1][y]==self.symbol[player]):
            return True
        
        #Checar vertical en medio
        if(self.validPoint(x+1,y) and self.validPoint(x-1,y) and self.grid[x+1][y]==self.grid[x-1][y] and self.grid[x+1][y]==self.symbol[player]):
            return True

        #vertical izquierda
        if(self.validPoint(x-2,y) and self.grid[x-1][y]==self.grid[x-2][y] and self.grid[x-1][y]==self.symbol[player]):
            return True 
        
        #Horizontal hacia arriba
        if(self.validPoint(x,y+2) and self.grid[x][y+1]==self.grid[x][y+2] and self.grid[x][y+1]==self.symbol[player]):
            return True
        
        #Horizontal hacia abajo
        if(self.validPoint(x,y-2) and self.grid[x][y-1]==self.grid[x][y-2] and self.grid[x][y-1]==self.symbol[player]):
            return True
        
        #Horizontal en medio
        if(self.validPoint(x,y+1) and self.validPoint(x,y-1) and self.grid[x][y+1]==self.grid[x][y-1] and self.grid[x][y+1]==self.symbol[player]):
            return True
        
        #Digonal positiva hacia arriba
        if(self.validPoint(x-2,y+2) and self.grid[x-1][y+1]==self.grid[x-2][y+2] and self.grid[x-1][y+1]==self.symbol[player]):
            return True
        #Diagonal positiva hacia abajo
        if(self.validPoint(x+2,y-2) and self.grid[x+1][y-1]==self.grid[x+2][y-2] and self.grid[x+1][y-1]==self.symbol[player]):
            return True
        #Diagonal positiva en medio
        if(self.validPoint(x+1,y-1) and self.validPoint(x-1,y+1) and self.grid[x+1][y-1]==self.grid[x-1][y+1] and self.grid[x-1][y+1]==self.symbol[player]):
            return True
        #Diagonal negativa hacia arriba
        if(self.validPoint(x+2,y+2) and self.grid[x+1][y+1]==self.grid[x+2][y+2] and self.grid[x+1][y+1]==self.symbol[player]):
            return True
        #Diagonal negativa hacia abajo
        if(self.validPoint(x-2,y-2) and self.grid[x-2][y-2]==self.grid[x-1][y-1] and self.grid[x-1][y-1]==self.symbol[player]):
            return True
        if(self.validPoint(x+1,y+1) and self.validPoint(x-1,y-1) and self.grid[x+1][y+1]==self.grid[x-1][y-1] and self.grid[x+1][y+1]==self.symbol[player]):
            return True
        
        return False

    #Función para obtener el estado actual

    def getState(self,player):
        s=""
        for i in range(self.n):
            for j in range(self.n):
                s+=self.grid[i][j]
        return s

    #Algoritmo minimax

    def mM(self,player,depth):
        if(self.gameOver()):
            return depth*((-1)**(self.player!=player))
        x=1000*((-1)**(player==self.player))
        estado=self.getState(player)
        if(estado in self.dp):
            return self.dp[estado]
        for i in range(self.n):
            for j in range(self.n):
                if(self.grid[i][j]=='_'):
                    self.Mark(player,i,j)
                    if(self.winner(player,i,j)):
                        self.unMark(player,i,j)
                        self.dp[self.getState(player)]=(self.n**2+1)*((-1)**(self.player!=player))+depth*((-1)**self.player==player)
                        return (self.n**2+1)*((-1)**(self.player!=player))+depth*((-1)**self.player==player)
                    next=not player
                    if(self.player==player):
                        x=max(x,self.mM(next,depth+1))
                    else:
                        x=min(x,self.mM(next,depth+1))
                    self.unMark(player,i,j)
        self.dp[self.getState(player)]=x
        return x

    def bestMove(self):
        best=-1000
        coords=(0,0)
        for i in range(self.n):
            for j in range(self.n):
                if(self.grid[i][j]=='_'):
                    self.Mark(self.player,i,j)
                    if(self.winner(self.player,i,j)):
                        self.unMark(self.player,i,j)
                        return (i,j)
                    nxt=not self.player
                    self.dp={}
                    aux=self.mM(nxt,0)
                    self.unMark(self.player,i,j)
                    if(aux>best):
                        best=aux
                        coords=(i,j) 
        return coords
                        
    
def menu():
    game=Minimax()
    while(True):
        game.show()
        player=False
        game.player=not player
        opt=input("1.Jugada del jugador 1\n2.Jugada del jugador 2\n")
        if(opt=='1'):
            x,y=input("Ingresa las coordenadas con espacio de la casilla que quieres llenar: ").split()
            game.Mark(player,int(x),int(y))
            if(game.winner(player,int(x),int(y))):
                print("Felicidades jugador 1!!")
                return
            if(game.gameOver()):
                print("Empate!!!")
                return
        elif (opt=='2'):
            x,y=game.bestMove()
            game.Mark(game.player,x,y)
            if(game.winner(game.player,x,y)):
                print("Felicidades jugador 2!!")
                return
            if(game.gameOver()):
                print("Empate!!!")
                return
            
menu()
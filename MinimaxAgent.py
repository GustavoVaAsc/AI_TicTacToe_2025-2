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

    def Mark(self,player,x,y):
        self.grid[x*self.n+y]=self.symbol[player]
        
    
    #Función para desmarcar una casilla del grid

    def unMark(self,player,x,y):
        self.grid[x*self.n+y]='_'

    #Función para determinar que el juego no puede continuar

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
        
        return False

    #Función para obtener el estado actual

    def getState(self):
        s=""
        for i in range(self.n):
            for j in range(self.n):
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
                    else:
                        x=min(x,val)
                        beta=min(beta,x)
                        if(beta<=alpha):
                            self.dp[self.getState()]=x
                            return x
                    
        self.dp[self.getState()]=x
        return x

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
                     
             
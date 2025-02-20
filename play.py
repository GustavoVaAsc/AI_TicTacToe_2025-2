
class Minimax:

    #Tamaño del grid

    n=3

    #Declaración del grid

    grid=[]

    #Declaración de vectores de verificación

    rows=[]
    columns=[]
    Pdiag=[]
    Ndiag=[]


    #Jugador 

    def __init__(self):
        for i in range(self.n):
            self.grid.append([])
            for j in range(self.n):
                self.grid[i].append('_')
        for i in range(2):
            self.rows.append([])
            self.columns.append([])
            for j in range(self.n):
                self.rows[i].append(0)
                self.columns[i].append(0)

        for i in range(2):
            self.Pdiag.append([])
            self.Ndiag.append([])
            for j in range(2*self.n):
                self.Pdiag[i].append(0)
                self.Ndiag[i].append(0)

    #Funcion para mostrar el grid

    def show(self):
        for i in range(self.n):
            for j in range(self.n):
                print(self.grid[i][j],end=" ")
            print()

    #Funcion para marcar una casilla del grid

    def Mark(self,player,x,y):
        self.rows[player][x]+=1
        self.columns[player][y]+=1
        self.Pdiag[player][x-y+self.n-1]+=1
        self.Ndiag[player][x+y]+=1
        if(player):
            self.grid[x][y]='x'
        else:
            self.grid[x][y]='o'
    
    #Función para desmarcar una casilla del grid

    def unMark(self,player,x,y):
        self.rows[player][x]-=1
        self.columns[player][y]-=1
        self.Pdiag[player][x-y+self.n-1]-=1
        self.Ndiag[player][x+y]-=1
        self.grid[x][y]='_'

    #Función para determinar que el juego no puede continuar

    def gameOver(self):
        for i in range(self.n):
            for j in range(self.n):
                if(self.grid[i][j]=='_'):
                    return False
        return True

    #Función para verificar si un jugador ya gano

    def winner(self,player):
        for i in range(self.n):
            if(self.rows[player][i]==3 or self.columns[player][i]==3):
                return True 
        for i in range(2*self.n):
            if(self.Pdiag[player][i]==3 or self.Ndiag[player][i]==3):
                return True
        return False


    #Algoritmo minimax

    def mM(self,player,depth):
        if(self.gameOver()):
            return (-1)**(player)*depth
        x=1000*((-1)**(player+1))
        for i in range(self.n):
            for j in range(self.n):
                if(self.grid[i][j]=='_'):
                    self.Mark(player,i,j)
                    if(self.winner(player)):
                        self.unMark(player,i,j)
                        return (2*(self.n**2+1))*((-1)**player)-((-1)**(player+1))*depth
                    next=not player
                    if(not player):
                        x=max(x,self.mM(next,depth+1))
                    else:
                        x=min(x,self.mM(next,depth+1))
                    self.unMark(player,i,j)
        return x

    def bestMove(self,player):
        best=1000*((-1)**(player+1))
        coords=(0,0)
        for i in range(self.n):
            for j in range(self.n):
                if(self.grid[i][j]=='_'):
                    self.Mark(player,i,j)
                    nxt=not player
                    aux=self.mM(nxt,0)
                    self.unMark(player,i,j)
                    if(not player):
                        if(aux>best):
                            best=aux
                            coords=(i,j)
                    else:
                        if(aux<best):
                            best=aux
                            coords=(i,j)
                    
        return coords
                        


    
def menu():
    game=Minimax()
    game.player=True
    while(True):
        game.show()
        opt=input("1.Jugada del jugador 1\n2.Jugada del jugador 2\n")
        if(opt=='1'):
            x,y=input("Ingresa las coordenadas con espacio de la casilla que quieres llenar: ").split()
            game.Mark(1,int(x),int(y))
            if(game.winner(1)):
                print("Felicidades jugador 1!!")
                return
            if(game.gameOver()):
                print("Empate!!!")
                return
        elif (opt=='2'):
            x,y=game.bestMove(0)
            game.Mark(0,x,y)
            if(game.winner(0)):
                print("Felicidades jugador 2!!")
                return
            if(game.gameOver()):
                print("Empate!!!")
                return
            
menu()
        

            
   


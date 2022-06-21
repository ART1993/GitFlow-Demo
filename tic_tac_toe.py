import random
def display_board(board):
    """
        En esta función se genera la tabla que se mostrará al jugador
        los movimientos realizados a lo largo de la partida
    """
    table=""
    #funcion para pintar el tablero
    #la usaré al principio y dada vez que se realize un cambio
    for i in range(3):
        table=table +"  "+ board[i][0] +" | "+board[i][1]+" | "+board[i][2]+   "\n"
        if i==2:
            break
        table=table + "----+---+-----\n"
    return print(table)


def enter_move(board):
    """ 
    En esta función vamos a pedir al jugador que 
    realize un movimiento. Cada movimiento hará que 
    un contador aumente su valor, esto será así 
    hasta llegar a 9 o bien que uno de los 
    jugadores gane.
    """
    print("Es el turno del jugador.",end="")
    position=make_list_of_free_fields(board)
    print("\tfila columna")
    for pos in position:
        print("Las posiciones disponibles son:",pos[0],pos[1],sep="\t")
    i,j=input("introduce dos números que desees introducir entre 0 y 2\n").split()
    i,j=int(i),int(j)
    while ([i,j] not in position):
        i,j=input("valor fuera de las casillas, vuelve a introducirlos\n").split()
        i,j=int(i),int(j)
    board[i][j]="X"
    return board
    #funcion para que el usario introduzca su movimiento

def make_list_of_free_fields(board):
    """ 
    El objetivo es que lea una lista que se dé de entrada
    para luego leer los espacios libres que se pueden usar
    de este modo el ordenador y el jugador solo podran
    elegir un número determinado de valores sin tener que crear 
    condiciones de contorno.
    Tenemos que decidir que devolverá la función, en este caso 
    deberá de ser una lista de números que el jugador o 
    la máquina pueden usar como movimiento
    """

    m_lista=[]
    i=0
    for i in range(0,3):
        for j in range(0,3):
            if board[i][j]==" ":
                #Movimientos disponibles
                m_lista.append([i,j])
    #print(n_lista)
    #break
    return m_lista
    #funcion para comprobar espacios libres

def victory_for(board, sign=True):
    """Debemos de buscar las condiciones de victoria para cada
       jugador, suponoendo que a cada jugador le asignamos 
       un simbolo (X=Jugador y O=Máquina) entonces podemos poner las condicio-
       nes de vistoria relacionados con estos valores"""
    lista=make_list_of_free_fields(board)
    if  ((board[1][0]==board[1][1]==board[1][2]=="O") or 
         (board[0][1]==board[1][1]==board[2][1]=="O") or
         (board[0][0]==board[1][1]==board[2][2]=="O") or
         (board[0][0]==board[0][1]==board[0][2]=="O") or
         (board[0][2]==board[1][2]==board[2][2]=="O") or
         (board[0][0]==board[1][0]==board[2][0]=="O") or
         (board[0][2]==board[1][1]==board[2][0]=="O") or
         (board[2][0]==board[2][1]==board[2][2]=="O")):
        print("Gana la máquina")
        display_board(board)
        return sign
    elif((board[1][0]==board[1][1]==board[1][2]=="X") or 
         (board[0][1]==board[1][1]==board[2][1]=="X") or
         (board[0][0]==board[1][1]==board[2][2]=="X") or
         (board[0][0]==board[0][1]==board[0][2]=="X") or
         (board[0][2]==board[1][2]==board[2][2]=="X") or
         (board[0][0]==board[1][0]==board[2][0]=="X") or
         (board[0][2]==board[1][1]==board[2][0]=="X") or
         (board[2][0]==board[2][1]==board[2][2]=="X")):
        print("Gana el jugador")
        display_board(board)
        return sign
    elif(len(lista)==0):
        print("empate")
        display_board(board)
        return sign
    else:
    #funcion para comprobar quien gana, debe devolver un true o false
        return False
def draw_move(board):
    """Creación de los movimientos de la máquina
       Esta función solo dibujará un O por turno.
       El programa leera la lista de puntos libres a la hora de seleccionar puntos
       En caso de que ninguna de las condiciones puesta se cumpla, simplemente
       elegirá un punto al azar de los que disponga.
    """
    positions=make_list_of_free_fields(board)
    positions_square=[]
    for i in[0,2]:
        for j in [0,2]:
            if [i,j] in positions:
                positions_square.append([i,j])
    o="O"
    #Condiciones para elegir la victoria
    if  ([1,1] in positions):
        board[1][1]=o
    elif(((board[1][1]==board[0][0]=="O") or 
          (board[2][0]==board[2][1]=="O") or
          (board[0][2]==board[1][2]=="O")) and 
          [2,2] in positions):
        board[2][2]=o
    elif(((board[2][2]==board[0][2]=="O") or 
          (board[1][0]==board[1][1]=="O")) and 
          [1,2] in positions):
        board[1][2]=o
    elif(((board[1][1]==board[2][0]=="O") or 
          (board[0][0]==board[0][1]=="O") or
          (board[2][2]==board[1][2]=="O")) and 
          [0,2] in positions):
        board[0][2]=o
    elif((board[1][1]==board[0][2]=="O" or 
          board[0][0]==board[1][0]=="O" or
          board[2][2]==board[2][1]=="O") and 
          [2,0] in positions):
        board[2][0]=o
    elif((board[1][1]==board[0][1]=="O" or 
         board[2][0]==board[2][2]=="O") and 
         ([2,1] in positions)):
        board[2][1]=o
    elif((board[1][1]==board[2][1]=="O" or 
          board[0][0]==board[0][2]=="O") and 
          [0,1] in positions):
        board[0][1]=o
    elif((board[1][1]==board[1][2]=="O" or 
          board[0][0]==board[2][0]=="O") and 
          [1,0] in positions):
        board[1][0]=o
    elif(((board[1][0]==board[2][0]=="O") or 
         (board[1][1]==board[2][2]=="O") or 
         (board[0][1]==board[0][2]=="O")) and 
         [0,0] in positions):
        board[0][0]=o
    #Condiciones para evitar la derrota
    elif(((board[1][1]==board[0][0]=="X") or 
          (board[2][0]==board[2][1]=="X") or
          (board[0][2]==board[1][2]=="X")) and 
          [2,2] in positions):
        board[2][2]=o
    elif(((board[2][2]==board[0][2]=="X") or 
          (board[1][0]==board[1][1]=="X")) and 
          [1,2] in positions):
        board[1][2]=o
    elif((board[1][1]==board[2][0]=="X" or 
          board[0][0]==board[0][1]=="X" or
          board[2][2]==board[1][2]=="X") and 
          [0,2] in positions):
        board[0][2]=o
    elif((board[1][1]==board[0][2]=="X" or 
          board[0][0]==board[1][0]=="X" or
          board[2][2]==board[2][1]=="X") and 
          [2,0] in positions):
        board[2][0]=o
    elif((board[1][1]==board[0][1]=="X" or 
         board[2][0]==board[2][2]=="X") and 
         ([2,1] in positions)):
        board[2][1]=o
    elif((board[1][1]==board[2][1]=="X" or 
          board[0][0]==board[0][2]=="X") and 
          [0,1] in positions):
        board[0][1]=o
    elif((board[1][1]==board[1][2]=="X" or 
          board[0][0]==board[2][0]=="X") and 
          [1,0] in positions):
        board[1][0]=o
    elif(((board[1][0]==board[2][0]=="X") or 
         (board[1][1]==board[2][2]=="X") or 
         (board[0][1]==board[0][2]=="X")) and 
         [0,0] in positions):
        board[0][0]=o  
    #Tácticas que se me ocurren para que la máquina obtenga la victoria
    elif(len(positions_square)>=3):
        list_neigh=[[1,0],[0,1],[2,1],[1,2]]
        for vals in list_neigh:
            count=0
            if (board[vals[0]][vals[1]]=="X"):
                if [vals[0]+1,vals[1]] in positions_square:
                    positions_square.remove([vals[0]+1,vals[1]])
                    count+=1
                if [vals[0]-1,vals[1]] in positions_square:
                    positions_square.remove([vals[0]-1,vals[1]])
                    count+=1
                if [vals[0],vals[1]+1] in positions_square:
                    positions_square.remove([vals[0],vals[1]+1])
                    count+=1
                if [vals[0],vals[1]-1] in positions_square:
                    positions_square.remove([vals[0],vals[1]-1])
                    count+=1
                if count==2:
                    break
        if board[0][0] =="X":
            positions_square.remove([2,2])
        elif board[0][2] =="X":
            positions_square.remove([2,0])
        elif board[0][0] =="X":
            positions_square.remove([0,2])
        elif board[2][2] =="X":
            positions_square.remove([0,0])
        positions_square_random=random.choice(positions_square)
        ins1,ins2=positions_square_random[0],positions_square_random[1]
        board[ins1][ins2]=o
    #En caso de que ninguno de los casos anteriores se cumpla se coge un punto al azar
    #Entre los existentes
    else:
        position=random.choice(positions)
        ins1,ins2=position[0],position[1]
        board[ins1][ins2]=o
    #TODO funcion para pintar el movimiento de la maquina
    return board



def jugar():
    """
    Función donde tiene lugar la partida.
    En la primera parte se inicia el tablero vacio.
    Fuera de la función, se realizará un bucle donde tendrá lugar la partida.
    """
    tablero = [[" " for c in range(3)] for d in range(3)]
    print("Vamos a jugar al 3 en raya!!!")
    print("El jugador usará X. La máquina O")
    return tablero
    #TODO inicializacion del juego

tablero=jugar()
s=random.randint(1,2)
print(s)
if (s==1):
#El primer turno lo tendrá el ordenador
    t=0
else:
#El primer turno lo tendrá el jugador
    t=1
for _ in range(0,9):
    if t%2==0:
        draw_move(tablero)
    elif t%2!=0:
        enter_move(tablero)
    if(victory_for(tablero)):
        break
    display_board(tablero)
    print("\n")
    print(t,"\n")
    t=t+1

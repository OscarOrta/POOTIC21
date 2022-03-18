class Sokoban:
  """
  Definimos los componentes
  0-cajas
  1-paredes
  2-muñeco
  3-caminos
  4-metas
  """
  posicion_columna = 4 #columna inicial del muñeco 
  mapa = [1,3,3,3,2,3,3,3,1] #mapa inicial del juego
  
  def __init__(self): #metodo para inicializar el objeto
    pass #inicializacion del juego

  def imprimirMapa(self): #metodo impresion del map
    for i in self.mapa: #Recorre cada posición del mapa 
      if i == 3: #Si el elemento es un 3 (camino)
        print(" ", end ="") #imprime " " y no da salto de linea
      elif i==2: #Si el elemento es un 2 (muñeco)
        print(chr(64),end ="") #imprime " " y no da salto de linea
      elif i==1: #Si el elemento es 1 (pared)
        print("|",end ="") #imprime "|" y no da salto de linea
      else: #De lo contrario
        print(i, end = "") # Imprime el elemento encontrado
    print() #imprime una linea en blanco

  def moverDerecha(self): #metodo para mover el personaje a la derecha
    self.posicion_columna += 1 #Actualiza la posicion un lugar derecha
    self.mapa[self.posicion_columna]= 2 #Coloca el muñeco en la nueva posicion
    self.mapa[self.posicion_columna - 1] = 3 #Coloca un espacio donde estaba el muñeco
    self.imprimirMapa() #Imprimir el mapa actualizado
    
  def moverIzquierda(self): #metodo para mover el personaje a la izquierda
    self.posicion_columna -= 1 #Actualiza la posicion un lugar izquierda
    self.mapa[self.posicion_columna]= 2 #Coloca el muñeco en la nueva posicion
    self.mapa[self.posicion_columna + 1] = 3 #Coloca un espacio donde estaba el muñeco
    self.imprimirMapa() #Imprimir el mapa actualizado

juego = Sokoban() #Crea un objeto del juego sokoban
juego.imprimirMapa() #Imprime el mapa

instrucciones = "q Salir\nd Derecha\na Izquierda" #Variable con las instrucciones del juego

while True: #Bucle infinito
  print(instrucciones) #Imprime las instrucciones
  movimiento=input("Mover: ") #lee hacia donde se mueve el muñeco
  if movimiento == "d": #si el movimiento es igual a "d"
    juego.moverDerecha() #Llama al metodo mover a la derecha
  elif movimiento == "a": #si el movimiento es igual a "a"
    juego.moverIzquierda() #Llama al metodo mover a la izquierda
  elif movimiento == "q": #si el movimiento es igual a "q"
    print("Saliste del juego") #Mensaje de salida 
    break
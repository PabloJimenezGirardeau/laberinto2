''' e aquí un programa que mermite moverse a través de un pequeño laberinto hasta
llegar a la salida del mismo'''


# Coordenadas del muro
muro = ((0, 1), (0, 2), (0, 3), (0, 4), (1, 1), (2, 1), (2, 3), (3, 3), (4, 0), (4, 1), (4, 2), (4, 3))

#creo una clase llamada laberinto y sus propiedades
class Laberinto:
    def __init__(self, muro):
        filas = 5
        columnas = 5
        self.laberinto = [[' ' for _ in range(columnas)] for _ in range(filas)]
        self.posicion_actual = (filas - 5, columnas - 5)
        self.destino = (filas - 1, columnas - 1)
        self.recorrido = []  # Inicializar recorrido
        self.inicializar_laberinto(muro)


#esta funcion llena la matriz del laberinto con los muros y establece la posición inicial y el destino.
    def inicializar_laberinto(self, muro):
        for coordenada in muro:
            fila, columna = coordenada
            self.laberinto[fila][columna] = 'X'
        self.laberinto[self.posicion_actual[0]][self.posicion_actual[1]] = '.'
        self.laberinto[self.destino[0]][self.destino[1]] = 'S'

    def mostrar_laberinto(self):
        for fila in self.laberinto:
            print('  '.join(fila))
        print()

# la funcion moverse usa las letras 'wasd' para moverse en el laberinto
    def moverse(self, direccion):
        fila, columna = self.posicion_actual

        if direccion == 'w' and fila > 0 and self.laberinto[fila - 1][columna] != 'X':
            fila -= 1

        elif direccion == 's' and fila < len(self.laberinto) - 1 and self.laberinto[fila + 1][columna] != 'X':
            fila += 1

        elif direccion == 'a' and columna > 0 and self.laberinto[fila][columna - 1] != 'X':
            columna -= 1

        elif direccion == 'd' and columna < len(self.laberinto[0]) - 1 and self.laberinto[fila][columna + 1] != 'X':
            columna += 1

        self.laberinto[self.posicion_actual[0]][self.posicion_actual[1]] = ' '
        self.posicion_actual = (fila, columna)
        self.laberinto[fila][columna] = '.'
        self.mostrar_laberinto()
        self.recorrido.append(direccion)

        if self.posicion_actual == self.destino:
            print("¡Felicidades, has completado el laberinto!")

# crear una instancia de Laberinto
lab = Laberinto(muro)

# mostrar el laberinto inicial
lab.mostrar_laberinto()

# para moverse por el laberinto hasta completarlo
while lab.posicion_actual != lab.destino:
    direccion = input("Ingresa la dirección: arriba(w), abajo(s), izquierda(a), derecha(d): ").lower()
    lab.moverse(direccion)

print("Recorrido realizado:", lab.recorrido) 

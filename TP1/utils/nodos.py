
class Nodo:
    def __init__(self, estado, padre, movimiento, profundidad):
        self.estado = estado  # posicion actual
        self.padre = padre  # nodo padre
        self.movimiento = movimiento  # moviento para llegar a este nodo desde el padre
        self.profundidad = profundidad  # profundidad en el arbol

    def mover(self, direccion):
        estado = list(self.estado)
        ind = estado.index(0)

        if direccion == "arriba":
            if ind not in [6, 7, 8]:
                temp = estado[ind + 3]
                estado[ind + 3] = estado[ind]
                estado[ind] = temp
                return tuple(estado)
            else:
                return None
        elif direccion == "abajo":
            if ind not in [0, 1, 2]:
                temp = estado[ind - 3]
                estado[ind - 3] = estado[ind]
                estado[ind] = temp
                return tuple(estado)
            else:
                return None
        elif direccion == "izquierda":
            if ind not in [2, 5, 8]:
                temp = estado[ind + 1]
                estado[ind + 1] = estado[ind]
                estado[ind] = temp
                return tuple(estado)
            else:
                return None
        elif direccion == "derecha":
            if ind not in [0, 3, 6]:
                temp = estado[ind - 1]
                estado[ind - 1] = estado[ind]
                estado[ind] = temp
                return tuple(estado)
            else:
                return None

    def encontrar_sucesores(self):
        sucesores = []
        sucesorN = self.mover("arriba")
        sucesorS = self.mover("abajo")
        sucesorE = self.mover("derecha")
        sucesorO = self.mover("izquierda")

        # Encuentra los sucesores
        sucesores.append(Nodo(sucesorN, self, "arriba", self.profundidad + 1))
        sucesores.append(Nodo(sucesorS, self, "abajo", self.profundidad + 1))
        sucesores.append(Nodo(sucesorE, self, "derecha", self.profundidad + 1))
        sucesores.append(Nodo(sucesorO, self, "izquierda", self.profundidad + 1))

        sucesores = [nodo for nodo in sucesores if nodo.estado is not None]
        return sucesores

    def encontrar_camino(self, inicio):
        camino = []
        nodo_actual = self
        # print("La profundidad de la solucion es: " + nodo_actual.profundidad)  # profundidad
        while nodo_actual.profundidad >= 1:
            camino.append(nodo_actual)
            nodo_actual = nodo_actual.padre
        camino.reverse()
        print("Camino de resolucion")
        for elem in camino:
            elem.imprimir()
            print("\n")
        return camino

    def imprimir(self):
        fila = 0
        for pieza in self.estado:
            if pieza == 0:
                print(" ", end=" ")
            else:
                print(pieza, end=" ")
            fila += 1
            if fila == 3:
                print()
                fila = 0
        print("\n")


# clase que define nodo con heuristica
class NodoH(Nodo):
    def __init__(self, estado, padre, movimiento, profundidad, heuristica):
        super().__init__(estado, padre, movimiento, profundidad)
        self.heuristica = heuristica
        # self.valorH = self.heuristica(self.estado)  # calcula el valor segun la funcion heuristica

    def encontrar_sucesores(self):
        sucesores = []
        sucesorN = self.mover("arriba")
        sucesorS = self.mover("abajo")
        sucesorE = self.mover("derecha")
        sucesorO = self.mover("izquierda")

        sucesores.append(NodoH(sucesorN, self, "arriba", self.profundidad + 1, heuristicas.hamming_distance(sucesorN)))
        sucesores.append(NodoH(sucesorS, self, "abajo", self.profundidad + 1, heuristicas.hamming_distance(sucesorS)))
        sucesores.append(NodoH(sucesorE, self, "derecha", self.profundidad + 1, heuristicas.hamming_distance(sucesorE)))
        sucesores.append(NodoH(sucesorO, self, "izquierda", self.profundidad + 1, heuristicas.hamming_distance(sucesorO)))

        sucesores = [nodo for nodo in sucesores if nodo.estado is not None]
        return sucesores

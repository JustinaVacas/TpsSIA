from TP1.utiles import heuristicas
from colorama import Fore, Back, Style

# unicode for draw puzzle in command promt or terminal
left_down_angle = '\u2514'
right_down_angle = '\u2518'
right_up_angle = '\u2510'
left_up_angle = '\u250C'

middle_junction = '\u253C'
top_junction = '\u252C'
bottom_junction = '\u2534'
right_junction = '\u2524'
left_junction = '\u251C'

# bar color
bar = Style.BRIGHT + Fore.CYAN + '\u2502' + Fore.RESET + Style.RESET_ALL
dash = '\u2500'

# Line draw code
first_line = Style.BRIGHT + Fore.CYAN + left_up_angle + dash + dash + dash + top_junction + dash + dash + dash + top_junction + dash + dash + dash + right_up_angle + Fore.RESET + Style.RESET_ALL
middle_line = Style.BRIGHT + Fore.CYAN + left_junction + dash + dash + dash + middle_junction + dash + dash + dash + middle_junction + dash + dash + dash + right_junction + Fore.RESET + Style.RESET_ALL
last_line = Style.BRIGHT + Fore.CYAN + left_down_angle + dash + dash + dash + bottom_junction + dash + dash + dash + bottom_junction + dash + dash + dash + right_down_angle + Fore.RESET + Style.RESET_ALL


class Nodo:
    def __init__(self, estado, padre, movimiento, profundidad):
        self.estado = estado  # posicion actual
        self.padre = padre  # nodo padre
        self.movimiento = movimiento  # moviento para llegar a este nodo desde el padre
        self.profundidad = profundidad  # profundidad en el arbol (asumimos que es el costo)

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
        while nodo_actual.profundidad >= 1:
            camino.append(nodo_actual)
            nodo_actual = nodo_actual.padre
        camino.append(nodo_actual)
        camino.reverse()
        print("Camino de resolucion:")
        for elem in camino:
            elem.imprimir()
            print("\n")
        return camino

    def imprimir(self):
        print(first_line)
        fila = 0
        i = 0
        for pieza in self.estado:
            if pieza == 0:
                print(bar, Back.RED + ' ' + Back.RESET, end=' ')
            else:
                print(bar, pieza, end=' ')
            i += 1
            if i == 3:
                print(bar)
                fila += 1
                i = 0
                if fila == 3:
                    print(last_line)
                else:
                    print(middle_line)
        print("\n")


# clase que define nodo con heuristica
class NodoH(Nodo):
    def __init__(self, estado, padre, movimiento, profundidad, heuristica, valor_heuristica):
        super().__init__(estado, padre, movimiento, profundidad)
        self.valor_heuristica = valor_heuristica
        self.heuristica = heuristica

    def encontrar_sucesores(self):
        sucesores = []
        sucesorN = self.mover("arriba")
        sucesorS = self.mover("abajo")
        sucesorE = self.mover("derecha")
        sucesorO = self.mover("izquierda")

        if self.heuristica == 'H':
            sucesores.append(NodoH(sucesorN, self, "arriba", self.profundidad + 1, self.heuristica, heuristicas.hamming_distance(sucesorN)))
            sucesores.append(NodoH(sucesorS, self, "abajo", self.profundidad + 1, self.heuristica, heuristicas.hamming_distance(sucesorS)))
            sucesores.append(NodoH(sucesorE, self, "derecha", self.profundidad + 1, self.heuristica, heuristicas.hamming_distance(sucesorE)))
            sucesores.append(NodoH(sucesorO, self, "izquierda", self.profundidad + 1, self.heuristica, heuristicas.hamming_distance(sucesorO)))

        elif self.heuristica == 'M':
            sucesores.append(NodoH(sucesorN, self, "arriba", self.profundidad + 1, self.heuristica, heuristicas.manhattan_distance(sucesorN)))
            sucesores.append(NodoH(sucesorS, self, "abajo", self.profundidad + 1, self.heuristica, heuristicas.manhattan_distance(sucesorS)))
            sucesores.append(NodoH(sucesorE, self, "derecha", self.profundidad + 1, self.heuristica, heuristicas.manhattan_distance(sucesorE)))
            sucesores.append(NodoH(sucesorO, self, "izquierda", self.profundidad + 1, self.heuristica, heuristicas.manhattan_distance(sucesorO)))

        elif self.heuristica == 'NA':
            sucesores.append(NodoH(sucesorN, self, "arriba", self.profundidad + 1, self.heuristica, heuristicas.noadmisible(sucesorN)))
            sucesores.append(NodoH(sucesorS, self, "abajo", self.profundidad + 1, self.heuristica, heuristicas.noadmisible(sucesorS)))
            sucesores.append(NodoH(sucesorE, self, "derecha", self.profundidad + 1, self.heuristica, heuristicas.noadmisible(sucesorE)))
            sucesores.append(NodoH(sucesorO, self, "izquierda", self.profundidad + 1, self.heuristica, heuristicas.noadmisible(sucesorO)))

        sucesores = [nodo for nodo in sucesores if nodo.estado is not None]
        return sucesores

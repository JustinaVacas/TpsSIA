from collections import deque


# clase que define el nodo
class Nodo:
    def __init__(self, estado, padre, movimiento, profundidad):
        self.estado = estado  # posicion actual
        self.padre = padre  # nodo padre
        self.movimiento = movimiento  # moviento para llegar a este nodo desde el padre
        self.profundidad = profundidad  # profundidad en el arbol

        def mover():
            estado = list

        def encontrar_sucesores():
            sucesores = []
            sucesorN = self.mover("arriba")
            sucesorS = self.mover("abajo")
            sucesorE = self.mover("derecha")
            sucesorO = self.mover("izquierda")

            sucesores.append(Nodo(sucesorN, self, "arriba", self.profundidad + 1))
            sucesores.append(Nodo(sucesorS, self, "abajo", self.profundidad + 1))
            sucesores.append(Nodo(sucesorE, self, "derecha", self.profundidad + 1))
            sucesores.append(Nodo(sucesorO, self, "izquierda", self.profundidad + 1))

            sucesores = [nodo for nodo in sucesores if nodo.estado is not None]
            return sucesores

        def encontrar_camino(self, inicio):
            camino = []
            nodo_actual = self
            while nodo_actual.profundida >= 1:
                camino.append(nodo_actual)
                nodo_actual = nodo_actual.padre
            camino.reverse()
            return camino


def bpa(inicio, objetivo):
    explorados = set()  # conjunto de nodos explorados
    frontera = deque()  # nodos sin expandir
    frontera.append(Nodo(inicio, None, None, 0))
    while frontera:
        nodo = frontera.popleft()
        if nodo.estado not in explorados:
            explorados.add(nodo.estado)
            print("\n", explorados)
        else:
            continue
        if nodo.estado == objetivo:
            print("\n Llego al objetivo")
            return nodo.encontrar_camino(inicio)
        else:
            frontera.extend(nodo.encontrar_sucesores())


def bpp(inicio, objetivo):
    explorados = set()  # conjunto de nodos explorados
    frontera = deque()  # nodos sin expandir
    frontera.append(Nodo(inicio, None, None, 0))
    while frontera:
        nodo = frontera.pop()
        if nodo.estado not in explorados:
            explorados.add(nodo.estado)
            print("\n", explorados)
        else:
            continue
        if nodo.estado == objetivo:
            print("\n Llego al objetivo")
            return nodo.encontrar_camino(inicio)
        else:
            frontera.extend(nodo.encontrar_sucesores())


def bppv(inicio, objetivo, limite):
    explorados = set()
    frontera = deque()
    frontera.append(Nodo(inicio, None, None, 0))
    while frontera:
        nodo = frontera.pop()
        if nodo.estado not in explorados:
            explorados.add(nodo.estado)
            print("\n", explorados)
        else:
            continue
        if nodo.estado == objetivo:
            print("\n Llego al objetivo")
            return nodo.encontrar_camino(inicio)
        else:
            frontera.extend(nodo.encontrar_sucesores())


def printPuzzle(fin):
    print("___")
    print(' '.join(fin.estado[0:3]))
    print(' '.join(fin.estado[3:6]))
    print(' '.join(fin.estado[6:9]))
    print('')

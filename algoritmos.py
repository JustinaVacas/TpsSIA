from collections import deque
import time


# clase que define el nodo
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


# bfs
def bpa(inicio, objetivo):
    print("bpa")
    explorados = set()  # conjunto de nodos explorados
    frontera = deque()  # nodos sin expandir
    frontera.append(Nodo(inicio, None, None, 0))
    while frontera:
        nodo = frontera.popleft()
        if nodo.estado not in explorados:
            explorados.add(nodo.estado)  # cantidad de nodos explorados len(explorados)
            nodo.imprimir()
            print("\n")
            # print("\n", explorados)
        else:
            continue
        if nodo.estado == objetivo:
            print("\n Llego al objetivo!")  # resultado de la busqueda exito
            print("Cantidad de nodos expandidos: ", len(explorados))
            print("Profundidad: ", nodo.profundidad)
            return nodo.encontrar_camino(inicio)
        else:
            frontera.extend(nodo.encontrar_sucesores())
    print("\n No llego al objetivo")  # resultado de la busqueda fracaso


# dfs hacer clase
def bpp(inicio, objetivo):
    explorados = set()
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
            print("\n Llego al objetivo!")
            print("Cantidad de nodos expandidos: ", len(explorados))
            print("Profundidad: ", nodo.profundidad)
            return nodo.encontrar_camino(inicio)
        else:
            frontera.extend(nodo.encontrar_sucesores())


def bppv(inicio, objetivo, profundidad):
    explorados = set()
    faltantes = set()
    expandir = set()
    frontera = deque()  # nodos sin expandir
    frontera.append(Nodo(inicio, None, None, 0))
    prof = 0
    nodo_inicial = Nodo(inicio, None, None, 0)
    while frontera and prof <= profundidad:
        print("profundidad actual: ", prof)
        nodo = frontera.pop()

        print("nodo")
        nodo.imprimir()
        print("nodo")

        print("agregando a faltantes")
        while len(frontera) != 0:
            aux = frontera.pop()
            if aux.estado != nodo_inicial.estado:
                faltantes.add(aux)
                aux.imprimir()
        print("agregando a faltantes")

        if nodo not in explorados:
            explorados.add(nodo)
            prof = prof + 1
        else:
            continue
        for nodos in faltantes:
            if nodos not in explorados:
                explorados.add(nodos)
                expandir.add(nodos)
        if nodo.estado == objetivo:
            print("\n Llego al objetivo!")
            print("Cantidad de nodos expandidos: ", len(explorados))
            print("Profundidad: ", nodo.profundidad)
            return nodo.encontrar_camino(inicio)
        else:
            print("nodos a expandir")
            print("------")
            nodo.imprimir()
            frontera.extend(nodo.encontrar_sucesores())
            for nodos in expandir:
                frontera.extend(nodos.encontrar_sucesores())
                nodos.imprimir()
            print("------")
            expandir.clear()

        for elem in explorados:
            elem.imprimir()
        # if prof == profundidad:
        #     time.sleep(0.1)
        #     profundidad = profundidad + 1
        #     print("Aumento del limite de profundidad\n")
        #     print("Profundidad: ", profundidad)
        #     print("\n")


def main():
    estado_objetivo = (1, 2, 3, 4, 5, 6, 7, 8, 0)
    estado_inicial = (0, 1, 3, 4, 2, 5, 7, 8, 6)
    print("Estado inicial:")
    Nodo(estado_inicial, None, None, 0).imprimir()
    print("----------------")
    bpa(estado_inicial, estado_objetivo)
    # bpp(estado_inicial, estado_objetivo)
    # bppv(estado_inicial, estado_objetivo, 2)
    print("----------------")
    print("Estado final:")
    Nodo(estado_objetivo, None, None, 0).imprimir()


if __name__ == '__main__':
    main()

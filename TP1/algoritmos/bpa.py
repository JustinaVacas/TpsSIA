from collections import deque

from TP1.utiles.nodos import Nodo


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

from TP1.utiles.nodos import Nodo
from collections import deque
import time


def bpp(inicio, objetivo):

    explorados = set()
    frontera = deque()
    frontera.append(Nodo(inicio, None, None, 0))  # nodos sin expandir
    start_time = time.process_time()

    while frontera:
        nodo = frontera.pop()
        if nodo.estado not in explorados:
            explorados.add(nodo.estado)
        else:
            continue
        if nodo.estado == objetivo:
            end_time = time.process_time()
            print("Llegó al objetivo!")
            print("Cantidad de nodos expandidos: ", len(explorados))
            print("Cantidad de nodos frontera: ", len(frontera))
            print("Profundidad: ", nodo.profundidad)
            print('Costo: ', nodo.profundidad)
            print('Tiempo de búsqueda: ', end_time-start_time)
            return nodo.encontrar_camino(inicio)

        for n in nodo.encontrar_sucesores():
            if n.estado not in explorados:
                frontera.append(n)

    end_time = time.process_time()
    print("No llegó al objetivo")  # resultado de la busqueda fracaso
    print("Cantidad de nodos expandidos: ", len(explorados))
    print("Cantidad de nodos frontera: ", len(frontera))
    print('Tiempo de búsqueda: ', end_time - start_time)

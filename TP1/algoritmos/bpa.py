from collections import deque
from TP1.utiles.nodos import Nodo
import time


def bpa(inicio, objetivo):

    explorados = set()  # conjunto de nodos explorados
    frontera = deque()  # conjunto de nodos frontera

    frontera.append(Nodo(inicio, None, None, 0))
    start_time = time.process_time()

    while frontera:
        nodo = frontera.popleft()
        if nodo.estado not in explorados:
            explorados.add(nodo.estado)  # cantidad de nodos explorados len(explorados)
        else:
            continue
        if nodo.estado == objetivo:
            end_time = time.process_time()
            print("Llegó al objetivo!")  # resultado de la busqueda exito
            print("Cantidad de nodos expandidos: ", len(explorados))
            print("Cantidad de nodos frontera: ", len(frontera))
            print("Profundidad: ", nodo.profundidad)
            print('Costo: ', nodo.profundidad)
            print('Tiempo de búsqueda: ', end_time - start_time)
            return nodo.encontrar_camino(inicio)
        else:
            for n in nodo.encontrar_sucesores():
                if n.estado not in explorados:
                    frontera.append(n)

    end_time = time.process_time()
    print("No llegó al objetivo")  # resultado de la busqueda fracaso
    print("Cantidad de nodos expandidos: ", len(explorados))
    print("Cantidad de nodos frontera: ", len(frontera))
    print('Tiempo de búsqueda: ', end_time - start_time)

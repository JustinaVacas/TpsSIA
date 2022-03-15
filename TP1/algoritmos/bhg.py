import time
from TP1.utiles.nodos import NodoH
from TP1.utiles import heuristicas


def bhg(inicial, objetivo, heuristica):
    explorados = set()
    frontera = []
    if heuristica == 'M':
        frontera.append(NodoH(inicial, None, None, 0, heuristica, heuristicas.manhattan_distance(inicial)))
    elif heuristica == 'H':
        frontera.append(NodoH(inicial, None, None, 0, heuristica, heuristicas.hamming_distance(inicial)))
    elif heuristica == 'NA':
        frontera.append(NodoH(inicial, None, None, 0, heuristica, heuristicas.noadmisible(inicial)))
    else:
        print('Error, inserte una heuristica valida')
        return
    start_time = time.process_time()

    while frontera:
        nodo = frontera.pop()

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
            return nodo.encontrar_camino(inicial)

        frontera.extend(nodo.encontrar_sucesores())
        frontera.sort(key=lambda x: x.valor_heuristica, reverse=True)

    end_time = time.process_time()
    print("No llegó al objetivo")  # resultado de la busqueda fracaso
    print("Cantidad de nodos expandidos: ", len(explorados))
    print("Cantidad de nodos frontera: ", len(frontera))
    print('Tiempo de búsqueda: ', end_time - start_time)

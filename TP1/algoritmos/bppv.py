from collections import deque
from TP1.utiles.nodos import Nodo


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

        while len(frontera) != 0:
            aux = frontera.pop()
            if aux.estado != nodo_inicial.estado:
                faltantes.add(aux)

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
            frontera.extend(nodo.encontrar_sucesores())
            for nodos in expandir:
                frontera.extend(nodos.encontrar_sucesores())
            expandir.clear()

        for elem in explorados:
            elem.imprimir()

    print("\n No llego al objetivo")  # resultado de la busqueda fracaso


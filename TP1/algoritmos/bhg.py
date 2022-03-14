from TP1.utils.nodos import NodoH


def bhg(estado_inicial, estado_objetivo):
    inicial = NodoH(estado_inicial, None, None, 0, 0)
    arbol = [inicial]
    frontera = [inicial]
    #    frontera = set(estado_inicial)
    explorados = set()
    while len(frontera) != 0:
        nodo_actual = frontera.pop()
        if nodo_actual == estado_objetivo:
            print("\n Llego al objetivo!")
            print("Cantidad de nodos expandidos: ", len(explorados))
            print("Profundidad: ", nodo_actual.profundidad)
            return nodo_actual.encontrar_camino(estado_inicial)
        else:
            for sucesor in nodo_actual.encontrar_sucesores():
                frontera.append(sucesor)
            # frontera.append(nodo_actual.encontrar_sucesores())
            for nodos in arbol:
                for sucesor in nodos.encontrar_sucesores():
                    frontera.append(sucesor)
                    arbol.append(sucesor)
                # frontera.extend(nodos.encontrar_sucesores())
                # arbol.extend(nodos.encontrar_sucesores())
                nodos.imprimir()
            sorted(frontera, key=lambda nodo: nodo.heuristica)

    print("\n No llego al objetivo")  # resultado de la busqueda fracaso


from TP1.utiles.nodos import Nodo
import time

LIMITE_DEFAULT = 20
LIMITE_AUMENTO = 5


def bppv(inicio, objetivo, limite):
    if limite == -1:
        limite = LIMITE_DEFAULT

    start_time = time.process_time()

    fondo_arbol = False

    while not fondo_arbol:
        resultado, fondo_arbol = bppv_rec(Nodo(inicio, None, None, 0), objetivo, 0, limite)
        if resultado is not None:
            end_time = time.process_time()
            print("Llegó al objetivo!")
            print("Profundidad: ", resultado.profundidad)
            print('Costo: ', resultado.profundidad)
            print('Limite final: ', limite)
            print('Tiempo de búsqueda: ', end_time - start_time)
            return resultado.encontrar_camino(inicio)
        limite += LIMITE_AUMENTO
        print('Incrementando el limite a: ', limite)

    end_time = time.process_time()
    print("No llegó al objetivo")  # resultado de la busqueda fracaso
    print('Tiempo de búsqueda: ', end_time - start_time)


def bppv_rec(nodo, objetivo, profundidad, limite):
    if nodo.estado == objetivo:
        return nodo, True

    if profundidad == limite:
        if len(nodo.encontrar_sucesores()) > 0:
            return None, False
        else:
            return None, True

    fondo_arbol = True
    for i in range(len(nodo.encontrar_sucesores())):
        resultado, fondo_arbol_rec = bppv_rec(nodo.encontrar_sucesores()[i], objetivo, profundidad + 1, limite)

        if resultado is not None:
            return resultado, True
        fondo_arbol = fondo_arbol and fondo_arbol_rec
    return None, fondo_arbol

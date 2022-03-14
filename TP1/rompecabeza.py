'''
import json
import sys

from algoritmos.bpa import bpa

ESTADO_OBJETIVO = (1, 2, 3, 4, 5, 6, 7, 8, 0)

if len(sys.argv) < 2 or not str(sys.argv[1]).endswith('.json'):
    print('Argumentos invalidos')
    exit()

with open(sys.argv[1], 'r') as configuracion:
    config = json.load(configuracion)

    if not 'algoritmo' in config:
        print('Debe especificar un algoritmo en el archivo de configuracion')
        config.close()
        exit()

    estado_inicial = []
    if 'estado_inicial' in config:
        for c in range(0, len(config['estado_inicial'])):
            if config['estado_inicial'][c] == " " or config['estado_inicial'][c] == ',' or config['estado_inicial'][c] == '(' or config['estado_inicial'][c] == ')':
                continue
            else:
                estado_inicial.append(int(config['estado_inicial'][c]))
    inicial = tuple(estado_inicial)

    if 'limite' in config:
        if config['limite'] > 0:
            limite = config['limite']
        else:
            limite = -1

    if 'heuristica' in config:
        if config['heuristica'] == 'Manhattan' or config['heuristica'] == 'Hamming':
            heuristica = config['heuristica']
        else:
            heuristica = -1

    algoritmo = config['algoritmo']
    heuristicas = {"Manhattan", "Hamming"}

    print(algoritmo)
    print(inicial)
    print(heuristica)
    print(limite)

    if algoritmo == 'BPA':
        s = bpa(inicial, ESTADO_OBJETIVO)
    # elif algoritmo == 'BPP':
    #     s = bpp(inicial, ESTADO_OBJETIVO)
    # elif algoritmo == 'BPPV':
    #     s = bppv(estado_inicial, limit)
    # elif algoritmo == 'BHG':
    #     s = bhg(estado_inicial, heu))
    # elif algoritmo == 'BHL':
    #     s = bhl(estado_inical)
    # elif algoritmo == 'A*':
    #     s = a*(estado_inical)
    else:
        print('Algoritmo incorrecto')
        configuracion.close()
        exit()
    configuracion.close()
'''
from TP1.algoritmos.bpa import bpa
from TP1.utils.nodos import Nodo


def main():
    estado_objetivo = (1, 2, 3, 4, 5, 6, 7, 8, 0)
    estado_inicial = (0, 1, 3, 4, 2, 5, 7, 8, 6)  # (0, 1, 3, 4, 2, 5, 7, 8, 6)
    print("Estado inicial:")
    Nodo(estado_inicial, None, None, 0).imprimir()
    print("----------------")
    bpa(estado_inicial, estado_objetivo)
    # bpp(estado_inicial, estado_objetivo)
    # bppv(estado_inicial, estado_objetivo, 2)
    # bhg(estado_inicial, estado_objetivo)
    print("----------------")
    print("Estado final:")
    Nodo(estado_objetivo, None, None, 0).imprimir()


if __name__ == '__main__':
    main()

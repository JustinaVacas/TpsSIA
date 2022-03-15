import json
import sys

from TP1.algoritmos.aestrella import aestrella
from TP1.algoritmos.bhg import bhg
from TP1.algoritmos.bhl import bhl
from TP1.algoritmos.bpp import bpp
from TP1.algoritmos.bppv import bppv
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
            if config['estado_inicial'][c] == " " or config['estado_inicial'][c] == ',' or config['estado_inicial'][c] \
                    == '(' or config['estado_inicial'][c] == ')':
                continue
            else:
                estado_inicial.append(int(config['estado_inicial'][c]))
    inicial = tuple(estado_inicial)

    if 'limite' in config:
        if config['limite'] > 0:
            limite = config['limite']
        else:
            limite = 'No aplicado.'

    if 'heuristica' in config:
        if config['heuristica'] == 'M' or config['heuristica'] == 'H' or config['heuristica'] == 'NA':
            heuristica = config['heuristica']
        else:
            heuristica = 'No aplicada.'

    algoritmo = config['algoritmo']

    print('Algoritmo seleccionado: ', algoritmo)
    print('Estado inicial: ', inicial)
    if heuristica == 'M':
        print('Heuristica: Manhattan')
    elif heuristica == 'H':
        print('Heuristica: Hamming')
    elif heuristica == 'NA':
        print('Heuristica: No admisible')
    else:
        print('Heuristica: No aplicada')
    print('Limite: ', limite)
    print('\n')

    if algoritmo == 'BPA':
        s = bpa(inicial, ESTADO_OBJETIVO)
    elif algoritmo == 'BPP':
        s = bpp(inicial, ESTADO_OBJETIVO)
    elif algoritmo == 'BPPV':
        if limite == 'No aplicado.':
            s = bppv(inicial, ESTADO_OBJETIVO, -1)
        else:
            s = bppv(inicial, ESTADO_OBJETIVO, limite)
    elif algoritmo == 'BHG':
        s = bhg(inicial, ESTADO_OBJETIVO, heuristica)
    elif algoritmo == 'BHL':
        s = bhl(inicial, ESTADO_OBJETIVO, heuristica)
    elif algoritmo == 'A*':
        s = aestrella(inicial, ESTADO_OBJETIVO, heuristica)
    else:
        print('Algoritmo incorrecto')
        configuracion.close()
        exit()

    configuracion.close()

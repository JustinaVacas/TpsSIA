correcto = (1, 2, 3, 4, 5, 6, 7, 8, 0)


# cantidad de estados que estan mal
def hamming_distance(estado):
    if estado is None:
        return -1
    piezas_incorrectas = 0
    i = 0
    while i < 9:
        if estado[i] != correcto[i]:
            piezas_incorrectas += 1
        i += 1
    return piezas_incorrectas


# numero de pasos para llega al resultado
def manhattan_distance(estado):
    if estado is None:
        return -1
    heu = 0
    i = 0
    position = 0
    while i < 9:
        j = 0
        flag = 1
        if estado[i] != correcto[i]:
            while j < 9 and flag:
                if correcto[j] == estado[i]:
                    flag = 0
                    position = j
                j += 1
            aux = abs(position - i)
            aux2 = 0
            while (aux - 3) > 0:
                aux -= 3
                aux2 += 1
            heu += aux + aux2
        i += 1
    return heu


def noadmisible(estado):
    if estado is None:
        return -1
    piezas_incorrectas = 0
    i = 0
    while i < 9:
        if estado[i] != correcto[i]:
            piezas_incorrectas += 1 + i
        i += 1
    return piezas_incorrectas

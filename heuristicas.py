OBJETIVO = (1, 2, 3, 4, 5, 6, 7, 8, 0)


def hamming_distance(actual):
    heu = 0
    i = 0
    while i < 9:
        if actual[i] != OBJETIVO[i]:
            heu += 1
        i += 1
    return heu


def manhattan_distance(actual):
    heu = 0
    i = 0
    position = 0
    while i < 9:
        j = 0
        flag = 1
        if actual[i] != OBJETIVO[i]:
            while j < 9 and flag:
                if OBJETIVO[j] == actual[i]:
                    flag = 0
                    position = j
                j += 1
            aux = abs(position-i)
            aux2 = 0
            while (aux-3) > 0:
                aux -= 3
                aux2 += 1
            heu += aux + aux2
        i += 1
    return heu


def main():
    actual = (3, 2, 8, 4, 5, 6, 7, 1, 0)
    heuritica1 = hamming_distance(actual)
    print("la heuristica1 es: ", heuritica1)

    heuritica2 = manhattan_distance(actual)
    print("la heuristica2 es: ", heuritica2)


if __name__ == '__main__':
    main()

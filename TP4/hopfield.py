import numpy as np
from TP4.letters import get_alphabet, get_letters


def print_letter(letter):
    for i in range(25):
        if letter[i] == 1:
            print("* ", end=" ")
        else:
            print("  ", end=" ")
        if i == 4 or i == 9 or i == 14 or i == 19 or i == 24:
            print('\n')


def hopfield(patrones, entrada):
    # pesos sinapticos
    weights = np.zeros((len(patrones[0]), len(patrones[0])))
    for i in range(len(patrones[0])):
        for j in range(len(patrones[0])):
            if i == j:
                weights[i][j] = 0
            else:
                suma = 0
                for k in range(len(patrones)):
                    suma += patrones[k][i] * patrones[k][j]
                weights[i][j] = suma / len(patrones[0])
    # print(weights)

    # inicializacion
    previous = entrada
    states = np.zeros(25)

    # iteracion hasta convergencia, hasta que sea estable
    while not np.array_equiv(previous, states):
        for i in range(25):
            aux = 0
            for j in range(25):
                if i != j:
                    aux += weights[i][j] * previous[j]
            states[i] = int(np.sign(aux)) if aux != 0 else 0
        if not np.array_equiv(previous, states):
            previous = states
            states = np.zeros(25)
        print("-----actual----\n")
        print_letter(previous)

    print("Final states\n")
    print_letter(states)

    return states


if __name__ == "__main__":

    RUIDO = 0.7

    letters = get_letters()
    alphabet = get_alphabet()

    alphabet = np.array([np.array(abc).flatten() for abc in alphabet]) # para que me quede 26 arrays de 25 numeros y no array de array de array

    # elijo 4 patrones
    patrones = np.zeros((4, 25))
    patrones_letras = []
    randoms = []
    for i in range(4):
        num = np.random.randint(0, 25)
        while num in randoms:
            num = np.random.randint(0, 25)
        randoms.append(num)
        patrones[i] = alphabet[num]
        patrones_letras.append(letters[num])
        print("Patron nro", i, ":", patrones_letras[i], patrones[i])
        print(patrones_letras[i])

    # elijo un patron de los 4 anteriores
    rand = np.random.randint(0, 3)
    original = patrones[rand]
    print("ORIGINAL:\n letra", patrones_letras[rand], patrones[rand])
    print_letter(original)
    print('\n')

    # altero el elejido
    alterada = np.copy(original)
    for i in range(0, 25):
        p = np.random.uniform()
        if p < RUIDO:
            alterada[i] = alterada[i]*-1
    print("ALTERADA", alterada)
    print('\n')
    print_letter(alterada)

    states = hopfield(patrones, alterada)

    print("-------------------------------------------------")

    if np.array_equiv(original, states):
        print(original)
        print_letter(original)
        print(states)
        print_letter(states)
        print("Correcto")

    else:
        print("Incorrecto")

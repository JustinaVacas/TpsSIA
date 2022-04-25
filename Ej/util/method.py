from Ej.util.function import error


def g_des(X, alpha, n, points, output):
    print("Valores iniciales: X=" + str(X))
    aux = 0
    results = []
    for i in range(n):
        aux, gradient = error(X, output, points)
        print(gradient)
        for x in X:
            x = x-alpha*gradient
        print(X)

        results.append([i+1, aux])                   #Me guardo las iteraciones para graficarlas

    print("Resultados: X=" + str(X) + " Error = " + str(aux))
    return results

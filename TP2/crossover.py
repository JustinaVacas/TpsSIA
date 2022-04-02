import random


def uniform_crossover(x1, x2):
    y1 = list()
    y2 = list()
    for i in range(len(x1)):
        p = random.randint(0, 1)
        if p == 1:
            y1.append(x2[i])
            y2.append(x1[i])
        else:
            y1.append(x1[i])
            y2.append(x2[i])
    return y1, y2


# x1 [a1 a2 a3 a4]
# x2 [b1 b2 b3 b4]
def simple_crossover(x1, x2):
    p = random.randint(1, len(x1))
    y1 = list(x1[:p])
    y2 = list(x2[:p])
    y1[p:] = x2[p:]
    y2[p:] = x1[p:]
    return y1, y2


def multiple_crossover(x1, x2):
    c = random.randint(2, len(x1)-1)
    points = random.sample(range(1, len(x1)), c)
    points.sort()
    y1 = list(x1[:])
    y2 = list(x2[:])
    for j in range(len(points)):
        if j % 2 != 0:
            y1[points[j-1]:points[j]], y2[points[j-1]:points[j]] = x2[points[j-1]:points[j]], x1[points[j-1]:points[j]]
    return y1, y2

zahlenliste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def verzehnfache(x):
    return x * 10


def quadriere(x):
    return x ** 2


zahlenliste = (list(map(lambda zahl: verzehnfache(zahl), zahlenliste)))
print(zahlenliste)
print(list(map(lambda zahl: quadriere(zahl), zahlenliste)))

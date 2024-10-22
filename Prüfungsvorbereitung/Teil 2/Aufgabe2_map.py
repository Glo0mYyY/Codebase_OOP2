zahlenliste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def quadriere(x):
    return x ** 2

print(list(map(lambda zahl: quadriere(zahl), zahlenliste)))

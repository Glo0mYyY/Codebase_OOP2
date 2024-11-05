zahlenliste = [-5,-4,-3,-2,-1,0 ,1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]


def ist_kleinerZehn(x):
    return x <= 10


def ist_positiv(x):
    return x >= 0


zahlenliste = (list(filter(lambda zahl: ist_kleinerZehn(zahl), zahlenliste)))
print(list(filter(lambda zahl: ist_positiv(zahl), zahlenliste)))

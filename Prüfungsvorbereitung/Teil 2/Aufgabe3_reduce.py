from functools import reduce

zahlenliste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def addiere(x, y):
    return x + y


def multipliziere(x, y):
    return x * y


print(reduce(lambda x, y: addiere(x,y), zahlenliste))
print(reduce(lambda x, y: multipliziere(x, y), zahlenliste))

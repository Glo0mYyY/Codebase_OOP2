from functools import reduce

zahlenliste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 60,-10, 80]

def groesste(x, y):
    if x > y:
        return x
    else:
        return y

def kleinste(x, y):
    if x > y:
        return y
    else:
        return x

print(reduce(lambda x, y: groesste(x, y), zahlenliste))
print(reduce(lambda x, y: kleinste(x, y), zahlenliste))

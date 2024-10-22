zahlenliste=[1,2,3,4,5,6,7,8,9,10]

def ist_gerade(x):
    return x % 2 == 0


def ist_durch_drei_teilbar(x):
    return x % 3 == 0


print(list(filter(lambda zahl: ist_gerade(zahl), zahlenliste)))
print(list(filter(lambda zahl: ist_durch_drei_teilbar(zahl), zahlenliste)))

def sortiere_ziffern(zahlen):
    return sorted(zahlen, key=lambda x: len(str(x)))

zahlen = [123,11111, 45, 6789]
sortierte_zahlen = sortiere_ziffern(zahlen)
print(sortierte_zahlen)
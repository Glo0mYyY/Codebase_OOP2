def squared(numbers):
    filteredList = list (filter(lambda x: x % 2 == 0, numbers))
    squares = map(lambda x: x**2, filteredList)
    return squares

print(list(squared([1, 2, 3, 4, 5])))
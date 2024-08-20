def squared(numbers):
    squares = map(lambda x: x**2, numbers)
    return squares

print(list(squared([1, 2, 3, 4, 5])))
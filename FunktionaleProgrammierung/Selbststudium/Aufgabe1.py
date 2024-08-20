from functools import reduce
def squared(numbers):
    filteredList = filter(lambda x: x % 2 == 0, numbers)
    squares = map(lambda x: x**2, filteredList)
    summedSquares = reduce(lambda x, y: x + y, squares)
    return summedSquares

print(squared([1, 2, 3, 4, 5]))
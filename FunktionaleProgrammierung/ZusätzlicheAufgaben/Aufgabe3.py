def filter_palindrom(words):
    return list(filter(lambda word: word == word[::-1], words))

print(filter_palindrom(["hello", "world", "python","anna"]))
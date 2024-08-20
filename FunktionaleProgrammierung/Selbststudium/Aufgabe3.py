alphabet = ["d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
words = ["Hello", "World", "Python", "Programming", "is", "fun"]

def checkAlphabet(words):
    filteredWord = filter(lambda x: all(char.lower() in alphabet for char in x), words)
    return filteredWord

print(list(checkAlphabet(words)))
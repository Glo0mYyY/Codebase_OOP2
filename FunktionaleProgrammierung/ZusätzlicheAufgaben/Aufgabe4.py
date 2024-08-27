def reverse_words(word_list):
    return list(map(lambda word: word[::-1], word_list))

print(list(reverse_words(["Hello", "World", "Python"])))
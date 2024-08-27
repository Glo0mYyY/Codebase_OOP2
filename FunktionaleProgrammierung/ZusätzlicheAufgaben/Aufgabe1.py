def convert_to_uppercase(word_list):
    return list(map(lambda word: word.upper(), word_list))

print(list(convert_to_uppercase(["Hello", "World", "Python"])))
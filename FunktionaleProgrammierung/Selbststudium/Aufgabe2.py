def uppercaseOnly(words):
    uppercaseWords = filter(lambda x: x.isupper() == True, words)
    return uppercaseWords

print(list(uppercaseOnly(["TEST","hELLO","ciao"])))

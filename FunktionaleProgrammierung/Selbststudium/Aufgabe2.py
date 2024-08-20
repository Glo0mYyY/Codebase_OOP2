def uppercaseOnly(words):
    uppercaseWords = filter(lambda x: x.isupper(), words)
    return uppercaseWords

print(list(uppercaseOnly(["TEST","hELLO","ciao"])))

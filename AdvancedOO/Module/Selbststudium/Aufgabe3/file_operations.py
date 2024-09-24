def readFile(filename):
    with open (filename, 'r') as file:
        return file.read()
    
def writeFile(filename, content):
    with open (filename, 'w') as file:
        file.write(content)
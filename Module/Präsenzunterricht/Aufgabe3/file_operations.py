def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "File not found"
    except IOError:
        return "I/O Error occurred"
    except:
        return "An error occurred"
    
def write_file(file_name, content):
    try:
        with open(file_name, 'w') as file:
            return file.write(content)
    except FileNotFoundError:
        return "File not found"
    except IOError:
        return "I/O Error occurred"
    except:
        return "An error occurred"

def append_to_file(file_name, content):
    try:
        with open(file_name, 'a') as file:
            return file.write(content)
    except FileNotFoundError:
        return "File not found"
    except IOError:
        return "I/O Error occurred"
    except:
        return "An error occurred"

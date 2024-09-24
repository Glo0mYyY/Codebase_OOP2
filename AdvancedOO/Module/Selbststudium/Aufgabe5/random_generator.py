import random
import string


def generate_random_number():
    return random.randint(1, 100)


#https: // www.delftstack.com/de/howto/python/random-string-python/

def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))

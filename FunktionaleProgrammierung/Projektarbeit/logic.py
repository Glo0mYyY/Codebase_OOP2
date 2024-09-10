import random


def generate_random_number():
    """Eine reine Funktion, die eine zufällige Zahl zwischen 1 und 100 generiert."""
    return random.randint(1, 100)


def check_guess(guess, number_to_guess):
    """Vergleicht die geratene Zahl mit der Zielzahl."""
    if guess < number_to_guess:
        return "zu niedrig"
    elif guess > number_to_guess:
        return "zu hoch"
    else:
        return "richtig"

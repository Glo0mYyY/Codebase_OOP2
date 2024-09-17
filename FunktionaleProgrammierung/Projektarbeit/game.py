from logic import check_guess, generate_random_number
from storage import save_result, load_results
import json

class Game:
    def __init__(self, max_attempts=6):
        self.max_attempts = max_attempts
        self.number_to_guess = generate_random_number()
        self.attempts = 0
        self.score = 0
        self.difficulty = 1 # 1 = easy, 2 = medium, 3 = hard
        self.max_attempts = 6

    def play(self):
        print("Willkommen zum Zahlenratespiel!")
        print("Ich habe mir eine Zahl zwischen 1 und 100 ausgedacht.")

        print("Wähle den Schwierigkeitsgrad:")
        print("1 - einfach (8 Versuche)")
        print("2 - mittel (6 Versuche)")
        print("3 - schwer (5 Versuche)")

        self.difficulty = int(input("Gib die Nummer des Schwierigkeitsgrads ein: "))
        if self.difficulty == 1:
            self.max_attempts = 8
        elif self.difficulty == 2:
            self.max_attempts = 6
        elif self.difficulty == 3:
            self.max_attempts = 5
        else:
            self.max_attempts = 8
            print(f"Ungültige Eingabe, Standard-Schwierigkeitsgrad {self.dificulty} wird verwendet.")

        print(f"Du hast {self.max_attempts} Versuche, um sie zu erraten.")

        while self.attempts < self.max_attempts:
            user_input = input("Gib eine Zahl ein: ")

            if not user_input.isdigit():
                print("Bitte gib eine gültige Zahl ein.")
                continue

            guess = int(user_input)
            self.attempts += 1
            result = check_guess(guess, self.number_to_guess)

            if result == "richtig":
                self.score = self.max_attempts - self.attempts + 1
                print(f"Glückwunsch! Du hast die richtige Zahl erraten: {
                      self.number_to_guess}")
                print(f"Dein Punktestand ist: {self.score}")
                break
            elif result == "zu hoch":
                print("Deine Zahl ist zu hoch.")
            else:
                print("Deine Zahl ist zu niedrig.")

        if self.attempts == self.max_attempts and result != "richtig":
            print(f"Leider hast du keine Versuche mehr. Die Zahl war {
                  self.number_to_guess}.")

        save_result({"score": self.score, "attempts": self.attempts, "difficulty": self.difficulty})

# Wenn das Modul direkt ausgeführt wird, wird das Spiel gestartet
if __name__ == "__main__":
    while True:
        game = Game()
        game.play()
        print("Bisherige Ergebnisse:")
        print(json.dumps(load_results(), indent=4))
        if input("Möchtest du noch einmal spielen? (j/n) ") != "j":
            break

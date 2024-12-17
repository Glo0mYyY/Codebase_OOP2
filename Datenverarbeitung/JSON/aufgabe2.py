import json

# JSON-Datei öffnen und Daten laden
with open("students.json") as file:
    data = json.load(file)

# Namen und Noten aller Studenten ausgeben
for student in data["students"]:
    print(f"Name: {student['name']}, Note: {student['grade']}")

# Alter des letzten Studenten erhöhen
last_student = data["students"][-1]
last_student["age"] += 1

# Geänderte Daten in die JSON-Datei schreiben
with open("students.json", "w") as file:
    json.dump(data, file, indent=4)

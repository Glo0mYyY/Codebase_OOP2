import json

# JSON-Datei öffnen und Daten laden
with open("books.json") as file:
    data = json.load(file)

# Titel aller Bücher ausgeben
for book in data["books"]:
    print(book["title"])

# Jahr des ersten Buches ändern
data["books"][0]["year"] = 2021

# Geänderte Daten in die JSON-Datei schreiben
with open("books.json", "w") as file:
    json.dump(data, file, indent=4)

import json

# JSON-Daten erstellen
data = {
    "fruits": [
        {
            "name": "Apple",
            "color": "red",
            "price": 1.5
        },
        {
            "name": "Banana",
            "color": "yellow",
            "price": 0.5
        },
        {
            "name": "Orange",
            "color": "orange",
            "price": 0.8
        }
    ]
}

# JSON-Daten in die Datei "fruits.json" schreiben
with open("fruits.json", "w") as file:
    json.dump(data, file, indent=4)

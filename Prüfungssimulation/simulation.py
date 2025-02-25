import json
import pandas as pd
import xml.etree.ElementTree as ET
import numpy as np
import os

# Aufgabe 1: Dictionaries und JSON
animals = {
    "Tiere": [
        {"Name": "Bella", "Art": "Hund", "Alter": 5},
        {"Name": "Milo", "Art": "Katze", "Alter": 3},
        {"Name": "Charlie", "Art": "Papagei", "Alter": 2}
    ]
}

# Speichern als JSON
with open("tiere.json", "w") as file:
    json.dump(animals, file, indent=4)

# Lesen aus JSON
with open("tiere.json", "r") as file:
    data = json.load(file)
    print("JSON-Inhalt:", json.dumps(data, indent=4))

# Aufgabe 2: Verarbeitung von JSON und Pandas
df = pd.DataFrame(data["Tiere"])
df["Gewicht"] = [20, 5, 1]  # Beispielwerte

df.to_csv("tiere.csv", index=False)
print("CSV-Datei gespeichert.")

# Sicherstellen, dass die XML-Datei im gleichen Pfad ist
xml_path = os.path.join(os.path.dirname(__file__), "buecher.xml")

# Einlesen der XML-Datei
tree = ET.parse(xml_path)
root = tree.getroot()

for buch in root.findall("Buch"):
    titel = buch.find("Titel").text
    autor = buch.find("Autor").text
    print(f"Buch: {titel}, Autor: {autor}")

# Aufgabe 4: NumPy-Arrays mit Daten aus Dictionaries
temperatures = {"Montag": 18, "Dienstag": 20,
                "Mittwoch": 22, "Donnerstag": 19, "Freitag": 21}
values = np.array(list(temperatures.values()))

print("Mittelwert:", np.mean(values))
print("Maximalwert:", np.max(values))
print("Minimalwert:", np.min(values))

# Aufgabe 5: XML-Daten in Pandas DataFrame konvertieren
daten = []
for buch in root.findall("Buch"):
    titel = buch.find("Titel").text
    autor = buch.find("Autor").text
    jahr = buch.find("Erscheinungsjahr").text
    daten.append({"Titel": titel, "Autor": autor, "Erscheinungsjahr": jahr,
                 "Seitenzahl": np.random.randint(100, 500)})

df_buecher = pd.DataFrame(daten)
print(df_buecher)

# Aufgabe 6: Analyse mit Pandas und NumPy
df_tiere = pd.read_csv("tiere.csv")
alter_array = df_tiere["Alter"].to_numpy()

print("Durchschnitt:", np.mean(alter_array))
print("Median:", np.median(alter_array))
print("Standardabweichung:", np.std(alter_array))

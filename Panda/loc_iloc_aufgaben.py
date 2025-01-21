import pandas as pd
import numpy as np

# Beispiel-Daten
produkte = ["Apfel", "Banane", "Orange", "Birne"]
monate = ["Jan", "Feb", "Mär", "Apr"]

# Erstellen eines DataFrames mit zufälligen Zahlen
np.random.seed(42)  # für reproduzierbare Ergebnisse
daten = np.random.randint(10, 100, size=(4, 4))
df = pd.DataFrame(data=daten, index=produkte, columns=monate)

print("Originaler DataFrame:")
print(df)

# Aufgabe 1
print("\nAufgabe 1:")
# 1. Wähle mit loc nur die Zeile "Banane" aus dem DataFrame (als Series) aus.
print("\n1. Zeile 'Banane' mit loc:")
print(df.loc["Banane"])

# 2. Gib anschließend die Zeilen "Apfel" und "Orange" aus, aber nur die Spalte "Feb".
print("\n2. Zeilen 'Apfel' und 'Orange' und Spalte 'Feb':")
print(df.loc[["Apfel", "Orange"], "Feb"])

# Aufgabe 2
print("\nAufgabe 2:")
# 1. Hole die Spalten "Jan" und "Apr" für alle Zeilen mit loc.
print("\n1. Spalten 'Jan' und 'Apr' für alle Zeilen:")
print(df.loc[:, ["Jan", "Apr"]]) # : selektiert alle Zeilen

# 2. Erstelle eine boolesche Maske, um nur die Zeilen zu filtern, in denen der Wert in der Spalte "Mär" größer als 50 ist.
print("\n2. Zeilen mit 'Mär' > 50:")
mask = df["Mär"] > 50
print(df.loc[mask])

# Aufgabe 3
print("\nAufgabe 3:")
# 1. Verwende iloc, um aus dem DataFrame die erste Zeile ("Apfel") und die letzte Spalte ("Apr") auszuwählen.
print("\n1. Erste Zeile und letzte Spalte mit iloc:")
print(df.iloc[0, -1])

# 2. Hole mit iloc alle Zeilen, aber nur die mittleren zwei Spalten.
print("\n2. Alle Zeilen, mittlere zwei Spalten mit iloc:")
print(df.iloc[:, 1:3])

# Aufgabe 4
print("\nAufgabe 4:")
# 1. Verwende loc, um alle Produkte von "Banane" bis "Birne" (einschließlich) und die Spalten "Feb" bis "Apr" zu holen.
print("\n1. Produkte von 'Banane' bis 'Birne' und Spalten 'Feb' bis 'Apr':")
print(df.loc["Banane":"Birne", "Feb":"Apr"])

# 2. Verwende iloc, um die mittleren zwei Zeilen (Index 1 und 2) und die mittleren zwei Spalten (Index 1 und 2) zu holen.
print("\n2. Mittlere zwei Zeilen und mittlere zwei Spalten mit iloc:")
print(df.iloc[1:3, 1:3])

# Aufgabe 5
print("\nAufgabe 5:")
# Erstelle ein eigenes kleines DataFrame
new_df = pd.DataFrame({
    "X": [10, 20, 30, 40, 50],
    "Y": [15, 25, 35, 45, 55],
    "Z": [20, 30, 40, 50, 60]
}, index=["A", "B", "C", "D", "E"])

print("\nEigenes DataFrame:")
print(new_df)

# 1. Nur bestimmte Zeilen auswählen
print("\n1. Zeilen 'B' und 'D':")
print(new_df.loc[["B", "D"]])

# 2. Nur bestimmte Spalten auswählen
print("\n2. Spalten 'X' und 'Z':")
print(new_df.loc[:, ["X", "Z"]])

# 3. Beliebige Teilbereiche (Slicing) extrahieren
print("\n3. Teilbereich Zeilen 'B':'D', Spalten 'Y':'Z':")
print(new_df.loc["B":"D", "Y":"Z"])

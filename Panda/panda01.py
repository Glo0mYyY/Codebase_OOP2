import os
import pandas as pd

# Datenrahmen erstellen
daten = {
    "Name": ["herbert", "jan", "tim", "elias", "tim"],
    "Alter": [22, 29, 34, 19, 28],
    "Stadt": ["soly west", "Chur", "Winti amk", "bern", "Genf"]
}
df = pd.DataFrame(daten)
print("Datenrahmen:")
print(df)

# Datenrahmen filtern
gefiltert = df[df["Alter"] > 25]
print("\nGefilterter Datenrahmen (Alter > 25):")
print(gefiltert)

# Spalten auswählen
namen = df["Name"]
print("\nSpalte 'Name':")
print(namen)

# Summen und Durchschnitte berechnen
summe_alter = df["Alter"].sum()
durchschnitt_alter = df["Alter"].mean()
print("\nSumme des Alters:", summe_alter)
print("Durchschnitt des Alters:", durchschnitt_alter)

# Sortieren und speichern
sortierter_df = df.sort_values(by="Alter", ascending=False)
# Get the directory where the script is run
script_dir = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(script_dir, "sortierte_daten.csv")

# Save the sorted DataFrame to the output path
sortierter_df.to_csv(output_path, index=False)
print("\nDer sortierte Datenrahmen wurde in " + output_path + " gespeichert.")

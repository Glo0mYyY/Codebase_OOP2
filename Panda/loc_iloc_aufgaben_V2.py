import pandas as pd
import numpy as np

produkte = ["Apfel", "Banane", "Orange", "Birne"]
monate = ["Jan", "Feb", "Mär", "Apr"]

np.random.seed(42)
daten = np.random.randint(10, 100, size=(4, 4))
df = pd.DataFrame(data=daten, index=produkte, columns=monate)

print("Base")
print(df)

# Aufgabe 1
print("\nAufgabe 1:")
print(df.loc["Banane"])
print(df.loc[["Apfel", "Orange"], "Feb"])

# Aufgabe 2
print("\nAufgabe 2:")
print(df.loc[:, ["Jan", "Apr"]])
mask = df["Mär"] > 50
print(df.loc[mask])

# Aufgabe 3
print("\nAufgabe 3:")
print(df.iloc[0, -1])
print(df.iloc[:, 1:3])

# Aufgabe 4
print("\nAufgabe 4:")
print(df.loc["Banane":"Birne", "Feb":"Apr"])
print(df.iloc[1:3, 1:3])

# Aufgabe 5

new_df = pd.DataFrame({})
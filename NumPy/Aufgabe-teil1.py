import numpy as np

# Übung 1: Erstellen Sie ein NumPy-Array mit den ganzen Zahlen von 1 bis 10 und geben Sie es aus.
array_1_to_10 = np.arange(1, 11)
print("Array von 1 bis 10:", array_1_to_10)

# Übung 2: Erzeugen Sie eine 3x3-Matrix mit den Zahlen 1 bis 9 und berechnen Sie die Summe der Diagonalelemente.
matrix_3x3 = np.arange(1, 10).reshape(3, 3)
diagonal_sum = np.trace(matrix_3x3)
print("3x3 Matrix:\n", matrix_3x3)
print("Summe der Diagonalelemente:", diagonal_sum)

# Übung 3: Erstellen Sie ein NumPy-Array mit 20 zufälligen Ganzzahlen zwischen 1 und 100. Finden Sie das Maximum, das Minimum und den Durchschnitt dieser Zahlen.
random_array = np.random.randint(1, 101, 20)
max_value = np.max(random_array)
min_value = np.min(random_array)
mean_value = np.mean(random_array)

print("Zufällige Zahlen:", random_array)
print("Maximum:", max_value)
print("Minimum:", min_value)
print("Durchschnitt:", mean_value)

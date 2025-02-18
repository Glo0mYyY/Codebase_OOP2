import numpy as np

# Übung 1
arr = np.linspace(0, 1, 20)
print("Durchschnitt:", np.mean(arr))
print("Summe:", np.sum(arr))
print("Median:", np.median(arr))
print("Standardabweichung:", np.std(arr))

# Übung 2
A = np.random.randint(1, 11, (3, 3))
B = np.random.randint(1, 11, (3, 3))

print("\nMatrix A:\n", A)
print("Matrix B:\n", B)
print("Matrix A * B:\n", np.dot(A, B))
print("Determinante A:", np.linalg.det(A))  # GPT

try:
    print("Inverse B:\n", np.linalg.inv(B))  # GPT
except np.linalg.LinAlgError:  # GPT
    print("B het kei Inverse.")

# Übung 3
nums = np.arange(1, 101)
even = nums[nums % 2 == 0]


def is_prime(n):  # GPT
    if n < 2:
        return False
    for i in range(2, int(np.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


primes = np.array([n for n in nums if is_prime(n)])  # GPT
squares = np.square(nums)

print("\nGerade Zahlen:", even)
print("Primzahlen:", primes)
print("Quadrate:", squares)

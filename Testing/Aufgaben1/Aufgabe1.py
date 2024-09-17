import unittest

class Number:
    def is_prime(self, n):
        for i in range(2, n):
            if (n%i) == 0:
                return False
        return True

class Check_prime(unittest.TestCase):
    def test_prime1(self):
        number = Number()
        isPrimeNumber = number.is_prime(5)
        return self.assertTrue(isPrimeNumber)
    def test_prime2(self):
        number = Number()
        isPrimeNumber = number.is_prime(6)
        return self.assertFalse(isPrimeNumber)

check_prime = Check_prime()
print(check_prime.test_prime1())
print(check_prime.test_prime2())

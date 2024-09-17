import unittest

# AI used
class NumberFunction():
    def factorial(self, n):
        if n == 0 or n == 1:
            return 1
        elif n < 0:
            return False
        else:
            result = 1
            for i in range(2, n+1):
                result *= i
            return result


class Check_factorial(unittest.TestCase):
    def test_correctFactorial(self):
        correctFactorial = NumberFunction()
        resultFactorial = correctFactorial.factorial(5)
        return self.assertEqual(resultFactorial, 120)
    
    def test_invalidFactorial(self):
        correctFactorial = NumberFunction()
        resultFactorial = correctFactorial.factorial(-5)
        return self.assertFalse(resultFactorial)


check_factorial = Check_factorial()
print(check_factorial.test_correctFactorial())
print(check_factorial.test_invalidFactorial())


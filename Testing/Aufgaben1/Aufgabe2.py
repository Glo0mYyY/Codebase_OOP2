import unittest


class ListFunctions():
    def calculate_average(self, numbers):
        sum = 0
        try:
            for number in numbers:
                sum += number
            return sum / len(numbers)
        except ZeroDivisionError:
            return None



class Check_List(unittest.TestCase):
    def test_correctAverage(self):
        listFunction = ListFunctions()
        listAverage = listFunction.calculate_average([1, 2, 3, 4, 5])
        return self.assertEqual(listAverage, 3)

    def test_correctEmpty(self):
        listFunction = ListFunctions()
        listAverage = listFunction.calculate_average([])
        return self.assertIsNone(listAverage)

    def test_correctNegative(self):
        listFunction = ListFunctions()
        listAverage = listFunction.calculate_average([-1, -2, -3, -4, -5])
        return self.assertEqual(listAverage, -3)


check_prime = Check_List()
print(check_prime.test_correctAverage())
print(check_prime.test_correctEmpty())
print(check_prime.test_correctNegative())

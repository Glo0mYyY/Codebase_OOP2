import unittest

class Circle():
    def calculateSurface(self, r):
        return 3.14 * r * r


class Check_Circle(unittest.TestCase):
    def test_correctSurface(self):
        correctSurface = Circle()
        resultSurface = correctSurface.calculateSurface(5)
        return self.assertEqual(resultSurface, 78.5)


check_circle = Check_Circle()
print(check_circle.test_correctSurface())

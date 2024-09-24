import unittest
from unittest.mock import MagicMock


class PriceCalculator:
    def get_price(self, product, quantity):
        # Holt die Preise
        # Apfel = 0.5
        pass

class CalculationTest(unittest.TestCase):
    def test_total_price(self):
        price_check = PriceCalculator()
        price_check.get_price = MagicMock(return_value=1)

        # Rufe die Methode auf
        price = price_check.get_price("Apfel", 2)
        assert price == 1


CalculationTest().test_total_price()
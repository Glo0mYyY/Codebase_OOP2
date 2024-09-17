import unittest

class CharFunction():
    def reverse_string(self, string):
        return string[::-1]
    

class Check_ReverseString(unittest.TestCase):
    def test_correctReverse(self):
        charFunction = CharFunction()
        reversedString = charFunction.reverse_string("Hello")
        return self.assertEqual(reversedString, "olleH")
    
    def test_correctReverseSpecial(self):
        charFunction = CharFunction()
        reversedString = charFunction.reverse_string("He!!o")
        return self.assertEqual(reversedString, "o!!eH")

    def test_correctReverseEmpty(self):
        charFunction = CharFunction()
        reversedString = charFunction.reverse_string("")
        return self.assertEqual(reversedString, "")


check_reverse = Check_ReverseString()
print(check_reverse.test_correctReverse())
print(check_reverse.test_correctReverseSpecial())
print(check_reverse.test_correctReverseEmpty())

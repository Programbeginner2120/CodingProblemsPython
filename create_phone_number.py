import unittest

# URL: https://www.codewars.com/kata/525f50e3b73515a6db000b83

'''Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.

Example: create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"

The returned format must be correct in order to complete this challenge.
Don't forget the space after the closing parentheses!'''


# SOLUTION
def create_phone_number(n):
    phone_number = "(xxx) xxx-xxxx"
    for i in n:
        phone_number = phone_number.replace("x", str(i), 1)
    return phone_number




class TestClass(unittest.TestCase):

    def create_phone_number_test_1(self):
        self.assertEqual(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), "(123) 456-7890")

    def create_phone_number_test_2(self):
        self.assertEqual(create_phone_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), "(111) 111-1111")

    def create_phone_number_test_3(self):
        self.assertEqual(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), "(123) 456-7890")

    def create_phone_number_test_4(self):
        self.assertEqual(create_phone_number([0, 2, 3, 0, 5, 6, 0, 8, 9, 0]), "(023) 056-0890")

    def create_phone_number_test_5(self):
        self.assertEqual(create_phone_number([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), "(000) 000-0000")


TC = TestClass();

try:
    TC.create_phone_number_test_1()
    TC.create_phone_number_test_2()
    TC.create_phone_number_test_3()
    TC.create_phone_number_test_4()
    TC.create_phone_number_test_5()
    print("All test cases valid")

except TC.failureException:
    print("Found inequality when calling assertEqual() on test case")



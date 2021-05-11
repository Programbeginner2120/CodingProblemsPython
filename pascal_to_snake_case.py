import unittest

# URL: https://www.codewars.com/kata/529b418d533b76924600085d

"""Complete the function/method so that it takes CamelCase string and returns the string in snake_case notation. 
Lowercase characters can be numbers. If method gets number, it should return string."""


def to_underscore(string):
    string = str(string)
    new_str = ""
    for i in range(len(string)):
        lowercase_ch = string[i].lower()
        if string[i] != lowercase_ch:
            if (new_str):
                new_str += "_"
        new_str += lowercase_ch
    return new_str


class TestClass(unittest.TestCase):

    def to_underscore_test_1(self):
        self.assertEqual(to_underscore("TestController"), "test_controller")

    def to_underscore_test_2(self):
        self.assertEqual(to_underscore("MoviesAndBooks"), "movies_and_books")

    def to_underscore_test_3(self):
        self.assertEqual(to_underscore("App7Test"), "app7_test")

    def to_underscore_test_4(self):
        self.assertEqual(to_underscore(1), "1")


TC = TestClass();

try:
    TC.to_underscore_test_1()
    TC.to_underscore_test_2()
    TC.to_underscore_test_3()
    TC.to_underscore_test_4()
    print("All test cases valid")


except TC.failureException:
    print("Found inequality when calling assertEqual() on test case")

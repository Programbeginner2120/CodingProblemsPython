import unittest

# URL: https://www.codewars.com/kata/5679aa472b8f57fb8c000047

"""You are going to be given an array of integers. Your job is to take that array and find an index N where the sum of
the integers to the left of N is equal to the sum of the integers to the right of N. If there is no index that would 
make this happen, return -1."""


def find_even_index(arr):
    for i in range(len(arr)):
        if sum(arr[:i]) == sum(arr[i+1:]):
            return i
    return -1


class TestClass(unittest.TestCase):

    def find_even_index_test_1(self):
        self.assertEqual(find_even_index([1,2,3,4,3,2,1]),3)

    def find_even_index_test_2(self):
        self.assertEqual(find_even_index([1,100,50,-51,1,1]),1)

    def find_even_index_test_3(self):
        self.assertEqual(find_even_index([1,2,3,4,5,6]),-1)

    def find_even_index_test_4(self):
        self.assertEqual(find_even_index(list(range(1,100))),-1)

    def find_even_index_test_5(self):
        self.assertEqual(find_even_index(list(range(-100,-1))),-1)


TC = TestClass();

try:
    TC.find_even_index_test_1()
    TC.find_even_index_test_2()
    TC.find_even_index_test_3()
    TC.find_even_index_test_4()
    TC.find_even_index_test_5()
    print("All test cases valid")


except TC.failureException:
    print("Found inequality when calling assertEqual() on test case")


# https://www.codewars.com/kata/5a946d9fba1bb5135100007c/train/python

import math

def isPrime(number):
    if (number <= 1):
        return False

    if (number == 2 or number == 5):
        return True

    string_num = str(number)

    if (int(string_num[-1]) == 1 or int(string_num[-1]) == 3 or int(string_num[-1]) == 7 or int(string_num[-1]) == 9):
        for i in range(2, math.ceil(number / math.log(number))):  # Prime growth rate from number theory
            if (number % i == 0):
                return False
        return True
    return False


def minimum_number(numbers):
    list_sum = sum(numbers)

    for i in range(math.ceil(list_sum / math.log(list_sum))):  # Prime growth rate from number theory
        if (isPrime(list_sum + i)):
            return i
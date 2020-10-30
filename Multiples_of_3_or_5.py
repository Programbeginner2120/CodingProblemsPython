"""Function that returns the sum of all multiples of 3 and 5 below given number"""


def solution(number):
    return sum([i for i in range(number) if i % 3 == 0 or i % 5 == 0])
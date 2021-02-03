# https://www.codewars.com/kata/56662e268c0797cece0000bb/train/python

def sum_fibs(n):

    total_sum = 0
    prev = 0
    current = 1

    for i in range(2, n+ 2):  # Since it's up to n's index and not just n, we use n+2 as upper bound not n+1
        if (current % 2 == 0):
            total_sum += current
        prev, current = current, prev + current
    return total_sum


print(sum_fibs(5))  # 2
print(sum_fibs(9))  # 44
print(sum_fibs(10))  #44
print(sum_fibs(11))  #44
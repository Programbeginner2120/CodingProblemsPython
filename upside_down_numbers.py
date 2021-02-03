#


def solve(a, b):
    num_upside_down = 0
    for num in range(a, b):
        new_num = ''
        i = len(str(num)) - 1
        num = str(num)
        while (i >= 0):
            if  num[i] == '0' or num[i] == '1' or num[i] == '8':
                new_num += num[i]
            elif num[i] == '6':
                new_num += '9'
            elif num[i] == '9':
                new_num += '6'
            else:
                break
            i -= 1
        if new_num == num:
            num_upside_down += 1
    return num_upside_down


print(solve(0, 10))  # 3
print(solve(10, 100))  # 4
print(solve(100, 1000))  # 12
print(solve(1000, 10000))  # 20
print(solve(10000, 15000))  # 6
print(solve(15000, 20000))  # 9
print(solve(60000, 70000))  # 15
print(solve(60000, 130000))  # 55
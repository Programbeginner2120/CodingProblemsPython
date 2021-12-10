def solve(arr):
    new_arr = []
    sum = 0
    for str in arr:
        for i, c in enumerate(str):
            if ord(c.upper()) - 64 == i + 1:
                sum += 1
        new_arr.append(sum)
        sum = 0
    return new_arr
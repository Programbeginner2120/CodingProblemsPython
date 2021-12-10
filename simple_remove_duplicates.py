def solve(arr):
    new_arr = []
    i = len(arr) - 1
    while (i >= 0):
        if arr[i] not in new_arr:
            new_arr.append(arr[i])
        i -= 1
    new_arr.reverse()
    return new_arr
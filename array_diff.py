# https://www.codewars.com/kata/523f5d21c841566fde000009/train/python


def array_diff(a, b):
    for elem_b in b:
        if elem_b in a:
            new_a = []
            for elem_a in a:
                if elem_a != elem_b:
                    new_a.append(elem_a)
            a = new_a
    return a


print(array_diff([1,2], [1]))  # [2]
print(array_diff([1,2,2], [1]))  # [2,2]
print(array_diff([1,2,2], [2]))  # [1]
print(array_diff([1,2,2], []))  # [1,2,2]
print(array_diff([], [1,2]))  # []
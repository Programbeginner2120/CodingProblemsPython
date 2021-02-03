# https://www.codewars.com/kata/54e6533c92449cc251001667/train/python


def unique_in_order(iterable):
    list = []
    lastAppend = '' # Variable to keep track of last appended item
    for i in iterable:
        if (lastAppend != i): # if the last added char does not equal current char
            list.append(i)
            lastAppend = i # current char becomes last appended item
    return list


print(unique_in_order('AAAABBBCCDAABBB'))  # ['A', 'B', 'C', 'D', 'A', 'B']
print(unique_in_order('ABBCcAD'))  # ['A', 'B', 'C', 'c', 'A', 'D']
print(unique_in_order([1,2,2,3,3]))  # [1,2,3]
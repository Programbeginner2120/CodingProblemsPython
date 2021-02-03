# https://www.codewars.com/kata/52774a314c2333f0a7000688/train/python


def valid_parentheses(string):
    balanceFactor = 0
    i = 0
    while (i < len(string)):
        if (string[i] == '('):
            balanceFactor += 1
        elif (string[i] == ')'):
            balanceFactor -= 1
            if (balanceFactor < 0):
                return False
        i += 1
    return balanceFactor == 0


print(valid_parentheses("  ("))  # False
print(valid_parentheses(")test"))  # False
print(valid_parentheses(""))  # True
print(valid_parentheses("hi())("))  # False
print(valid_parentheses("hi(hi)()"))  # True
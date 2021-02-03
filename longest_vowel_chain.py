# https://www.codewars.com/kata/59c5f4e9d751df43cf000035


def solve(s):
    longestSubstringLength = 0
    current = 0
    vowelList = {'a' ,'e' ,'i' ,'o' ,'u'}
    for i in range(len(s)):
        if (s[i] in vowelList):
            current += 1
            if (current > longestSubstringLength):
                longestSubstringLength = current
        else:
            current = 0
    return longestSubstringLength


print(solve("codewarriors"))  # 2
print(solve("suoidea"))  # 3
print(solve("ultrarevolutionariees"))  # 3
print(solve("strengthlessnesses"))  # 1
print(solve("cuboideonavicuare"))  # 2
print(solve("chrononhotonthuooaos"))  # 5
print(solve("iiihoovaeaaaoougjyaw"))  # 8



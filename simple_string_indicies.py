# https://www.codewars.com/kata/5a24254fe1ce0ec2eb000078/train/python

def solve(st, idx):
    if (st[idx] != '('): # If we're not given an open paren, return -1 automatically
        return -1
    paren_balance_factor = 1 # Indicating that there is one open parenthesis
    remaining_string = st[idx+1:] # We only care about the segment after our index
    current_index = idx + 1
    for char in remaining_string:
        if (char == '('):
            paren_balance_factor += 1 # Open paren adds to balance factor
        elif (char == ')'):
            paren_balance_factor -= 1 # Closed paren subtracts from balance factor
        if (paren_balance_factor == 0):
            return current_index # return our current index if balance factor is 0 (if all parenthesis are correct)
        current_index += 1
    return -1 # return -1 if balance factor is not 0 at end of loop (if parenthesis are not correct)

print("Basic tests")
print(solve("((1)23(45))(aB)",0)) # should return 10
print(solve("((1)23(45))(aB)",1)) # should return 3
print(solve("((1)23(45))(aB)",2)) # should return -1
print(solve("((1)23(45))(aB)",6)) # should return 9
print(solve("((1)23(45))(aB)",11)) # should return 14
print(solve("(g(At)IO(f)(tM(qk)YF(n)Nr(E)))",11)) # should return 28
print(solve("(g(At)IO(f)(tM(qk)YF(n)Nr(E)))",0)) # should return 29
print(solve("(>_(va)`?(h)C(as)(x(hD)P|(fg)))",19)) # should return 22


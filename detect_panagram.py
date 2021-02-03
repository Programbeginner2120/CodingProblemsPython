# https://www.codewars.com/kata/545cedaa9943f7fe7b000048/train/python


import string

def is_pangram(s):
    charSet = set(string.ascii_lowercase) # charSet is set of all lowercase letters
    s = s.lower()

    for i in s:
        charSet.discard(i) # discard each unique i in s from charSet

    return len(charSet) == 0 # returns true if charSet is empty


pangram = "The quick, brown fox jumps over the lazy dog!"
print(is_pangram(pangram))  # True
pangram = "abcdefghijklmnopqrstuvwxyz"
print(is_pangram(pangram))  # True
not_pangram = "I am clearly not a pangram"
print(is_pangram(not_pangram))  # False


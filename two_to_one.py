def longest(a1, a2):
    long_str = a1 + a2
    long_str = list(set(long_str))
    long_str.sort()
    return "".join(long_str)
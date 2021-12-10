def circle_of_numbers(n, fst):
    pos = ((n + fst) % n)
    return abs(pos + .5*n) % n
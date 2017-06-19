def gcdIter(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    smaller = min(a, b)
    larger = max(a, b)
    i = 1
    while True:
        if larger % (smaller/i) == 0:
            return int(smaller/i)
        i += 1

print(gcdIter(414, 360))
#18
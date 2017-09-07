def genPrimes():
    yield 2
    x = 2
    p = x - 1
    while True:
        if (x % p) != 0:
            p -= 1
            if p == 1:
                yield x
        else:
            x += 1
            p = x - 1


prime = genPrimes()
for i in range(10):
    print(prime.__next__())

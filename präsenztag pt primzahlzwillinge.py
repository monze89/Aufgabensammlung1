def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n//2+1):
        if n % i == 0:
            return False
    return True

def twinPrimeSum(n):
    sum = 0
    i = 0
    x = 2
    pi = None
    lastp = None
    while i < n:
        if is_prime(x):
            i += 1
            if pi == x-2:
                print(f"({pi} - {x})")
                if lastp != pi:
                    sum += pi
                sum += x
                lastp = x
            pi = x
        x += 1
    return sum

print(twinPrimeSum(6))
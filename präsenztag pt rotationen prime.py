def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n//2+1):
        if n % i == 0:
            return False
    return True

def get_digits(n):
    digits = []
    while n > 0:
        d = n % 10
        n = n // 10
        digits.append(d)
    return digits

def get_number(digits):
    r = 0
    for n in range(len(digits)):
        r += digits[n]*10**n # 10 Basis hoch Wertigkeit = Stelligkeit
    return r

def check_rotations(digits): # damit ich mein Array von vorne bis hinten die Zahlen durchwechsle
    for i in range(1, len(digits)):
        tmp = digits[0]
        del digits[0]
        digits.append(tmp)
        n = get_number(digits)
        if not is_prime(n):
            return False
    return True

def get_rot_primes():
    for x in range(2, 1000000):
        if is_prime(x):
            digits = get_digits(x)
            if check_rotations(digits):
                print(x)

get_rot_primes()
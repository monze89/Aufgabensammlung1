import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n//2+1):
        if n % i == 0:
            return False
    return True

def is_proth_opt(n):

    if n < 2:
         return False

    n = n-1
    i = 0 # count

    while n > 0 and n % 2 == 0:
          n //= 2
          i += 1
    if n < 2**i:
        return True
    else:
         return False

for n in range(100):
     if is_proth_opt(n):
          print(n) 

def is_proth(number):
    for n in range(1, int(math.log2(number))+2):
        for k in range(1, 2**n, 2): # step funktion: , 2 da überspringen wir jede zweite zahl, daher ungerade
            tmp = k*2**n+1
            if tmp == number:
                return True
    return False

for n in range (1, 100):
    if is_proth(n):
        print(n)

def P(n, m):
    summe = 0
    for x in range(n, m+1):
        if is_prime(x) and is_proth(x):
            summe += x
    return summe

print(P(1, 1000))
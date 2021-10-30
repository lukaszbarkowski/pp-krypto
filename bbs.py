import sympy
import random


def next_usable_prime(x):
    p = sympy.nextprime(x)
    while p % 4 != 3:
        p = sympy.nextprime(p)
    return p


def bbs(outputLength, seed):
    if seed is None:
        seed = random.randint(1, 1e10)

    x = 3 * 10 ** 10
    y = 4 * 10 ** 10

    bits = ""

    p = next_usable_prime(x)
    q = next_usable_prime(y)
    M = p * q

    x = seed

    for _ in range(outputLength):
        x = x * x % M
        b = x % 2
        bits += str(b)

    return seed, bits

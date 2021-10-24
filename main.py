import sympy
import random
import sys
from longestSeries import getLongestSeries
from series import getSeries
from poker import getPoker

x = 3*10**10    
y = 4*10**10    

seed = random.randint(1,1e10)

def next_usable_prime(x):
        p = sympy.nextprime(x)
        while (p % 4 != 3):
            p = sympy.nextprime(p)
        return p

p = next_usable_prime(x)
q = next_usable_prime(y)
M = p*q

N = 20000

x = seed

bits = ""
for _ in range(N):
    x = x*x % M
    b = x % 2
    bits += str(b)
print(bits)

# test pojedynczych bitów
print("Test pojedynczych bitów:\n")
print("Zera:",bits.count("0"))
print("Jedynki:",bits.count("1"))

getSeries(bits)
getPoker(bits)

print("Najdluzsza seria:", getLongestSeries(bits))

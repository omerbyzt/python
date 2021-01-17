"""
13195’in asal çarpanları 5, 7, 13 ve 29’dur.

600851475143 sayısının en büyük asal çarpanı kaçtır?
#6857
"""
import math


def prime_check(x):
    is_prime = True

    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            is_prime = False
            continue
    return is_prime


biggest_prime_number = -1
number = 600851475143

for i in range(2, int(math.sqrt(number)) + 1):
    if number % i == 0 and prime_check(i):
        biggest_prime_number = i

print(biggest_prime_number)

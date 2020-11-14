"""
Count the number of prime numbers less than a non-negative number, n.
"""

import math

def countPrimes(n):
    if n<2:
        return 0

    isPrime = [True] * n
    isPrime[0] = isPrime[1] = False

    for i in range(2, int(math.ceil(math.sqrt(n)))):
        if isPrime[i]:
            for multiplesOfI in range(i*i, n, i):
                isPrime[multiplesOfI] = False

    return sum(isPrime)


if __name__ == '__main__':

    print("*")
    print(countPrimes(25))
    print("*")
    print(countPrimes2(10))
    print("*")

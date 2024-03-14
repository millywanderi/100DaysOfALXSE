#!/usr/bin/python3
"""
Python program to print all primes smaller than or equal to n using
Sieve of Eratosthenes
"""


def SieveOfErasthenes(n):
    """
    First step is to create a boolean array
    Then prime[0..n] and initialize all entries
    A value in prime[i] will finally be false if i is not a prime,
    else true
    """
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        # if prime[p] is not changed, then it is a prime
        if (prime[p] == True):
            # update all multiples of p
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1

    # Print all prime numbers
    for p in range(2, n+1):
        if prime[p]:
            print(p)


# Driver code
if __name__ == '__main__':
    n = 20
    print("Following are the prime numbers smaller"),
    print("than or equal to", n)
    SieveOfEratosthenes(n)

#!/usr/bin/env python3

# utils.py

"""
Module that holds helper functions.
"""

import math
import string

SYMBOLS = string.printable

def findModInverse(a, m):
    """
    Returns the modular inverse of a % m, the number x such that a*x % m = 1
    This is a function from InventWithPython.
    :param a: int to find modular inverse of.
    :param m: int to modular by
    :return: int if inverse is found or None if no inverse is there
    """
    if math.gcd(a, m) != 1:
        return None # no mod inverse exists if a & m aren't relatively prime
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3 # // is the integer division operator
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m

if __name__ == '__main__':
    # tests
    for i in range(1000):
        print("Mod Inverse of {0} is {1}".format(i, findModInverse(i, len(SYMBOLS))))
    print("Working symbols are....\n{}".format(SYMBOLS))


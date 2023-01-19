# Write a python program to calculate permutations & combinations (using & w/o using
# library)

# Here is a Python program that calculates permutations and combinations using the math library
import math

def permutations(n, k):
    return math.perm(n, k)

def combinations(n, k):
    return math.comb(n, k)

n = 5
k = 2
print("Permutations of", n, "and", k, ":", permutations(n, k))
print("Combinations of", n, "and", k, ":", combinations(n, k))




# Here is a Python program that calculates permutations and combinations without using the math library
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def permutations(n, r):
    return factorial(n) / factorial(n-r)

def combinations(n, r):
    return factorial(n) / (factorial(r) * factorial(n-r))

# Example usage
n = 5
r = 2
print("Permutations of", n, "and", r, ":", permutations(n, r))
print("Combinations of", n, "and", r, ":", combinations(n, r))
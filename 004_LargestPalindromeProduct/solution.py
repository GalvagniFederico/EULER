import math

# A palindromic number reads the same both ways.
# Find the largest palindrome made from the product of two 3-digit numbers.

def isPalindrome(n):
    n = str(n)
    for i in range(math.floor(len(n)/2)):
        if n[i] != n[len(n)-i-1]:
            return False
    return True

def LargestPalindromeProduct(digits):
    digits = 10**digits
    max = 0
    for i in range(digits, 0, -1):
        for j in range(digits, 0, -1):
            if isPalindrome(i*j):
                if max < i*j:
                    max = i*j
    return max

print(LargestPalindromeProduct(3))

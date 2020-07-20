# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def find_palindromic():
    for i in range(999, 99, -1):
        for j in range(999, 99, -1):
            num = i * j
            str1 = str(num)
            str2 = str(num)[::-1]
            if str1 == str2:
                return (num, i, j) # num is the palindrome, i and j are the two 3-digit factors

print(find_palindromic())
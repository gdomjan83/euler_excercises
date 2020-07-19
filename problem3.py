# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
def largest_prime_factor(n):
    x = 2
    while x < n:
        if n % x == 0:
            n //= x
        else:
            x += 1
    print(n)
    

largest_prime_factor(13195)



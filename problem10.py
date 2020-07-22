# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million. If it takes too long to compute this, find the sum below 1000


def prime_sum():
    primes = [2, 3, 5, 7]
    number = 8
    while True:
        is_prime = True
        for num in primes:
            if number % num == 0:
                number += 1
                is_prime = False
                break
        if is_prime:
            primes.append(number)
            if primes[-1] >= 1000:
                total = 0
                for x in primes[:-1]:
                    total += x
                return total
            number += 1
        
print(prime_sum())
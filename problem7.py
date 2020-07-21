# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?
def prime_in_position():
    n = int(input("Which prime do you want to know? "))
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
            if len(primes) == n:
                 return number
            number += 1
        
print(prime_in_position())

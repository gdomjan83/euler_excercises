# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def found_smallest(n):
    x = n
    found = False
    while not found: 
        found = True   
        for number in range(n, n - 10, -1):
            if x % number != 0:
                x += n
                found = False
                break            
    return x

print(found_smallest(20))


# The sum of the squares of the first ten natural numbers is, 1 ** 2 + 2** 2 + ... + 10 ** 2 = 385
# The square of the sum of the first ten natural numbers is,(1+2+...+10) ** 2 = 55 ** 2 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025−385=2640
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
def square_difference(n):
    x = 0
    y = 0
    for number in range(1, n + 1):
        x += number ** 2
        y += number
    return (y ** 2 - x)

print(square_difference(100))
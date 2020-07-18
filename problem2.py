# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
total = 0
first = 1
second = 2
result = [1, 2]
while result[-1] <= 4000000:
    result.append(first + second)
    first, second = second, first + second
result.pop()

for item in result:
    if item % 2 == 0:
        total += item

print(total)
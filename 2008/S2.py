from math import floor
from math import sqrt

r = int(input())

while r != 0:
    pennies = 0
    for x in range(-r, r + 1):
        pennies += 2 * floor(sqrt(r ** 2 - x ** 2))
    pennies += 2 * r + 1
    print(pennies)
    r = int(input())

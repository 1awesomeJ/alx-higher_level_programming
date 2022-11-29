#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    k = number % 10
elif number < 0:
    k = number % -10

if k > 5:
    print(f"Last digit of {number:d} is {k:d} and is greater than 5")
elif k == 0:
    print(f"Last digit of {number:d} is {k:d} and is 0")
else:
    print(f"Last digit of {number:d} is {k:d} and is less than 6 and not 0")

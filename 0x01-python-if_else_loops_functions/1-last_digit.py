#!/usr/bin/python3

import random
number = random.randint(-10000, 10000)
lastd = abs(number) % 10

if number < 0:
    lastd = (abs(number) % 10) * -1  #abs returns absolute value of a number
else:
    lastd = number % 10

print("Last digit of {} is {} ".format(number, lastd), end="")
if lastd > 5:
    print("and is greater than 5")
if lastd == 0:
    print("and is 0")
elif lastd < 6 and lastd != 0:
    print("and is less than 6 and not 0")

#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastd = abs(number) % 10
print("Last digit of {} is {} ".format(number, lastd))
if lastd > 5:
    print("and is greateer than 5")
if lastd == 0:
    print("and is 0")
elif lastd < 6 and lastd != 0:
    print("and is less than 6 and not 0")

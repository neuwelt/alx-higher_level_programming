#!/usr/bin/python3

def print_last_digit(number):
    if number < 0:
        dig = (abs(number) % 10) * -1
    else:
        dig = number % 10
    print(dig)

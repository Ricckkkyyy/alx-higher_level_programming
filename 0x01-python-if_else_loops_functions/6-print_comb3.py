#!/usr/bin/python3
for tens_digit in range(10):
    for ones_digit in range(tens_digit + 1, 10):
        if tens_digit == 8:
            print(f"{tens_digit}{ones_digit}")
        else:
            print(f"{tens_digit}{ones_digit}", end=", ")

#!/usr/bin/python3
for tens_digit in range(0, 9):
    for ones_digit in range(tens_digit + 1, 10):
        if tens_digit == 8:
            print("{}{}".format(tens_digit, ones_digit))
        else:
            print("{}{}".format(tens_digit, ones_digit), end=", ")

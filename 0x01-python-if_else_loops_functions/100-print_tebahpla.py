#!/usr/bin/python3

def reverse():
    for i in range (122,98,-1):
        print(chr(i) if  i % 2 == 0 else  chr(i-32), end='')
reverse()

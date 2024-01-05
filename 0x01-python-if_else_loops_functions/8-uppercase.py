#!/usr/bin/python3

def uppercase(str):
    for char in str:
        if ord(char) >= ord('a') and ord('z') <= ord(char):
            upper_char = chr(ord(char) - ord('a') + ord('A'))
            print("{}".format(upper_char, end="")
        else:
            print("{}".format(char), end="")

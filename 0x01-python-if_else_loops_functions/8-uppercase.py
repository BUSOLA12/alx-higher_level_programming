#!/usr/bin/python3

def uppercase(str):
    for char in str:
        if char >= 'a' and 'z' <= char:
            print("{}".format(chr(ord(char) - ord('a') + ord('A'))), end="")
        else:
            print("{}".format(char), end="")

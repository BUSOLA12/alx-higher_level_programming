#!/usr/bin/python3
"""print the lowercase alphabets in string format"""
for l_alp in range(ord('a'), ord('z') + 1):
    print("{}".format(chr(l_alp)), end="")

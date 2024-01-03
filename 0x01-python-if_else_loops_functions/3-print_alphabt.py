#!/usr/bin/python3
"""print lowercase alphabets except q and e"""
for alp in range(ord('a'), ord('z') + 1):
    if chr(alp) not in {'q', 'e'}:
        print("{}".format(chr(alp)), end="")

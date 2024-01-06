#!/usr/bin/python3

if __name__ == "__main__":

    import sys

    result = 0
    num = len(sys.argv)
    for i in range(num - 1):
        result += int(sys.argv[i + 1])
    print("{}".format(result))

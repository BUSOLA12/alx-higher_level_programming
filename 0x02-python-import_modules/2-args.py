#!/usr/bin/python3

if __name__ == "__main__":

    argv_len = len(argv)

    if argv_len == 0:
        print("{} arguments.".format(argv_len))
    else:
        print("{} argument:".format(argv_len))

    for i in range(1, argv_len + 1)
        print("{}: {}".format(i, argv[i]))

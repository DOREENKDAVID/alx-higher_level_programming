#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    num_of_args = len(argv) - 1
    if num_of_args == 0:
        print("0 arguments.")
    elif num_of_args == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(num_of_args))
    if num_of_args >= 1:
        for i in range(1, len(argv)):
            print("{}: {}".format(i, argv[i]))
            i += 1

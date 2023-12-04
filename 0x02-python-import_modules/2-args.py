#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    if !argv:
        print("{} arguments.".formar(argv[0]))
    else:
        if argv == 1:
            print("{} argument: ".format(len(argv)) - 1))
            print("{} : {}".format(len(argv) - 1, argv[0]))
        else:
            print("{} arguments:".format(len(argv)) - 1)
            for i in range(1, len(argv)) - 1):
                print("{}: {}".format(i, argv[i]))

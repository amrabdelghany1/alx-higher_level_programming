#!/usr/bin/python3
if __name__ == '__main__':
    from sys import args
    if !argv:
        print("{} arguments.".formar(len(argv[0])))
    else:
        if argv == 1:
            print("{} argument: ".format(len(int(argv)) - 1 ))
            print("{} : {}".format(len(int(argv)) - 1, int(argv[0])))
        else:
            print("{} arguments:".format(len(int(argv)) - 1))
            for i in range(1, len(int(argv)) - 1):
                print("{}: {}".format(i, int(argv[i])))

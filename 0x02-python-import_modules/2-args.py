#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    argc = len(sys.argv) - 1
    if argc == 0:
        print("0 arguments.")
    elif:
        if argc == 1:
            print("{} argument:".format(len(sys.argv) - 1))
                    print("{}: {}".format(len(sys.argv) - 1, argv[1]))
        else:
            print("{} arguments:".format(len(sys.argv[1:])))
            for i in range(1, len(sys.argv[1:]))):
                print("{}: {}".format(i,sys.argv[i]))

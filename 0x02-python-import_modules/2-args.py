#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    argc = len(sys.argv) - 1
    if argc == 0:
        print("0 arguments.")
    elif:
        if argc == 1:
            print("{} argument:".format(argc))
            print("{}: {}".format(argc, sys.argv[1]))
        else:
            print("{} arguments:".format(argc))
            for i in range(argc + 1):
                print("{}: {}".format(i + 1, sys.argv[i + 1]))

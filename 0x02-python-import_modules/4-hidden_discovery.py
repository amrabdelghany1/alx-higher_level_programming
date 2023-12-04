#!/usr/bin/python3
if __name__ == '__main__':
    import py_compile
    import code
    import hidden_4

    for name in dir(hidden_4):
        if not name.startswith('__'):
            print(name)

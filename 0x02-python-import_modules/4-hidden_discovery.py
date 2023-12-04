#!/usr/bin/python3
if __name__ == '__main__':
    import py_compile
    import code

    compiled = __import__('hidden_4')
    for name in sorted(module_names):
        if not name.startswith('__'):
            print(name)

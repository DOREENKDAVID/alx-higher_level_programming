#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4

    for name in dir(hidden_4):
        if name[1] == '_':
            continue
        else:
            print(name)
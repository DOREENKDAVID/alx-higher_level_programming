#!/usr/in/python3
def uppercase(str):
    for letter in str:
        if ord(letter) >= ord('a') and ord(letter) <= ord('z'):
            char = chr(ord(letter) - 32)
        else:
            char = letter
        print(f"{char}", end="")
    print("")

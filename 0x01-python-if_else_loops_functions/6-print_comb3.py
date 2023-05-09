#!/usr/bin/python3

for num1 in range(0, 9):
    for num2 in range(num1 + 1, 10):
        if num1 != 8:
            print(f"{num1}{num2}", end=", ")
        else:
            print(f"{num1}{num2}")

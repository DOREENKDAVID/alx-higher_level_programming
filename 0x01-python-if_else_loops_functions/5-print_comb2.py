#!/usr/bin/python3

for num in range(0, 100):
    if num == 99:
        print(num)
    else:
        print(f"{num:0>2d}", end=", ")    

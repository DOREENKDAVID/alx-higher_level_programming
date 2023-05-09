#!/usr/bin/python3
"""prints numbers from 0 to 99"""

for num in range(0, 100):
    if num == 99:
        print(num)
    else:
        print(f"{num:0>2d}", end=", ")    

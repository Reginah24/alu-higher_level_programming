#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        if i < j:
            print("{:02d}, {:02d}".format(i, j), end="")
print()

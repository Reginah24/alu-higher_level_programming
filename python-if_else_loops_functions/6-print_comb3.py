#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        if i < j:
            print("{:02d}".format(i) + ", " + "{:02d}".format(j), end="")
print()
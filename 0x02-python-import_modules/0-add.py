#!/usr/bin/python3
from add_0 import add

if __name__ == "__main__":
    """
    Prints the result of the addition between two numbers

    """
    x = 1
    y = 2
    print("{:d} + {:d} = {:d}".format(x, y, add(x, y)))


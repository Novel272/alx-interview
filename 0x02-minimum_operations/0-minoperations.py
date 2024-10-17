#!/usr/bin/python3

"""
    Method tht determis number of minmm operatins give n characters
"""


def minOperations(n):
    """
        function that calclates fewest number of opertions
        neede giv result of exacty n charaters in a file
        args: n: Number of character to be displayed
        return:
               number min operations
    """

    now = 1
    start = 0
    counter = 0
    while now < n:
        remainder = n - now
        if (remainder % now == 0):
            start = now
            now += start
            counter += 2
        else:
            now += start
            counter += 1
    return counter

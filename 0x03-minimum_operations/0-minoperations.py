#!/usr/bin/python3
"""
0x03. Minimum Operations
"""


def minOperations(n):
    process = 0
    aggregate = 1
    copypaste = 0

    while (aggregate < n):
        if (n % aggregate == 0):
            process += 2
            copypaste = aggregate
        else:
            process += 1

        aggregate = copypaste + aggregate

    return process

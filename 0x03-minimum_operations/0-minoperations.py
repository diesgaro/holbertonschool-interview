#!/usr/bin/python3
"""
0x03. Minimum Operations
"""


def minOperations(n):
    process = 0
    aggregate = 1

    while (aggregate < n):
        if (n % aggregate == 0):
            # print('copia y pega')
            process += 2
        else:
            # print('pega')
            process += 1

        aggregate += aggregate
    return process

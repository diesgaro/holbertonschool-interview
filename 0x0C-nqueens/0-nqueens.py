#!/usr/bin/python3
import sys
"""
0. N queens
"""


def nqueens(n):
    """
        Function that solve the N queens problem:
        https://en.wikipedia.org/wiki/Queen_%28chess%29
    """
    data = []
    result = []
    rec_nqueens(n, [], [], [], data)
    for row in data:
        for i, col in enumerate(row):
            coord = [i, col]
            result.append(coord)
        print(result)
        result = []


def rec_nqueens(n, queens, cord_dif, cord_sum, data):
    """
        Recursion function that find every posible solution
    """
    p = len(queens)

    if p == n:
        data.append(queens)
        return None

    for q in range(n):
        if q not in queens and p-q not in cord_dif and p+q not in cord_sum:
            rec_nqueens(
                n,
                queens + [q],
                cord_dif + [p - q],
                cord_sum + [p + q],
                data
            )


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    try:
        n = int(sys.argv[1])
    except TypeError:
        print("N must be a number")
        exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        exit(1)

    nqueens(n)

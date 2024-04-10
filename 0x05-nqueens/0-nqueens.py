#!/usr/bin/python3
"""
    Solve the N Queens Problem
    (See README for instruction)
"""

from sys import argv


def nQueens(n: int) -> None:
    """
        Finds all possible ways to place n queens on an
        n x n board without them attacking each other
    """
    board = []
    usedCols = set()
    nDiagonals = set()
    pDiagonals = set()

    def backtrack(row: int) -> None:
        """Prints all possible solution"""
        if row == n:
            print(board)
            return

        for col in range(n):
            if col in usedCols or col - row in nDiagonals\
                    or col + row in pDiagonals:
                continue
            usedCols.add(col)
            nDiagonals.add(col - row)
            pDiagonals.add(col + row)
            board.append([row, col])

            backtrack(row + 1)

            usedCols.remove(col)
            nDiagonals.remove(col - row)
            pDiagonals.remove(col + row)
            board.remove([row, col])

    backtrack(0)

    # for row in board:
    #     print(row)


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    try:
        N = int(argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)

    if N < 4:
        print("N must be at least 4")
        exit(1)

    nQueens(N)

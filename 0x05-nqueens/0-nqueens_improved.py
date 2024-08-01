#!/usr/bin/python3
'''
    The N-Queens Challenge
    more explanation in the documentation:
        `README.md` file
'''

import sys

def solve_nqueens(n):
    def backtrack(row, columns, diagonals1, diagonals2, solution):
        """Recursively attempt to place queens on the board"""
        if row == n:
            # If all queens are placed, add the solution
            solutions.append(solution[:])
            return

        for col in range(n):
            # Check if the column or diagonals are already attacked
            if col in columns or (row - col) in diagonals1 or (row + col) in diagonals2:
                continue

            # Place the queen
            columns.add(col)
            diagonals1.add(row - col)
            diagonals2.add(row + col)
            solution.append([row, col])

            # Recurse to the next row
            backtrack(row + 1, columns, diagonals1, diagonals2, solution)

            # Remove the queen (backtrack)
            columns.remove(col)
            diagonals1.remove(row - col)
            diagonals2.remove(row + col)
            solution.pop()

    solutions = []
    # Sets for columns and diagonals under attack
    columns = set()
    diagonals1 = set()  # Row - Column
    diagonals2 = set()  # Row + Column

    backtrack(0, columns, diagonals1, diagonals2, [])
    return solutions

if __name__ == '__main__':
    # Check if the script is being run directly
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print('N must be a number')
        sys.exit(1)

    if n < 4:
        print('N must be at least 4')
        sys.exit(1)

    solutions = solve_nqueens(n)

    for idx, val in enumerate(solutions):
        if idx == len(solutions) - 1:
            print(val, end='')
        else:
            print(val)

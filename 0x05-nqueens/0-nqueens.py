#!/usr/bin/python3
# Shebang line to indicate that this script should be executed using Python 3

'''
    The N-Queens Challenge
'''
# A docstring providing a brief description of the script's purpose

import sys
# Import the sys module to access command-line arguments and exit the program


if __name__ == '__main__':
    # Check if the script is being run directly (not imported as a module)
    ''' validate number of args '''
    # Validate the number of command-line arguments
    if len(sys.argv) != 2:
        # If there are not exactly two arguments (script name and N),
        # print usage message
        print("Usage: nqueens N")
        sys.exit(1)
        # Exit the program with status code 1 to indicate an error

    try:
        n = int(sys.argv[1])
        # Try to convert the command-line argument to an integer and
        # assign it to n
    except ValueError:
        # If conversion fails, print an error message and exit
        print('N must be a number')
        exit(1)

    if n < 4:
        # Check if the value of N is less than 4
        print('N must be at least 4')
        # Print an error message if N is less than 4
        exit(1)
        # Exit the program with status code 1

    solutions = []
    # List to store all possible solutions
    placed_queens = []  # coordinates format [row, column]
    # List to store the coordinates of placed queens on the board
    stop = False
    # Flag to indicate when to stop the backtracking process
    r = 0
    # Row index, starting from 0
    c = 0
    # Column index, starting from 0

    # iterate thru rows
    while r < n:
        # Loop through each row on the board
        goback = False
        # Flag to indicate if we need to backtrack
        # iterate thru columns
        while c < n:
            # Loop through each column in the current row
            # check if current column is safe
            safe = True
            # Assume the current position is safe for placing a queen
            for cord in placed_queens:
                # Check each previously placed queen's position
                col = cord[1]
                # Get the column index of the placed queen
                if(col == c or col + (r-cord[0]) == c or
                        col - (r-cord[0]) == c):
                    # Check for column, diagonal, and anti-diagonal conflicts
                    safe = False
                    # If there's a conflict, mark as unsafe
                    break

            if not safe:
                # If the position is not safe
                if c == n - 1:
                    # If we're at the last column, set backtracking flag
                    goback = True
                    break
                c += 1  # Move to the next column
                continue

            # place queen
            cords = [r, c]
            # Store the coordinates of the placed queen
            placed_queens.append(cords)
            # Add the coordinates to the list of placed queens
            # if last row, append solution and reset all to last unfinished row
            # and last safe column in that row
            if r == n - 1:
                # If we've reached the last row
                solutions.append(placed_queens[:])
                # Add the current solution to the list of solutions (deep copy)
                for cord in placed_queens:
                    # Iterate through placed queens to find backtrack position
                    if cord[1] < n - 1:
                        # If the column index is not the last column
                        r = cord[0]
                        # Set row index for backtracking
                        c = cord[1]
                        # Set column index for backtracking
                for i in range(n - r):
                    # Remove queens from incomplete rows
                    placed_queens.pop()
                if r == n - 1 and c == n - 1:
                    # If we backtrack to the last queen, reset everything
                    placed_queens = []
                    stop = True
                r -= 1
                # Move back one row
                c += 1
                # Move to the next column
            else:
                c = 0
                # Reset column index to start from the beginning in
                # the next row
            break
        if stop:
            # If stop flag is set, break out of the loop
            break
        # on fail: go back to previous row
        # and continue from last safe column + 1
        if goback:
            # If we need to backtrack
            r -= 1  # Move back one row
            while r >= 0:
                # Loop until a row is found to backtrack
                c = placed_queens[r][1] + 1
                # Set column to last placed column + 1
                del placed_queens[r]  # Remove the last placed queen
                if c < n:
                    # If the column is within bounds, break out
                    break
                r -= 1  # Move back another row
            if r < 0:
                # If we've backtracked beyond the first row, stop
                break
            continue
        r += 1  # Move to the next row

    for idx, val in enumerate(solutions):
        # Loop through each solution
        if idx == len(solutions) - 1:
            # If this is the last solution, print without newline
            print(val, end='')
        else:
            print(val)  # Print each solution with a newline

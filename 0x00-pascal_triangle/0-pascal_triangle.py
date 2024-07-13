#!/usr/bin/python3
'''
    Module 0-pascal_triangle
'''


def pascal_triangle(n):
    '''
        Returns pascal's trangle(list of lists of integers)
        or an empty list if n <= 0
    '''
    if n <= 0:  # validates the value of n
        return []

    # initialize triangle with a single row [1]
    triangle = [[1]]

    # Loop hrough to generate the rows
    while len(triangle) != n:
        # get the last row
        last_row = triangle[-1]
        # Create a new row with the first value = 1
        new_row = [1]
        # Compute the immediate elements of the new row
        for count in range(len(last_row) - 1):
            # using two consecutive elements from the last row
            # to compute new immediate element for the new row
            new_row.append(last_row[count] + last_row[count + 1])
        # add / appeend 1 to the end of the new row
        new_row.append(1)
        # add / append new row to triangle
        triangle.append(new_row)
    # return trinagle
    return triangle

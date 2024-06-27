#!/usr/bin/python3
'''
    Module 0-pascal_triangle
'''


def pascal_triangle(n):
    '''
        Returns pascal's trangle(list of lists of integers)
        or an empty list if n <= 0
    '''
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        trngl = triangles[-1]
        tmp = [1]
        for i in range(len(trngl) - 1):
            tmp.append(trngl[i] + trngl[i + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles

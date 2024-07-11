#!/usr/bin/python3


'''
    mini operation
'''

def minOperations(n):
    '''def minOperation'''
    Ope = 0
    minope = 2
    while n > 1:
        while n % minope == 0:
            Ope += minope
            n /= minope
        minope += 1
    return Ope

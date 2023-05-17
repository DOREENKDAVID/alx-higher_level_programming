#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in range(len(matrix)):
        new_matrix.append([element ** 2 for element in matrix[row]])
    return new_matrix

#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [[]]
    for i in len(matrix):
        for j in len(matrix[i]):
            new_matrix[i][j] = matrix[i][j] ** 2
    return new_matrix

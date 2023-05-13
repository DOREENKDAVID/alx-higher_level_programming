#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    num_of_elem = len(matrix[0])
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if j < num_of_elem -1:
                print("{:d}".format(matrix[i][j]), end=" ")
            else:
                print("{:d}".format(matrix[i][j]), end="")
    print()

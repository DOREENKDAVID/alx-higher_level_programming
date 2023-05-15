#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    num_of_elem = len(matrix[0])
    for row in range(len(matrix)):
        for column in range(len(matrix[0])):
            if column < num_of_elem - 1:
                print("{:d}".format(matrix[row][column]), end=" ")
            else:
                print("{:d}".format(matrix[row][column]), end="")
        print()

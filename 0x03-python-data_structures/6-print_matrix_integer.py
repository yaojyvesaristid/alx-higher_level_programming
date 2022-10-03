#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix) > 0:
        count = 0
        for i in matrix:
            for j in i:
                count += 1
                if count % 3 == 0:
                    print("{:d}".format(j), end='')
                else:
                    print("{:d}".format(j), end=' ')
            print()

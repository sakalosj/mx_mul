#!/usr/bin/python3
from matrix import Matrix


def read_mx_dimensions() -> (int, int):
    """
    Reads dimensions from input and checks if its int.

    Returns:
        (int, int)

    """
    val = input('width:')
    width = int(val)
    val = input('height:')
    height = int(val)
    return height, width


def read_mx_data(height, width) -> list:
    """
    Reads matrix data from input based on provided dimensions.

    Args:
        height: matrix rows
        width: matrix columns

    Returns:
        [][]

    """
    mx = []
    for _ in range(height):
        row_raw = input()
        row = [int(val) for val in filter(None, row_raw.split(' '))]
        if len(row) != width:
            raise ValueError('Incorrect number of values')
        mx.append(row)
    return mx


def read_input():
    """
    Using read_mx_dimensions and read_mx_data reads data and constructs matrices.
    Also checks if matrices have valid dimensions for multiplication

    Returns:
        (Matrix, Matrix)

    """
    print('Matrix A')
    mx_a_height, mx_a_width = read_mx_dimensions()

    print('\nMatrix B')
    mx_b_height, mx_b_width  = read_mx_dimensions()
    if mx_a_width != mx_b_height:
        raise ValueError('Matrices have to have mXn nXp dimensions')

    print('\nMatrix A values:')
    mx_a = read_mx_data(mx_a_height, mx_a_width)
    print('Matrix B values:')
    mx_b = read_mx_data(mx_b_height, mx_b_width)

    return Matrix(mx_a), Matrix(mx_b)


if __name__ == '__main__':
    mx_a, mx_b = read_input()
    print(mx_a.multiply(mx_b).list2d)

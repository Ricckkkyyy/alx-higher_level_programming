#!/usr/bin/python3
"""Defines a matrix division function."""

def matrix_divided(matrix, div)
    """
     Divides all elements of a matrix by a divisor and rounds the results to 2 decimal places.
     Parameters: 
        matrix (list of lists of int/float): The matrix to be divided.
        div (int/float): The divisor
    Returns:
        list of lists of float: A new matrix with all elements divided by div.
    Raises:
        TypeError: If matrix is not a list of lists of integers/floats, if rows are not of the same size,
                   or if div is not a number.
        ZeroDivisionError: If div is zero.
    """
    #Check if div is a number and is not zero
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    # Check if matrix is a list of lists of integers or floats
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if any(not all(isinstance(elem, (int, float)) for elem in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    # Check if all rows in the matrix are of the same size
    row_length = len(matrix[0])
    if any(len(row) != row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    # Create a new matrix with divided values rounded to 2 decimal places
    new_matrix = [[round(elem / div, 2) for elem in row] for row in matrix]
    return new_matrix
    

"""
Exercise: Row-wise Array Addition

Write a function add_to_rows that takes two arguments: (1) a 2D numpy array and
(2) 1D array with the same length as the number of rows in the matrix.

The function should add each element from the 1D array to all elements
in the corresponding row of the matrix.

Example:
    matrix = np.array([[1, 2, 3], 
                      [4, 5, 6]])
    row_values = np.array([1, 2])
    
    result = add_to_rows(matrix, row_values)
    # Should return: [[2, 3, 4], 
    #                 [6, 7, 8]]

Your function should:
    - Validate input dimensions are compatible - ie. the number of rows in the matrix should be the same as the number of elements in the row_values array
    - Raise provided InvalidDimensionError if dimensions are incompatible (as defined above)
    - Use broadcasting to add the row_values to the matrix
"""

import numpy as np

# define custom error type
class InvalidDimensionError(Exception):
    pass

def add_to_rows(matrix, row_values):
    """
    Add values to each row of a matrix using broadcasting.

    Parameters
    ----------
    matrix : np.ndarray
        2D array to add values to
    row_values : np.ndarray
        1D array of values to add to each row. Must have same length as 
        number of rows in matrix

    Returns
    -------
    np.ndarray
        New array with row_values added to each row of matrix

    Raises
    ------
    InvalidDimensionError
        If length of row_values does not match number of rows in matrix
    """
    
    # Your code here!
    pass
    
if __name__ == "__main__":
    # Example usage
    matrix = np.array([[1, 2, 3], 
                      [4, 5, 6]])
    
    row_values = np.array([1, 2])
    
    result = add_to_rows(matrix, row_values)

    # the result should be [[2, 3, 4], [6, 7, 8]]
    print(result)
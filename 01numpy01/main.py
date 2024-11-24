"""
NumPy Array Reshaping Exercise

Write a function, `reshape_array`, that takes a 1D NumPy array as input and:
1. Reshapes it to have dimensions `(5, 2, X)`, where `X` is inferred or calculated.
2. Returns a tuple containing:
    - The reshaped array.
    - The size of the third dimension, `X`.
    
You may use any valid method to reshape the array, such as manual calculation or letting NumPy infer the size.

If the input array size is not compatible with the desired shape, raise an `InvalidShapeError`, defined as a custom error type, below.

"""
import numpy as np

# define custom error type
class InvalidShapeError(Exception):
    pass

def reshape_array(arr):
    """
    Reshape a 1D NumPy array to dimensions (5, 2, X) and return the reshaped array 
    and the size of the third dimension.

    Parameters:
        arr (numpy.ndarray): Input 1D array.

    Returns:
        tuple: A tuple containing:
            - reshaped_array (numpy.ndarray): The reshaped array.
            - third_dimension_size (int): The size of the third dimension.

    Raises:
        ValueError: If the array size is not compatible with the desired shape.
    """

    # Your code here!
    pass

if __name__ == "__main__":
    # Example usage
    arr = np.random.random(50)
    reshaped_array, third_dim = reshape_array(arr)

    # Print results for verification
    print("Reshaped Array Shape:", reshaped_array.shape)
    print("Third Dimension Size:", third_dim)

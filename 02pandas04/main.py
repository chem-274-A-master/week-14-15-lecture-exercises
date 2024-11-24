"""
In this exercise, you will perform an operation on a dataframe using two different methods.

The Lecture videos cover using the apply method to perform operations on a dataframe.
While this works, pandas methods should always be used if available because they are optimized for performance.

In this exercise, you will compare the performance of two methods for rounding all the values in a dataframe.
Fill in the two methods below. A performance comparison is done in the main block.
"""
import os

import pandas as pd
import timeit

# Method 1: Using a pandas dataframe method
def round_method(df):
    
    # use a dataframe method to round all values.
    # Your line of code should be df.SOMETHING() 
    # where SOMETHING is a pandas method that performs the operation.
    
    rounded_df = # your code here
    
    return rounded_df

# Method 2: Using apply
def apply_method(df):
    
    # use the apply method to round all values.
    # apply the built-in round function.
    
    rounded_df = # your code here

    return rounded_df

if __name__ == "__main__":

    # load the data
    df = pd.read_csv("SAMPL.csv")

    # Time both methods
    round_time = timeit.timeit(lambda: round_method(df), number=1000)
    apply_time = timeit.timeit(lambda: apply_method(df), number=1000)

    print(f"df.round() time: {round_time:.4f} seconds")
    print(f"df.apply() time: {apply_time:.4f} seconds")
    print(f"df.round() is {apply_time/round_time:.2f} times faster than df.apply()")

    # Assert that the two methods give the same result
    assert round_method(df).equals(apply_method(df)), "The two methods do not give the same result."
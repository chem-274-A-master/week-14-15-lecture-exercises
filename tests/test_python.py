"""
Tests for NumPy Array Reshaping Exercise.
"""

import os
import sys
import numpy as np

import pytest

def test_01numpy01():
    # Add the exercise directory to the Python path
    exercise_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "01numpy01"))
    sys.path.append(exercise_dir)
    
    from main import reshape_array, InvalidShapeError

    # Test 1: Valid reshaping
    arr = np.random.random(50)
    reshaped_array, third_dim = reshape_array(arr)
    assert reshaped_array.shape == (5, 2, 5), "Reshaped array has incorrect shape"
    assert third_dim == 5, "Third dimension size is incorrect"

    # Test 2: Valid reshaping with a different size
    arr = np.random.random(30)
    reshaped_array, third_dim = reshape_array(arr)
    assert reshaped_array.shape == (5, 2, 3), "Reshaped array has incorrect shape"
    assert third_dim == 3, "Third dimension size is incorrect"

    # Test 3: Invalid reshaping (should raise ValueError)
    with pytest.raises(InvalidShapeError):
        arr = np.random.random(53)
        reshaped_array, third_dim = reshape_array(arr)

def test_01numpy02():
    # Add the exercise directory to the Python path
    exercise_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "01numpy02"))
    sys.path.append(exercise_dir)
    
    from main import answer

    # Manually create the expected identity matrix for n=6
    n = 6
    expected = np.zeros((n, n))
    for i in range(n):
        expected[i, i] = 1

    # Test if the answer is correct
    assert np.array_equal(answer, expected), f"Identity matrix is incorrect. Expected:\n{expected}\nGot:\n{answer}"

def test_01numpy03():
    # Add the exercise directory to the Python path
    exercise_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "01numpy03"))
    sys.path.append(exercise_dir)
    
    from main import add_to_rows, InvalidDimensionError

    # Test 1: Basic example
    matrix = np.array([[1, 2, 3], [4, 5, 6]])
    row_values = np.array([1, 2])
    result = add_to_rows(matrix, row_values)
    expected = np.array([[2, 3, 4], [6, 7, 8]])
    assert np.array_equal(result, expected), f"Failed Test 1. Expected:\n{expected}\nGot:\n{result}"

    # Test 2: Single row matrix
    matrix = np.array([[10, 20, 30]])
    row_values = np.array([5])
    result = add_to_rows(matrix, row_values)
    expected = np.array([[15, 25, 35]])
    assert np.array_equal(result, expected), f"Failed Test 2. Expected:\n{expected}\nGot:\n{result}"

    # Test 3: Invalid dimensions (mismatched row size)
    with pytest.raises(InvalidDimensionError):
        matrix = np.array([[1, 2], [3, 4]])
        row_values = np.array([1, 2, 3])  # Mismatched length
        add_to_rows(matrix, row_values)

def test_02pandas01():

    import pandas as pd

    # Add the exercise directory to the Python path
    exercise_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "02pandas01"))
    sys.path.append(exercise_dir)
    
    from main import df, expt_mean

    # Load the reference data for testing
    reference_df = pd.read_csv(os.path.join(exercise_dir,"SAMPL.csv"))

    # Test if the DataFrame was loaded correctly
    assert len(df) == len(reference_df), "DataFrame does not have the correct number of rows."
    assert list(df.columns) == list(reference_df.columns), "DataFrame does not have the correct columns."

    # Test if the mean of the 'expt' column is calculated correctly
    expected_mean = reference_df['expt'].mean()
    assert expt_mean == expected_mean, f"Mean of 'expt' is incorrect. Expected: {expected_mean}, Got: {expt_mean}"

def test_02pandas02():

    import pandas as pd

    # Add the exercise directory to the Python path
    exercise_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "02pandas02"))
    sys.path.append(exercise_dir)
    
    from main import df

    # Assert the shape of the DataFrame
    assert df.shape == (356, 2), "DataFrame has incorrect shape."

    # Assert the columns of the DataFrame
    assert list(df.columns) == ['deltaH', 'deltaG'], "DataFrame has incorrect columns."

def test_02pandas03():
    
    import pandas as pd

    # Add the exercise directory to the Python path
    exercise_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "02pandas03"))
    sys.path.append(exercise_dir)

    from main import ans

    # Load the reference data for testing
    # The reference data is saved in a CSV file in this folder
    module_path = os.path.abspath(os.path.dirname(__file__))
    reference_df = pd.read_csv(os.path.join(module_path, "ans.csv"), index_col=0)

    #breakpoint()

    # Test that reference data and the answer are the same
    assert ans.equals(reference_df), "DataFrames are not equal."

def test_02pandas04():

    import pandas as pd

    import inspect

    # Add the exercise directory to the Python path
    exercise_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "02pandas04"))
    sys.path.append(exercise_dir)

    from main import round_method, apply_method

    source1 = inspect.getsource(round_method)
    source2 = inspect.getsource(apply_method)

    assert "df.round()" in source1, "Method 1 does not use pandas method."
    assert "df.apply(" in source2, "Method 2 does not use apply method."

    # Make a small dataframe for testing
    df = pd.DataFrame({
        'A': [1.234, 2.345, 3.456],
        'B': [4.567, 5.678, 6.789]
    })

    # Test the two methods
    rounded1 = round_method(df)
    rounded2 = apply_method(df)

    # Assert that the two methods give the same result
    assert rounded1.equals(rounded2), "The two methods do not give the same result."

def test_02pandas05():
    import pandas as pd

    # Add the exercise directory to the Python path
    exercise_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "02pandas05"))
    sys.path.append(exercise_dir)

    # Import the main module
    from main import find_carbon_extremes

    # Test with molecules having same number of carbons but different SMILES representations
    df = pd.DataFrame({
       'smiles': ['c1ccccc1', 'CCCCCC', 'C', 'CC'],
       'iupac': ['benzene', 'cyclohexane', 'methane', 'ethane']
   })
    
    most_carbons, least_carbons = find_carbon_extremes(df)
   
    # benzene and cyclohexane both have 6 carbons
    # benzene should be returned since it comes first alphabetically
    assert most_carbons == 'benzene'
    
    # methane has 1 carbon, ethane has 2
    assert least_carbons == 'methane'

def test_03matplotlib01():

    import pandas as pd

    # Add the exercise directory to the Python path
    exercise_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "03matplotlib01"))
    sys.path.append(exercise_dir)

    from main import create_scatter_plot
    df = pd.DataFrame({
        'expt': [1, 2, 3],
        'calc': [1.1, 2.1, 3.1]
    })

    # Test the function with a simple example
    fig, ax = create_scatter_plot(df)
    
    assert len(ax.collections) == 1  # One scatter plot
    assert ax.get_xlabel() == 'Experimental'
    assert ax.get_ylabel() == 'Calculated'

def test_03matplotlib02():
    import pandas as pd

    # Add the exercise directory to the Python path
    exercise_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "03matplotlib02"))
    sys.path.append(exercise_dir)

    from main import create_dual_plots

    df = pd.DataFrame({
        'expt': [1, 2, 3],
        'calc': [1.1, 2.1, 3.1]
    })
    
    fig, (ax1, ax2) = create_dual_plots(df)
    
    # Test left subplot
    assert len(ax1.lines) == 1  # One line plot
    assert ax1.get_ylabel() == 'Experimental'
    
    # Test right subplot
    assert len(ax2.lines) == 1  # One line plot
    assert ax2.get_ylabel() == 'Calculated'
    




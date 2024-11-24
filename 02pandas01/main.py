"""
The SAMPL dataset contains experimental and calculated hydration free energies 
for small molecules in water. 
You have a CSV file named 'SAMPL.csv' that contains this data.

Your task is to load this data into a DataFrame and calculate the mean experimental
hydration free energy from the 'expt' column and store it in a variable named 'expt_mean'.
"""
import os

import pandas as pd

# The path of the current folder where this module is located
exercise_dir = os.path.dirname(__file__)

# Get SAMPL.csv filepath - Use this filepath to load the data
# This is necessary for testing, the filepath needs to include the folder.
csv_filepath = os.path.join(exercise_dir, "SAMPL.csv")

# load the data
df = # your code here - you need to use the csv_filepath variable for the test to pass

# calculate mean experimental value
expt_mean = # your code here
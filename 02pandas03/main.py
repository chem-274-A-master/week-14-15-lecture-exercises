"""
Load SAMPL.csv into a pandas dataframe named 'df'.
Use integer-based indexing in a single line of pandas code to get rows 50 to 59 (inclusive) from the dataframe.
Save the resulting dataframe to a variable named 'ans'.

You can access the index information in the dataframe using the .index attribute (i.e. df.index).
In your new dataframe (`ans`), get the value of the first index. 
Is it what you expected?
"""

import os
import pandas as pd

# The path of the current folder where this module is located
exercise_dir = os.path.dirname(__file__)

# Get SAMPL.csv filepath - Use this filepath to load the data
# This is necessary for testing, the filepath needs to include the folder.
csv_filepath = os.path.join(exercise_dir, "SAMPL.csv")

# load the data
df = pd.read_csv(csv_filepath)

# write your answer here
ans = # your code here
first_index = # your code here

# Keep this
print(f"First index value: {first_index}")
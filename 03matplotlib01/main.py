"""
Matplotlib exercise

Create a scatter plot using the provided data. Use the experimental values on the x-axis 
and calculated values on the y. Use the object oriented interface of matplotlib.

Label your x and y axes with 'Experimental' and 'Calculated' respectively.
"""

import matplotlib.pyplot as plt
import pandas as pd

# write this function
def create_scatter_plot(df):
   """
   Create a scatter plot of experimental vs calculated values.
   
   Parameters
   ----------
   df : pd.DataFrame
       DataFrame containing 'expt' and 'calc' columns
       
   Returns
   -------
   tuple
       (fig, ax) matplotlib figure and axes objects
   """
   
   # Your code here
   pass

if __name__ == "__main__":
   df = pd.read_csv("SAMPL.csv")
   fig, ax = create_scatter_plot(df)
   plt.show()
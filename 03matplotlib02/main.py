"""
Matplotlib exercise

Create a figure with two subplots. The subplots should have one row and two columns.

Plot the experimental values on the left subplot, and the calculated values on the right subplot. 
The x values can be a count of the index (this will happen automatically if you only specify y values for plotting).
Make sure to label the x-axis "Index" and the y-axis "Experimental" or "Calculated" as appropriate.

Write a function that takes a dataframe and creates the two plots.
"""

import matplotlib.pyplot as plt
import pandas as pd

def create_dual_plots(df):
    """
    Create two plots on one figure: experimental values and calculated values vs index.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame containing 'expt' and 'calc' columns
        
    Returns
    -------
    tuple
        (fig, (ax1, ax2)) matplotlib figure and axes objects
    """
    
    # Your code here
    pass

if __name__ == "__main__":
    df = pd.read_csv("SAMPL.csv")
    fig, (ax1, ax2) = create_dual_plots(df)
    fig.tight_layout() # This is a trick to fix overlapping text and labels
    plt.savefig("dual_plots.png")

    
"""
Pandas series (columns) that are string type have string methods available through series.str.
For example, to convert a series with string types to lowercase, you could do series.str.lower() (see example).

In this exercise, you will write a function to find the compounds with the most and least carbon atoms in a dataframe.
As we learned in lab, in SMILES strings, an uppercase 'C' represents a carbon atom, while a lowercase 'c' represents an aromatic carbon atom.
You should count both as carbon atoms.
Truly working with SMILES is a bit more complicated, but for this exercise, we will keep it simple.

Write a function that takes a dataframe containing 'smiles' and 'iupac' columns and returns:
1. The name of the compound with the most carbons (if there's a tie, pick the one that comes first alphabetically by iupac name)
2. The name of the compound with the least carbons (if there's a tie, pick the one that comes first alphabetically by iupac name)
"""

import pandas as pd

def find_carbon_extremes(df):
    """
    Find compounds with most and least carbon atoms.
    
    Parameters
    ----------
    df : pd.DataFrame
        Dataframe containing 'smiles' and 'iupac' columns
        
    Returns
    -------
    tuple
        (compound with most carbons, compound with least carbons)
        In case of ties, returns the compound that comes first alphabetically by iupac name
    """
    
    # Your code here
    pass

if __name__ == "__main__":
    df = pd.read_csv("SAMPL.csv")
    most_carbons, least_carbons = find_carbon_extremes(df)
    print(f"Compound with most carbons: {most_carbons}")
    print(f"Compound with least carbons: {least_carbons}")
import pandas as pd

def wrangling (df,year):
    filtered = df[df['Year'] == year]
    return filtered
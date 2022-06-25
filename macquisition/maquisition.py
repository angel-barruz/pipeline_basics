import pandas as pd

#acquisition methods

def acquisition(path):
    df = pd.read_csv(path)
    return df
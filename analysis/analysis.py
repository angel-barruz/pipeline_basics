import pandas as pd

# Analysys methods

def analysis(df,group,agg):
    analyzed = df.groupby(by=group)[agg].mean()
    analyzed.to_csv('../data/result.csv')
    return '-----AAA---'
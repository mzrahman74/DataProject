import pandas as pd

df = pd.read_csv('../data/corr.csv')
print(df.corr())
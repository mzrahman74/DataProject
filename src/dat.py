import pandas as pd

df = pd.read_csv('../data/train.csv')

for x in df.index:
    if df.loc[x, 'Duration'] > 120:
        df.loc[x, 'Duration'] = 120
        print(df.to_string())

print(df.duplicated())

df.drop_duplicates(inplace=True)
print(df.to_string())
import pandas as pd

df = pd.read_csv('../data/train.csv')

new_df = df.fillna(130, inplace=True)

print(new_df.to_string())

df['Date'] = pd.to_datetime(df['Date'], format= 'mixed')
print(df.to_string())

df.loc[7, 'Duration']= 45
print(df.to_string())
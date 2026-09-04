import pandas as pd


data =  {
    "calories": [420, 500, 600, 390, 380],
    "duration": [50, 40, 45, 40, 50]
}

df = pd.DataFrame(data)
print(df)
print("************************")
print(df.loc[0])
print("++++++++++++++++++++++++")
print(df.loc[[0, 1]])



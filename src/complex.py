import pandas as pd
import json

with open("../data/complex.json") as f:
    data = json.load(f)
#1
df = pd.json_normalize(data)
print(df)

#2
items_df= pd.DataFrame(data["items"])
print(items_df)

#3
items=pd.json_normalize(data["items"])
print(items)
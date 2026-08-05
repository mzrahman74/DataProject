import json

import pandas as pd

# load JSON directly into dataFrame

df = pd.read_json("../data/sample_data.json")
print(df.head())

# notice how the location column contains nested dictionaries (e.g., {'city': 'Austin', 'state': 'Tx')
# to unpack these into separate columns, use pd.json_normalize()

with open("../data/sample_data.json", 'r') as f:
    data = json.load(f)
    print(data)

#flatten nested dictionaries
df_flat = pd.json_normalize(data)
print(df_flat[["name", "department", "salary", "location.city", "location.state"]])

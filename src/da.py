import pandas as pd

df = pd.read_json('../data/data.json')

print(df.to_string())

data = {
    "Duration": {
        "0": 60,
        "1": 60,
        "2": 60,
        "3": 45,
        "4": 45,
        "5": 60,
    },
    "Pulse": {
        "0": 110,
        "1": 117,
        "2": 125,
        "3": 1109,
        "4": 125,
        "5": 102,
    },
    "Maxpulse": {
        "0": 130,
        "1": 145,
        "2": 145,
        "3": 130,
        "4": 135,
        "5": 135,
   },
   "Calories": {
       "0": 409,
       "1": 479,
       "2": 340,
       "3": 282,
       "4": 406,
       "5": 300,
   }
}
df = pd.DataFrame(data)
print(df)


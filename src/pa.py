import pandas as pd

mydataset = {
    'car': [ "BMW", "Volvo", "Ford"],
    'passings': [3, 8, 4]
}

mydataframe = pd.DataFrame(mydataset)

print(mydataframe)

calories = {"day1": 420, "day2": 420, "day3": 390, "day4": 490}

mydata = pd.Series(calories, index=['day1', 'day2'] )
print(mydata)

data = {
    "calories": [420, 300, 390],
    "duration": [50, 40, 45]
}

my_data = pd.DataFrame(data)
print(my_data)

df = pd.read_csv('../data/data.csv')
print(df.to_string())


pd.options.display.max_rows = 10
cf = pd.read_csv('../data/data.csv')
print(cf)
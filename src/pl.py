import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../data/data.csv')

df.plot(kind='scatter', x='Duration', y='Calories')
plt.show()


df.plot(kind='line', x='Duration', y='Maxpulse')
plt.show()

df["Duration"].plot(kind='hist')
plt.show()
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('QCI - Assignment2\\Assignment2\\sealevel.txt')

x = df['year']
y = df['sea_level']

plt.plot(x, y)
plt.xlabel('Year')
plt.ylabel('Sea Level')
plt.title('Sea Level Over Time')
plt.show()

print(df.head())
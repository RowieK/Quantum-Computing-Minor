import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('QCI - Assignment2\\Assignment2\\djia.txt', encoding='utf-8-sig')

# When reading this, try to comment the line under here and run the code to see what happens. 
# Then, uncomment it and run the code again to see the difference.
df['Date'] = pd.to_datetime(df['Date'])

x = df['Date']
y = df['High']

plt.plot(x, y)
plt.xlabel('Date')
plt.ylabel('High')
plt.title('DJIA High Price Over Time')
plt.show()

print(df.head())
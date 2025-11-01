import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
data = pd.read_csv('weather.csv')

# Show the first 5 rows
print("📊 Preview of Data:")
print(data.head())

# Basic statistics
print("\n📈 Summary statistics:")
print(data.describe())

# Plot temperature over time
plt.figure(figsize=(8,5))
plt.plot(data['Date'], data['Temperature'], marker='o')
plt.title('Temperature Over Time')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.grid()
plt.show()

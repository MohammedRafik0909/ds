import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample housing dataset
np.random.seed(42)
data = pd.DataFrame({
    'Price': np.random.randint(50000, 200000, size=100),
    'Area': np.random.randint(500, 2000, size=100),
    'Location': np.random.choice(['A', 'B', 'C'], size=100)
})

# Scatterplot
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Area', y='Price', data=data, hue='Location', palette='viridis')
plt.title('Scatterplot of Area vs Price with Location')
plt.xlabel('Area (sq. ft)')
plt.ylabel('Price ($)')
plt.show()

# Stacked Bar Chart
location_price = data.groupby('Location')['Price'].mean().reset_index()
location_area = data.groupby('Location')['Area'].mean().reset_index()

fig, ax = plt.subplots(figsize=(10, 6))

bar1 = ax.bar(location_price['Location'], location_price['Price'], label='Average Price', color='skyblue')
bar2 = ax.bar(location_area['Location'], location_area['Area'], bottom=location_price['Price'], label='Average Area', color='orange')

ax.set_ylabel('Values')
ax.set_title('Stacked Bar Chart of Average Price and Area by Location')
ax.legend()

plt.show()

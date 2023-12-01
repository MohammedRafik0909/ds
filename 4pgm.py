import pandas as pd

data = {
    'City': ['CityA', 'CityB', 'CityC'],
    'Temperature': [
        [25, 26, 27, 25, 24, 23, 22, 26, 28, 30, 32, 31],
        [20, 22, 21, 25, 26, 24, 23, 22, 21, 20, 19, 18],
        [30, 32, 31, 30, 28, 27, 25, 26, 28, 30, 31, 29]
    ]
}

df = pd.DataFrame(data)

mean_temperatures = df['Temperature'].apply(lambda x: sum(x) / len(x))

std_dev_temperatures = df['Temperature'].apply(lambda x: pd.Series(x).std())

temperature_ranges = df['Temperature'].apply(lambda x: max(x) - min(x))
city_highest_range = df.loc[temperature_ranges.idxmax(), 'City']

most_consistent_city = std_dev_temperatures.idxmin()

print("Mean Temperatures:")
print(mean_temperatures)

print("\nStandard Deviation of Temperatures:")
print(std_dev_temperatures)

print(f"\nCity with the Highest Temperature Range: {city_highest_range}")

print(f"\nCity with the Most Consistent Temperature: {most_consistent_city}")

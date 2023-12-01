weather_data = {
    'Sunny': 150,
    'Cloudy': 100,
    'Rainy': 80,
    'Snowy': 30,
    'Foggy': 20,
}

frequency_distribution = {}

for weather, count in weather_data.items():
    frequency_distribution[weather] = count

most_common_weather = max(frequency_distribution, key=frequency_distribution.get)

print("Frequency Distribution of Weather Conditions:")
for weather, count in frequency_distribution.items():
    print(f"{weather}: {count} times")

print(f"\nThe most common weather type is: {most_common_weather}")
1

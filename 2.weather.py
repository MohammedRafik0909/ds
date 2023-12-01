import pandas as pd
data = {
    'city': ['chennai', 'andhra', 'chennai', 'kerala', 'andhra', 'chennai'],
    'cli': ['sunny', 'foggy', 'rain', 'rain', 'foggy', 'sunny']
}
df = pd.DataFrame(data)
weather_frequency = df['cli'].value_counts()

most_common_weather = weather_frequency.idxmax()

print("Weather Frequency Distribution:")
print(weather_frequency)
print("\nThe most common weather type is:", most_common_weather)

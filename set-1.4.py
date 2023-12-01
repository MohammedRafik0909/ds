import numpy as np

# Assume you have a NumPy array named fuel_efficiency
fuel_efficiency = np.array([25, 30, 22, 28, 35, 18, 32, 26, 24, 29])

# Calculate the average fuel efficiency
average_fuel_efficiency = np.mean(fuel_efficiency)

# Choose two car models (indices in the array)
car_model1_index = 2
car_model2_index = 5

# Get the fuel efficiency of the selected car models
fuel_efficiency_car_model1 = fuel_efficiency[car_model1_index]
fuel_efficiency_car_model2 = fuel_efficiency[car_model2_index]
print(fuel_efficiency_car_model1)
# Calculate the percentage improvement
percentage_improvement = ((fuel_efficiency_car_model2 - fuel_efficiency_car_model1) / fuel_efficiency_car_model1) * 100

# Print the results
print("Average Fuel Efficiency:", average_fuel_efficiency)
print(f"Percentage Improvement from Car Model {car_model1_index} to {car_model2_index}: {percentage_improvement:.2f}%")

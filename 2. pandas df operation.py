import pandas as pd
import numpy as nm  
import matplotlib.pyplot as mtp  


# Assuming order_data is your DataFrame


data ={
    'customer_id':[1,2,1,3,1,2],
    'order_date':['2023-11-01','2023-11-02','2023-11-03','2023-11-01','2023-11-02','2023-11-03'],
    'product_name':['apple','orange','grape','apple','orange','apple'],
    'quantity':[3,4,2,1,2,3]
    }
print(type(data))
order_data = pd.DataFrame(data)

# Convert 'order_date' column to datetime type
order_data['order_date'] = pd.to_datetime(order_data['order_date'])

# Display the order_data DataFrame
print(order_data)




# 1. Total number of orders made by each customer
total_orders_per_customer = order_data.groupby('customer_id')['order_date'].count()

# 2. Average order quantity for each product
average_quantity_per_product = order_data.groupby('product_name')['quantity'].mean()

# 3. Earliest and latest order dates in the dataset
earliest_order_date = order_data['order_date'].min()
latest_order_date = order_data['order_date'].max()

# Display the results
print("Total number of orders made by each customer:")
print(total_orders_per_customer)

print("\nAverage order quantity for each product:")
print(average_quantity_per_product)

print("\nEarliest order date:", earliest_order_date)
print("Latest order date:", latest_order_date)

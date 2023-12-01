import pandas as pd

data = {'Product': ['Product_A', 'Product_B', 'Product_A', 'Product_C', 'Product_B'],
        'Price': [10.0, 20.0, 15.0, 25.0, 30.0],
        'Quantity': [2, 3, 1, 4, 2]}

sales_data = pd.DataFrame(data)
sales_data['total_cost'] = sales_data['Price']*sales_data['Quantity']

print(sales_data)

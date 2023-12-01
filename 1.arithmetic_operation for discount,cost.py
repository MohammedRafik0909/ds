item_prices = [2.5, 3.0, 1.75, 4.5]  # Prices of individual items
quantities = [3, 2, 1, 4]  # Quantities of each item
discount_rate = 10  
tax_rate = 8  
# Calculate the total cost before discounts and taxes
subtotal = sum(item_price * quantity for item_price, quantity in zip(item_prices, quantities))

# Calculate the discount amount
discount_amount = (discount_rate / 100) * subtotal

# Apply the discount
total_after_discount = subtotal - discount_amount

# Calculate the tax amount
tax_amount = (tax_rate / 100) * total_after_discount

# Calculate the final total cost
total_cost = total_after_discount + tax_amount

# Print the result
print(f"Subtotal: ${subtotal:.2f}")
print(f"Discount (-{discount_rate}%): -${discount_amount:.2f}")
print(f"Total after discount: ${total_after_discount:.2f}")
print(f"Tax (+{tax_rate}%): +${tax_amount:.2f}")
print(f"Final Total Cost: ${total_cost:.2f}")

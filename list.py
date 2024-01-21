# Product data
products = ["Sankofa Foods", "Jamestown Coffee", "Bioko Chocolate", "Blue Skies Ice Cream", "Fair Afric Chocolate", "Kawa Moka Coffee", "Aphro Spirit", "Mensado Bissap", "Voltic"]
prices = [30, 25, 40, 20, 20, 35, 45, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2, 9]

# Calculate total price average
average_price = sum(prices) / len(prices)

# Create a new price list reduced by $5
new_prices = [price - 5 for price in prices]

# Calculate total revenue
total_revenue = sum([price * customers for price, customers in zip(prices, last_week)])

# Calculate average daily revenue
average_daily_revenue = total_revenue / sum(last_week)

# Identify products with new prices less than $30
affordable_products = [product for product, price in zip(products, new_prices) if price < 30]

# Print results
print(f"Average Price: ${average_price:.2f}")
print(f"New Prices: {new_prices}")
print(f"Total Revenue: ${total_revenue:.2f}")
print(f"Average Daily Revenue: ${average_daily_revenue:.2f}")
print(f"Affordable Products: {affordable_products}")

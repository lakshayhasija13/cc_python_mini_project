# Creating Lists
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# TASK 1
total_price = 0

# TASK 2
for price in prices:
  total_price += price

# TASK 3
average_price = total_price / len(prices)

# TASK 4
print(f'Average Haircut Price: {average_price}')

# TASK 5
new_prices = [price - 5 for price in prices]

# TASK 6
print(new_prices)

# TASK 7
total_revenue = 0

# TASK 8
for i in range(0, len(hairstyles)):
  total_revenue += prices[i] * last_week[i]

# TASK 9
print(f'Total Revenue: {total_revenue}')

# TASK 10
average_daily_revenue = total_revenue / 7
print(f'Average Daily revenue: {average_daily_revenue}')

# TASK 11
cuts_under_30 = [hair for hair in range(len(hairstyles)) if new_prices[hair] < 30]

# TASK 12
print(cuts_under_30)

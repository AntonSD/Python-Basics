more_than_20kg = float(input())
weight = float(input())
days_until_travel = int(input())
count_bagages = int(input())
price = 0
if weight < 10:
    price = 0.2 * more_than_20kg
elif 10 <= weight <= 20:
    price = 0.5 * more_than_20kg
else:
    price = more_than_20kg
if days_until_travel > 30:
    price = price + 0.1 * price
elif 7 <= days_until_travel <= 30:
    price = price + 0.15 * price
elif days_until_travel < 7:
    price = price + 0.4 * price
total_price = count_bagages * price
print(f" The total price of bags is: {total_price:.2f} lv. ")
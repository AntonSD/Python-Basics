budget = float(input())
statists = int(input())
price_per_statist = float(input())

decorating = budget - 0.9 * budget
if statists > 150:
    price_per_statist *= 0.9
total_sum = decorating + statists * price_per_statist
difference = abs(budget - total_sum)
if budget >= total_sum:
    print("Action!")
    print(f"Wingard starts filming with {difference:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {difference:.2f} leva more.")
budget = float(input())
count_statists = int(input())
price_dressing_per_one = float(input())
decorating = budget * 0.1
price_dressing = price_dressing_per_one * count_statists
if count_statists > 150:
    price_dressing *= 0.9
needed_sum = decorating + price_dressing
difference = abs(needed_sum - budget)
if needed_sum > budget:
    print("Not enough money!")
    print(f"Wingard needs {difference:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {difference:.2f} leva left.")

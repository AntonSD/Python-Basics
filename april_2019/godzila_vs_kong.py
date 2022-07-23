budget = float(input())
number_statists = int(input())
dress_per_statist = float(input())
decorating = 0.1 * budget
total_dress = number_statists * dress_per_statist
if number_statists > 150:
    total_dress = 0.9 * total_dress
total_sum = decorating + total_dress
difference = abs(budget -  total_sum)
if total_sum > budget:
    print("Not enough money!")
    print(f"Wingard needs {difference:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {difference:.2f} leva left.")
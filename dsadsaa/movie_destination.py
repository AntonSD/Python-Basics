budget = float(input())
destination = input()
season = input()
number_days = int(input())
price_per_day = 0

if season == "Winter":
    if destination == "Dubai":
        price_per_day = 45000
    elif destination == "Sofia":
        price_per_day = 17000
    elif destination == "London":
        price_per_day = 24000
elif season == "Summer":
    if destination == "Dubai":
        price_per_day = 40000
    elif destination == "Sofia":
        price_per_day = 12500
    elif destination == "London":
        price_per_day = 20250
total = number_days * price_per_day
if destination == "Dubai":
    total *= 0.7
elif destination == "Sofia":
    total *= 1.25
difference = abs(budget - total)
if budget >= total:
    print(f"The budget for the movie is enough! We have {difference:.2f} leva left!")
else:
    print(f"The director needs {difference:.2f} leva more!")
budget = int(input())
season = input()
number_of_fishermen = int(input())
price = 0
if season == "Spring":
    price = 3000
elif season == "Summer" or season == "Autumn":
    price = 4200
elif season == "Winter":
    price = 2600
if number_of_fishermen <= 6:
    price *= 0.9
elif 7 < number_of_fishermen <= 11:
    price *= 0.85
elif number_of_fishermen > 12:
    price *= 0.75
if number_of_fishermen % 2 == 0 and season != "Autumn":
    price *= 0.95
difference = abs(budget - price)
if budget >= price:
    print(f"Yes! You have {difference:.2f} leva left.")
else:
    print(f"Not enough money! You need {difference:.2f} leva.")
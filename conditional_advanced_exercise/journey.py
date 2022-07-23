budget = float(input())
season = input()
price = 0
holiday = ""
destination = ""
if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        price = 0.3 * budget
        holiday = "Camp"
    elif season == "winter":
        price = 0.7 * budget
        holiday = "Hotel"
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        price = 0.4 * budget
        holiday = "Camp"
    elif season == "winter":
        price = 0.8 * budget
        holiday = "Hotel"
else:
    price = 0.9 * budget
    destination = "Europe"
    holiday = "Hotel"
print(f"Somewhere in {destination}")
print(f"{holiday} - {price:.2f}")

budget = float(input())
season = input()
clas = ""
type = ""
price = 0
if budget < 100:
    clas = "Economy class"
    if season == "Summer":
        price = 0.35 * budget
        type = "Cabrio"
    elif season == "Winter":
        price = 0.65 * budget
        type = "Jeep"
elif 100 <= budget <= 500:
    clas = "Compact class"
    if season == "Summer":
        price = 0.45 * budget
        type = "Cabrio"
    elif season == "Winter":
        price = 0.8 * budget
        type = "Jeep"
elif budget > 500 and (season == "Winter" or season == "Summer"):
    clas = "Luxury class"
    price = 0.9 * budget
    type = "Jeep"
print(f"{clas}")
print(f"{type} - {price:.2f}")
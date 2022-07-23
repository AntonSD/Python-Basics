budget = float(input())
season = input()
property_type = ""
price = 0
location = ""
if budget <= 1000:
    property_type = "Camp"
    if season == "Summer":
        location = "Alaska"
        price = 0.65 * budget
    elif season == "Winter":
        location = "Morocco"
        price = 0.45 * budget
elif 1000 < budget <= 3000:
    property_type = "Hut"
    if season == "Summer":
        location = "Alaska"
        price = 0.8 * budget
    elif season == "Winter":
        location = "Morocco"
        price = 0.60 * budget
else:
    property_type = "Hotel"
    price = 0.9 * budget
    if season == "Summer":
        location = "Alaska"
    elif season == "Winter":
        location = "Morocco"
print(f"{location} - {property_type} - {price:.2f}")

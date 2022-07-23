product = input()
city = input()
quantity = float(input())
amount = 0
if city == "Sofia":
    if product == "coffee":
        amount = 0.50
    if product == "water":
        amount = 0.80
    if product == "beer":
        amount = 1.20
    if product == "sweets":
        amount = 1.45
    if product == "peanuts":
        amount = 1.60

elif city == "Plovdiv":
    if product == "coffee":
        amount = 0.40
    if product == "water":
        amount = 0.70
    if product == "beer":
        amount = 1.15
    if product == "sweets":
        amount = 1.30
    if product == "peanuts":
        amount = 1.50

elif city == "Varna":
    if product == "coffee":
        amount = 0.45
    if product == "water":
        amount = 0.70
    if product == "beer":
        amount = 1.10
    if product == "sweets":
        amount = 1.35
    if product == "peanuts":
        amount = 1.55

sum = amount * quantity

print(sum)


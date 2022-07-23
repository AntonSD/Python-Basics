fruit = input()
day = input()
quantity = float(input())
amount = 0
if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
    if fruit == "banana":
        amount = 2.50
    elif fruit == "apple":
        amount = 1.20
    elif fruit == "orange":
        amount = 0.85
    elif fruit == "grapefruit":
        amount = 1.45
    elif fruit == "kiwi":
        amount = 2.70
    elif fruit == "pineapple":
        amount = 5.50
    elif fruit == "grapes":
        amount = 3.85
elif day == "Saturday" or day == "Sunday":
    if fruit == "banana":
        amount = 2.70
    elif fruit == "apple":
        amount = 1.25
    elif fruit == "orange":
        amount = 0.90
    elif fruit == "grapefruit":
        amount = 1.60
    elif fruit == "kiwi":
        amount = 3.00
    elif fruit == "pineapple":
        amount = 5.60
    elif fruit == "grapes":
        amount = 4.20

price = amount * quantity
if price == 0:
    print("error")
else:
    print(f"{price:.2f}")

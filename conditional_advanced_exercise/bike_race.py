number_juniors = int(input())
number_seniors = int(input())
trail = input()
tax = 0
junior_price = 0
senior_price = 0
donation = 0
if trail == "trail":
    junior_price = 5.50
    senior_price = 7
    tax = junior_price * number_juniors + senior_price * number_seniors
    donation = 0.95 * tax
elif trail == "cross-country":
    junior_price = 8
    senior_price = 9.50
    tax = junior_price * number_juniors + senior_price * number_seniors
    if number_seniors + number_juniors >= 50:
        tax = 0.75 * tax
    donation = 0.95 * tax
elif trail == "downhill":
    junior_price = 12.25
    senior_price = 13.75
    tax = junior_price * number_juniors + senior_price * number_seniors
    donation = 0.95 * tax
elif trail == "road":
    junior_price = 20
    senior_price = 21.50
    tax = junior_price * number_juniors + senior_price * number_seniors
    donation = 0.95 * tax
print(f"{donation:.2f}")
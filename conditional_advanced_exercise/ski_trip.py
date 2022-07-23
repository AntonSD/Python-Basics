days = int(input())
type = input()
rating = input()
room_for_one_person = 18
apartment = 25
president_apartment = 35
price_of_room = 0
if type == "apartment":
    price_of_room = 25
    if days < 10:
        price_of_room *= 0.7
    elif 10 < days < 15:
        price_of_room *= 0.65
    elif days > 15:
        price_of_room *= 0.5
elif type == "president apartment":
    price_of_room = 35
    if days < 10:
        price_of_room *= 0.9
    elif 10 < days < 15:
        price_of_room *= 0.85
    elif days > 15:
        price_of_room *= 0.8
else:
    price_of_room = 18
nights = days - 1
final_price = price_of_room * nights
if rating == "positive":
    final_price = final_price + 0.25 * final_price
elif rating == "negative":
    final_price = final_price - 0.1 * final_price
print(f"{final_price:.2f}")
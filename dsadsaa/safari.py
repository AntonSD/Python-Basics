budget = float(input())
number_nights = int(input())
price_per_night = float(input())
percent_extra_taxes = int(input())

if number_nights > 7:
    price_per_night = 0.95 * price_per_night
price_nights = price_per_night * number_nights
percent = percent_extra_taxes / budget * 100
total = price_nights + percent
difference = abs(budget - price_nights)
if budget >= total:
    print(f"Ivanovi will be left with {difference:.2f} leva after vacation.")
else:
    print(f"{difference:.2f} leva needed.")
kind_of_flowers = input()
count_flowers = int(input())
budget = int(input())
price = 0
price_of_flower = 0
if kind_of_flowers == "Roses":
    price_of_flower = 5
    price = price_of_flower * count_flowers
    if count_flowers > 80:
        price *= 0.9
elif kind_of_flowers == "Dahlias":
    price_of_flower = 3.80
    price = price_of_flower * count_flowers
    if count_flowers > 90:
        price *= 0.85
elif kind_of_flowers == "Tulips":
    price_of_flower = 2.80
    price = price_of_flower * count_flowers
    if count_flowers > 80:
        price *= 0.85
elif kind_of_flowers == "Narcissus":
    price_of_flower = 3
    price = price_of_flower * count_flowers
    if count_flowers < 120:
        price *= 1.15
elif kind_of_flowers == "Gladiolus":
    price_of_flower = 2.50
    price = price_of_flower * count_flowers
    if count_flowers < 80:
        price *= 1.20
difference = abs(budget - price)
if budget >= price:
    print(f"Hey, you have a great garden with {count_flowers} {kind_of_flowers} and {difference:.2f} leva left.")
else:
    print(f"Not enough money, you need {difference:.2f} leva more.")

import math
number_days = int(input())
left_food = int(input())
dog_per_day = float(input())
cat_per_day = float(input())
turtle_per_day = float(input())
turtle_per_day_kg = turtle_per_day * number_days / 1000
dog_whole = number_days * dog_per_day
cat_whole = number_days * cat_per_day
all_food = dog_whole + cat_whole + turtle_per_day_kg
difference = abs(left_food - all_food)
if left_food > all_food:
    print(f"{math.floor(difference)} kilos of food left.")
else:
    print(f"{math.ceil(difference)} more kilos of food are needed.")

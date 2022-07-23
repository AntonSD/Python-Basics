import math
x_square = int(input())
y_square = float(input())
z_liters = int(input())
worker = int(input())
grape = x_square * y_square
producing_wine = 0.4 * grape
wine = producing_wine / 2.5
difference = abs(wine - z_liters)
wine_per_worker = difference / worker
if wine < z_liters:
    print(f"It will be a tough winter! More {math.floor(difference)} liters wine needed.")
elif wine >= z_liters:
    print(f"Good harvest this year! Total wine: {math.ceil(wine)} liters.")
    print(f"{math.ceil(difference)} liters left -> {math.ceil(wine_per_worker)} liters per person.")



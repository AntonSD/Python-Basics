strawberry_price = float(input())
bananas_kg = float(input())
oranges_kg = float(input())
raspberries_kg = float(input())
strawberry_kg = float(input())
raspberries_price = 0.5 * strawberry_price
oranges_price = 0.6 * raspberries_price
bananas_price = 0.2 * raspberries_price
total_sum = strawberry_price * strawberry_kg + bananas_price * bananas_kg + raspberries_kg * raspberries_price + oranges_price * oranges_kg
print(f"{total_sum:.2f}")
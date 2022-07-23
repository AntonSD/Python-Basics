movie_type = input()
rows = int(input())
column = int(input())
income = 0
price = 0
if movie_type == "Premiere":
    price = 12.00
elif movie_type == "Normal":
    price = 7.50
elif movie_type == "Discount":
    price = 5.00
income = (rows * column) * price
print(f"{income:.2f} leva")
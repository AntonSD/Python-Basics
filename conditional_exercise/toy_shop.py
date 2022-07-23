excursion_price = float(input())
count_puzzles = int(input())
count_dolls = int(input())
count_bears = int(input())
count_minion = int(input())
count_truck = int(input())
count_toys = count_truck + count_bears + count_dolls + count_minion + count_puzzles
puzzle = 2.60
speaking_doll = 3
teddy_bear = 4.10
minion = 8.20
truck = 2
puzzle_price = puzzle * count_puzzles
doll_price = count_dolls * speaking_doll
bear_price = count_bears * teddy_bear
minion_price = minion * count_minion
truck_price = count_truck * truck
total_price = puzzle_price + doll_price + bear_price + minion_price + truck_price
count_toys = count_truck + count_bears + count_dolls + count_minion + count_puzzles
if count_toys >= 50:
    discount = total_price * 0.25
    total_sum = total_price - discount
    rent = total_sum * 0.1
    earning = total_sum - rent
    rest_money = earning - excursion_price
else:
    rent = total_price * 0.1
    earning = total_price - rent
    needed_money = excursion_price - earning
if earning > excursion_price:
    print(f"Yes! {rest_money:.2f} lv left.")
elif earning < excursion_price:
    needed_money = excursion_price - earning
    print(f"Not enough money! {needed_money:.2f} lv needed.")





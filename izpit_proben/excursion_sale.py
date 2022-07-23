number_sea = int(input())
number_mountain = int(input())
command = input()
sea_excursion = 680
mountain_excursion = 499
total_sum = 0
sea_counter = 0
mountain_counter = 0
all_sold = False
while command != "Stop":
    if command == "sea":
        if number_sea > sea_counter:
            sea_counter += 1
            total_sum += sea_excursion
        elif sea_counter > number_sea:
            continue
    elif command == "mountain":
        if number_mountain > mountain_counter:
            mountain_counter += 1
            total_sum += mountain_excursion
        elif mountain_counter > number_mountain:
            continue
    if sea_counter == number_sea and mountain_counter == number_mountain:
        all_sold = True
        break
    command = input()
if all_sold:
    print(f"Good job! Everything is sold.")
    print(f"Profit: {total_sum} leva.")
else:
    print(f"Profit: {total_sum} leva.")
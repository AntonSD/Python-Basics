pc_models = int(input())
average = 0
total_sales = 0
possible_salements = 0
for digit in range(pc_models):
    number = int(input())
    numbers = int(str(number)[:-1])
    number_as_str = str(number)
    last_number = number_as_str[2]
    if last_number == "2":
        total_sales += 0
    elif last_number == "3":
        total_sales += 0.5 * numbers
    elif last_number == "4":
        total_sales += 0.7 * numbers
    elif last_number == "5":
        total_sales += 0.85 * numbers
    elif last_number == "6":
        total_sales += numbers
    if number % 10 == 1:
        average += 1
    elif number % 10 == 2:
        average += 2
    elif number % 10 == 3:
        average += 3
    elif number % 10 == 4:
        average += 4
    elif number % 10 == 5:
        average += 5
    elif number % 10 == 6:
        average += 6
    elif number % 10 == 7:
        average += 7
    elif number % 10 == 8:
        average += 8
    elif number % 10 == 9:
        average += 9
overall_average = average / pc_models
print(f"{total_sales:.2f}")
print(f"{overall_average:.2f}")
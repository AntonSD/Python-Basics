number_moves = int(input())
points = 0
zero_to_nine = 0
nineteen = 0
twentynine = 0
thirtynine= 0
fourtynine = 0
fifty = 0

for numbers in range(number_moves):
    number = int(input())
    if 0 <= number <= 9:
        points += 0.2 * number
        zero_to_nine += 1
    elif 10 <= number <= 19:
        points += 0.3 * number
        nineteen += 1
    elif 20 <= number <= 29:
        points += 0.4 * number
        twentynine += 1
    elif 30 <= number <= 39:
        points += 0.5 * number
        thirtynine += 1
    elif 40 <= number <= 50:
        points += 100
        fourtynine += 1
    else:
        points /= 2
        fifty += 1

percent_zero = zero_to_nine / number_moves * 100
percent_nineteen = nineteen / number_moves * 100
percent_twenty = twentynine / number_moves * 100
percent_thirty = thirtynine / number_moves * 100
percent_fourty = fourtynine / number_moves * 100
percent_fifty = fifty / number_moves * 100
print(f"{points:.2f}")
print(f"From 0 to 9: {percent_zero:.2f}%")
print(f"From 10 to 19: {percent_nineteen:.2f}%")
print(f"From 20 to 29: {percent_twenty:.2f}%")
print(f"From 30 to 39: {percent_thirty:.2f}%")
print(f"From 40 to 50: {percent_fourty:.2f}%")
print(f"Invalid numbers: {percent_fifty:.2f}%")

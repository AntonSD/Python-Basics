count_of_numbers = int(input())
sum_of_all_numbers = 0
max_number = ""
for number in range(count_of_numbers):
    current_number = int(input())
    if number == 0:
        max_number = current_number
    sum_of_all_numbers += current_number
    if current_number > max_number:
        max_number = current_number
if max_number == sum_of_all_numbers - max_number:
    print("Yes")
    print(f"Sum = {max_number}")
else:
    difference = abs(max_number - (sum_of_all_numbers - max_number))
    print("No")
    print(f"Diff = {difference}")

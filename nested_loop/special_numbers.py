number = int(input())
for current_number in range(1111, 9999 + 1):
    number_is_special = True
    current_number_as_str = str(current_number)
    for current_digit in current_number_as_str:
        if int(current_digit) == 0 or number % int(current_digit) != 0:
            number_is_special = False
            break
    if number_is_special:
        print(current_number_as_str, end=' ')


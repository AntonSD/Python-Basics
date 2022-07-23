import sys

number = input()
min_num = sys.maxsize
while number != "Stop":
    new_number = int(number)
    if new_number < min_num:
        min_num = new_number
    number = input()
print(min_num)
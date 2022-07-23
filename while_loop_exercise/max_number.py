import sys

number = input()
max_num = -sys.maxsize
while number != "Stop":
    new_number = int(number)
    if new_number > max_num:
        max_num = new_number
    number = input()
print(max_num)
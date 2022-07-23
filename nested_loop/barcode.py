import sys

command = input()
min_num = sys.maxsize
new_num = 0
while command != "Stop":
    new = int(command)
    if new < min_num:
        min_num = new
    command = input()
print(min_num)
import sys

n = int(input())

max_num = -sys.maxsize
min_num = sys.maxsize
for i in range(n):
    number = int(input())
    if max_num < number:
        max_num = number
    elif min_num > number:
        min_num = number

print(f"Max number: {max_num}")
print(f"Min number: {min_num}")

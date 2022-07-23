number = int(input())
sum = 0

for number in range(1, number + 1):
    new_number = int(input())
    sum += new_number
average = sum / number
print(f"{average:.2f}")
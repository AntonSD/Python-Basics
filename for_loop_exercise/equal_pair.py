count_numbers = int(input())

sum_1 = 0
sum_2 = 0
for num in range(count_numbers):
    value = int(input())
    sum_1 += value

for num in range(count_numbers):
    value = int(input())
    sum_2 += value

difference = abs(sum_1 - sum_2)

if sum_1 == sum_2:
    print(f"Yes, value={sum_1}")
elif sum_1 != sum_2:
    print(f"No, maxdiff={difference}" )
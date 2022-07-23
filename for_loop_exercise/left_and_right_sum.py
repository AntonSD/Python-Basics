n = int(input())

left_sum = 0
for i in range(n):
    current_sum = int(input())
    left_sum += current_sum

right_sum = 0
for i in range(n):
    current_sum = int(input())
    right_sum += current_sum

if right_sum == left_sum:
    print(f"Yes, sum = {left_sum}")
else:
    diff = abs(left_sum - right_sum)
    print(f"No, diff = {diff}")
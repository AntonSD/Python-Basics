number = int(input())
sum = 1

while sum <= number:
    print(sum)
    sum = 2 * sum + 1
    if sum > number:
        break

k = int(input())
l = int(input())
m = int(input())
n = int(input())

counter = 0
while counter < 6:
    counter += 1
    for num1 in range(2, k + 1, 2):
        for num2 in range(1 , l +1):
            if num2 % 2 != 1:
                continue
            for num3 in range(2, m + 1, 2):
                for num4 in range(2, n + 1, 1):
                    if num4 % 2 != 1:
                        continue
    print(f"{num1} {num2} {num3} {num4}")

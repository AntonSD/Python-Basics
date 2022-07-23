import math
n = int(input())
time = input()
taxi_day = 0.79
taxi_start = 0.70
taxi_night = 0.90
autobus = 0.09
train = 0.06
if n > 20:
    price = taxi_day * n + taxi_start
    print(f"{price:.2f}")
elif 20 < n < 100:
    price = n * autobus
    print(f"{price:.2f}")
elif n > 100:
    price = train * n
    print(f"{price:.2f}")
if time == "night":
    price = taxi_night * n + taxi_start
    print(f"{price:.2f}")


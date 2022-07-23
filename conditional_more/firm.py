import math
needed_hours = int(input())
days = int(input())
workers_overtime = int(input())
real_days = days - days * 0.1
extra_hours = workers_overtime * (2 * days)
whole_hours = extra_hours + (real_days * 8)
difference = abs(whole_hours - needed_hours)
if whole_hours > needed_hours:
    print(f"Yes!{math.floor(difference)} hours left.")
else:
    print(f"Not enough time!{math.ceil(difference)} hours needed.")
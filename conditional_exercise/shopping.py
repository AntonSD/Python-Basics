budget = float(input())
count_gpu = int(input())
count_cpu = int(input())
count_ram = int(input())
gpu = 250
gpu_price = gpu * count_gpu
cpu = gpu_price * 35 / 100
ram = gpu_price * 10 / 100
cpu_price = cpu * count_cpu
ram_price = ram * count_ram
needed_sum = gpu_price + cpu_price + ram_price
if count_gpu > count_cpu:
    needed_sum = needed_sum - needed_sum * 15 / 100
difference = abs(budget - needed_sum)
if budget > needed_sum:
    print(f"You have {difference:.2f} leva left!")
else:
    print(f"Not enough money! You need {difference:.2f} leva more!")
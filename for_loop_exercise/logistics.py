loadings = int(input())
average_price = 0
microbus = 0
truck = 0
train = 0

for weight in range (loadings):
    type_load = int(input())
    if type_load <= 3:
        microbus += type_load
    elif 4 <= type_load <= 11:
        truck += type_load
    else:
        train += type_load

price_for_microbus = microbus * 200
price_for_truck = truck * 175
price_for_train = train * 120
all_cargos = microbus + truck + train
average_price = (price_for_train + price_for_truck + price_for_microbus) / all_cargos

percent_microbus = microbus / all_cargos * 100
percent_truck = truck / all_cargos * 100
percent_train = train / all_cargos * 100

print(f"{average_price:.2f}")
print(f"{percent_microbus:.2f}%")
print(f"{percent_truck:.2f}%")
print(f"{percent_train:.2f}%")

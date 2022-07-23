number_groups = int(input())
every_group_num_members = int(input())

musala = 0
monblan = 0
kilimanjaro = 0
k2 = 0
everest = 0
every_group = 0
for groups in range(number_groups):
    every_group = int(input())
    if every_group <= 5:
        musala += every_group
    elif 6 <= every_group <= 12:
        monblan += every_group
    elif 13 <= every_group <= 25:
        kilimanjaro += every_group
    elif 25 <= every_group <= 40:
        k2 += every_group
    else:
        everest += every_group
all_group_members = musala + monblan + kilimanjaro + k2 + everest
print(f"{musala / all_group_members * 100:.2f}%")
print(f"{monblan / all_group_members * 100:.2f}%")
print(f"{kilimanjaro / all_group_members * 100:.2f}%")
print(f"{k2 / all_group_members * 100:.2f}%")
print(f"{everest / all_group_members * 100:.2f}%")
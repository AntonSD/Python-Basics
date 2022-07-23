group_number = int(input())
all_group_members = 0
musala = 0
monblan = 0
kilimanjaro = 0
k2 = 0
everest = 0
for groups in range (group_number):
    group_members = int(input())
    all_group_members += group_members
    if group_members <= 5:
        musala += group_members
    elif 6 <= group_members <= 12:
        monblan += group_members
    elif 13 <= group_members <= 25:
        kilimanjaro +=  group_members
    elif 26 <= group_members <= 40:
        k2 += group_members
    else:
        everest += group_members
all_members = musala + monblan + kilimanjaro + k2 + everest
print(f"{musala / all_group_members * 100:.2f}%")
print(f"{monblan / all_group_members * 100:.2f}%")
print(f"{kilimanjaro / all_group_members * 100:.2f}%")
print(f"{k2 / all_group_members * 100:.2f}%")
print(f"{everest / all_group_members * 100:.2f}%")
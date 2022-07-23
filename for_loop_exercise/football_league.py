capacity_of_stadium = int(input())
number_of_fans = int(input())
sector_a = 0
sector_b = 0
sector_v = 0
sector_g = 0
team_1 = 0
team_2 = 0
for sectors in range (number_of_fans):
    sector = input()
    if sector == "A":
        team_1 += 1
        sector_a +=1
    elif sector == "B":
        team_1 += 1
        sector_b += 1
    elif sector == "V":
        team_2 += 1
        sector_v += 1
    elif sector == "G":
        team_2 += 1
        sector_g += 1
percent_capacity = number_of_fans / capacity_of_stadium * 100
percent_sector_a = sector_a / number_of_fans * 100
percent_sector_b = sector_b / number_of_fans * 100
percent_sector_v = sector_v / number_of_fans * 100
percent_sector_g = sector_g / number_of_fans * 100
print(f"{percent_sector_a:.2f}%")
print(f"{percent_sector_b:.2f}%")
print(f"{percent_sector_v:.2f}%")
print(f"{percent_sector_g:.2f}%")
print(f"{percent_capacity:.2f}%")

import math
number_tournaments = int(input())
starting_rank_points = int(input())
won = 0
w = 0
f = 0
sf = 0
all_points = 0
average_points = 0
won_points = 0
for number in range(number_tournaments):
    stage = input()
    if stage == "W":
        w += 2000
        won += 1
    elif stage == "F":
        f += 1200
    elif stage == "SF":
        sf += 720
won_points = w + f + sf
all_points = w + f + sf + starting_rank_points
average_points = won_points / number_tournaments
won_tournaments = (won / number_tournaments) * 100

print(f"Final points: {all_points}")
print(f"Average points: {math.floor(average_points)}")
print(f"{won_tournaments:.2f}%")

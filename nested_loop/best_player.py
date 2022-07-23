import sys

player_name = ""
goals = 0
player_goals = -sys.maxsize
best_player = ""
while goals >= 10:
    command = input()
    if command == "End":
        break
    goals = int(input())
    if goals > player_goals:
        player_goals = goals
        best_player = command
    if goals >= 10:
        player_goals = goals
        player_name = command
        break
    player_name = input()
if goals >= 3:
    print(f"{player_name} is the best player!")
    print(f"He has scored {player_goals} goals and made a hat-trick !!!")
else:
    print(f"{player_name} is the best player!")
    print(f"He has scored {goals} goals.")
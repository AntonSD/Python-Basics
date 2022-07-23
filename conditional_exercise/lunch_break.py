import math
tv_show = input()
tv_show_time = int(input())
rest_time = int(input())
lunch_time = rest_time * 1/8
off_time = rest_time * 1/4
all_time = rest_time - off_time - lunch_time
difference = abs(all_time - tv_show_time)
if all_time >= tv_show_time:
    print(f"You have enough time to watch {tv_show} and left with {math.ceil(difference)} minutes free time.")
else:
    print(f"You don't have enough time to watch {tv_show}, you need {math.ceil(difference)} more minutes.")

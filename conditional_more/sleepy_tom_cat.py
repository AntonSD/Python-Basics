days_off = int(input())
norm = 30000
working_days_minutes = 63
holidays_minutes = 127
year = 365
working_days = year - days_off
playing_time = (working_days * working_days_minutes) + (holidays_minutes * days_off)
difference = abs(norm - playing_time)
hours = difference // 60
minutes = difference % 60
if playing_time > norm:
    print('Tom will run away')
    print(f"{int(hours)} hours and {int(minutes)} minutes more for play")
else:
    print("Tom sleeps well")
    print(f"{int(hours)} hours and {int(minutes)} minutes less for play")
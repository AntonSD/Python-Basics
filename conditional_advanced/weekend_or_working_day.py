day = input()

is_working_day = day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday'
weekend = day == 'Sunday' or day == 'Saturday'

if is_working_day:
    print("Working day")
elif weekend:
    print("Weekend")
else:
    print("Error")
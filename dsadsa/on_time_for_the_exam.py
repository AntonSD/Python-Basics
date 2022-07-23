hour_of_the_exam = int(input())
minute_of_the_exam = int(input())
arriving_hour = int(input())
arriving_minute = int(input())
time_of_exam = hour_of_the_exam * 60 + minute_of_the_exam
time_of_arriving = arriving_hour * 60 + arriving_minute
if time_of_arriving > time_of_exam:
    print("Late")
elif time_of_exam - 30 <= time_of_arriving <= time_of_exam:
    print("On time")
else:
    print("Early")
difference = abs(time_of_arriving - time_of_exam)
hours = difference // 60
minutes = difference % 60
if time_of_exam - 60 < time_of_arriving < time_of_exam:
    print(f"{minutes} minutes before the start")
elif time_of_arriving <=time_of_exam - 60:
    print(f"{hours}:{minutes:02d} hours before the start")
elif time_of_exam < time_of_arriving < time_of_exam + 60:
    print(f"{difference} minutes after the start")
elif time_of_arriving >= time_of_exam + 60:
    print(f"{hours}:{minutes:02d} hours after the start")

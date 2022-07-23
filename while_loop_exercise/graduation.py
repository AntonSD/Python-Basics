name = input()
all_grades = 0
year = 0
failed_years = 0
graduated = True
while year != 12:
    rating = float(input())
    year += 1
    all_grades += rating
    if rating <= 4:
        failed_years += 1
        year -= 1
        if failed_years > 1:
            print(f"{name} has been excluded at {year} grade")
            continue
average_rating = all_grades / year
print(f"{name} graduated. Average grade: {average_rating:.2f}")



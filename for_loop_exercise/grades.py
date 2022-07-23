students = int(input())

students_with_2 = 0
students_with_3 = 0
students_with_4 = 0
students_with_5 = 0
average = 0
for grades in range(students):
    grade = float(input())
    average += grade
    if grade <= 2.99:
        students_with_2 += 1
    elif 3 <= grade <= 3.99:
        students_with_3 +=1
    elif 4 <= grade <= 4.99:
        students_with_4 += 1
    else:
        students_with_5 += 1
average_grade = average / students

percent_2 = students_with_2 / students * 100
percent_3 = students_with_3 / students * 100
percent_4 = students_with_4 / students * 100
percent_5 = students_with_5 / students * 100

print(f"Top students: {percent_5:.2f}%")
print(f"Between 4.00 and 4.99: {percent_4:.2f}%")
print(f"Between 3.00 and 3.99: {percent_3:.2f}%")
print(f"Fail: {percent_2:.2f}%")
print(f"Average: {average_grade:.2f}")
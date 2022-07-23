unsatisfied_grades = int(input())
solved_problems = 0
unsolved_problems = 0
last_problem = ""
grades_sum = 0
enough_grades = False
grades = 0
while unsolved_problems < unsatisfied_grades:
    problem_name = input()
    if problem_name == "Enough":
        enough_grades = True
        break
    grade = int(input())
    if grade <= 4:
        unsolved_problems += 1
    grades += grade
    grades_sum += 1
    solved_problems += 1
    last_problem = problem_name
average_grade = grades / grades_sum
if enough_grades:
    print(f"Average score: {average_grade:.2f}")
    print(f"Number of problems: {grades_sum}")
    print(f"Last problem: {last_problem}")
else:
    print(f"You need a break, {unsatisfied_grades} poor grades.")


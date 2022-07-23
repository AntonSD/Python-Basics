unsatisfied_ratings = int(input())
number_of_unsatisfied = 0
task = input()
score = 0
number_of_tasks = 0
while number_of_unsatisfied < unsatisfied_ratings:
    if task == "Enough":
        break
    scores = int(input())
    score += scores
    number_of_tasks += 1
    if scores <= 4:
        number_of_unsatisfied += 1
    task = input()
if number_of_unsatisfied > unsatisfied_ratings:
    print(f"You need a break, {unsatisfied_ratings} poor grades.")
else:
    average = score / number_of_tasks
    print(f"Average score: {average:.2f}")
    print(f"Number of problems: {number_of_tasks}")
    print(f"Last problem: {task}")



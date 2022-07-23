number_tabs = int(input())
salary = int(input())
salary_fine = 0
salary_after_fine = 0

for number in range(number_tabs):
    current_tab = input()
    if current_tab == "Facebook":
        salary_fine += 150
    elif current_tab == "Instagram":
        salary_fine += 100
    elif current_tab == "Reddit":
        salary_fine += 50
    if salary <= salary_fine:
        break
salary_after_fine = salary - salary_fine
if salary_after_fine > 0:
    difference = salary - salary_fine
    print(f"{salary_after_fine}")
else:
    print("You have lost your salary.")

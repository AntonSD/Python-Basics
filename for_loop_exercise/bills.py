number_months = int(input())
value_of_el = 0
water = 0
internet = 0
other_expenses = 0
total_of_other = 0
for number in range (number_months):
    electricity_per_month = float(input())
    value_of_el += electricity_per_month
    water += 20
    internet += 15
total_of_other += 1.2 * (water + internet + value_of_el)
average = (value_of_el + water + internet + total_of_other) / number_months
print(f"Electricity: {value_of_el:.2f} lv")
print(f"Water: {water:.2f} lv")
print(f"Internet: {internet:.2f} lv")
print(f"Other: {total_of_other:.2f} lv")
print(f"Average: {average:.2f} lv")
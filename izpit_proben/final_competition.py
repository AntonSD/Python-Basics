number_dancers = int(input())
points = float(input())
season = input()
destination = input()
income = 0
income_abroad = 0
expenses = 0
charity = 0
total_income = 0
dancer_income = 0
if destination == "Bulgaria":
    income = number_dancers * points
    if season == "winter":
        income = 0.92 * income
    elif season == "summer":
        income = 0.95 * income
elif destination == "Abroad":
    income_abroad = number_dancers * points
    income += 1.5 * income_abroad
    if season == "winter":
        income = 0.85 * income
    elif season == "summer":
        income = 0.90 * income
charity = 0.75 * income
total_income = income - charity
dancer_income = total_income / number_dancers
print(f"Charity - {charity:.2f}")
print(f"Money per dancer - {dancer_income:.2f}")



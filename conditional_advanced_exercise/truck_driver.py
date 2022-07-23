season = input()
km_per_month = float(input())
salary = 0
season_salary = 0
price_per_km = 0
season_salary = 0
tax = 0
neto_salary = 0
if (season == "Spring" or season == "Autumn") and km_per_month <= 10000:
    if km_per_month <= 5000:
        price_per_km = 0.75
    elif 5000 < km_per_month <= 10000:
        price_per_km = 0.95
elif season == "Summer" and km_per_month <= 10000:
    if km_per_month <= 5000:
        price_per_km = 0.90
    elif 5000 < km_per_month <= 10000:
        price_per_km = 1.10
elif season == "Winter" and km_per_month <= 10000:
    if km_per_month <= 5000:
        price_per_km = 1.05
    elif 5000 < price_per_km <= 10000:
        price_per_km = 1.25
elif 10000 < km_per_month <= 20000:
    price_per_km = 1.45
salary = km_per_month * price_per_km
season_salary = salary * 4
tax = season_salary - 0.9 * season_salary
neto_salary = season_salary - tax
print(f"{neto_salary:.2f}")
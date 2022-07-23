heritage = float(input())
living_years = int(input())
old = 17
spend_money = 0
rest_money = 0
year = 1800

for years in range(1800, living_years + 1):
    old += 1
    if years % 2 == 0:
        spend_money += 12000
    elif years % 2 != 0:
        spend_money += 12000 + 50 * old
difference = abs(heritage - spend_money)
if heritage > spend_money:
    print(f"Yes! He will live a carefree life and will have {difference:.2f} dollars left.")
else:
    print(f"He will need {difference:.2f} dollars to survive.")
number_chrisantemas = int(input())
number_roses = int(input())
number_tulips = int(input())
season = input()
celebrating = input()
service = 2
chrisantema = 0
rose = 0
tulip = 0
price = 0
if season == "Summer" or season == "Spring":
    chrisantema = 2
    rose = 4.10
    tulip = 2.50
    price = chrisantema * number_chrisantemas + tulip * number_tulips + rose * number_roses + service
elif season == "Winter" or season == "Autumn":
    chrisantema = 3.75
    rose = 4.50
    tulip = 4.15
    price = chrisantema * number_chrisantemas + tulip * number_tulips + rose * number_roses + service
if celebrating == "Y":
    price = 1.15 * price
if season == "Spring" and number_tulips > 7:
    price = 0.95 * price
elif season == "Winter" and number_roses >= 10:
    price = 0.9 * price
if number_roses + number_chrisantemas + number_tulips > 20:
    price = 0.8 * price
print(f"{price:.2f}")

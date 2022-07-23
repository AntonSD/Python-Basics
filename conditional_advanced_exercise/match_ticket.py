budget = float(input())
kind_of_ticket = input()
number_of_people = int(input())
ticket_price = 0
transport = 0
if kind_of_ticket == "VIP":
    ticket_price = 499.99
    if 1 <= number_of_people <= 4:
        transport = 0.75 * budget
    elif 5 <= number_of_people <= 9:
        transport = 0.6 * budget
    elif 10 <= number_of_people <= 24:
        transport = 0.5 * budget
    elif 25 <= number_of_people <= 49:
        transport = 0.4 * budget
    elif 50 <= number_of_people:
        transport = 0.25 * budget
elif kind_of_ticket == "Normal":
    ticket_price = 249.99
    if 1 <= number_of_people <= 4:
        transport = 0.75 * budget
    elif 5 <= number_of_people <= 9:
        transport = 0.6 * budget
    elif 10 <= number_of_people <= 24:
        transport = 0.5 * budget
    elif 25 <= number_of_people <= 49:
        transport = 0.4 * budget
    elif 50 <= number_of_people:
        transport = 0.25 * budget
final_price = ticket_price * number_of_people + transport
difference = abs(budget - final_price)
if budget >= final_price:
    print(f"Yes! You have {difference:.2f} leva left.")
elif budget < final_price:
    print(f"Not enough money! You need {difference:.2f} leva.")

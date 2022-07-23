needed_sum = float(input())
owned_money = float(input())
spend_money = 0
save_money = 0
spending_days = 0
saving_days = 0
days = 0
while owned_money < needed_sum and spending_days < 5:
    command = input()
    money = float(input())
    days += 1
    if command == "spend":
        spending_days += 1
        owned_money -= money
        if owned_money < 0:
            owned_money = 0
    elif command == "save":
        saving_days += 1
        owned_money += money
if spending_days == 5:
    print("You can't save the money.")
    print(f"{days}")
else:
    print(f"You saved the money for {days} days.")
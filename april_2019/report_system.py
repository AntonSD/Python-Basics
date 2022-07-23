needed_sum =int(input())

cash = 0
credit_card = 0
counter_cash = 0
counter_credit = 0
total = 0
counter = 0
while total < needed_sum:
    command = input()
    if command == "End":
        break
    counter += 1
    money = int(command)
    if counter % 2 == 0:
        if money < 10:
            print("Error in transaction!")
            continue
        counter_credit += 1
        credit_card += money
        print("Product sold!")
    else:
        if money > 100:
            print("Error in transaction!")
            continue
        cash += money
        counter_cash += 1
        print("Product sold!")
    total = cash + credit_card
average_cash = cash / counter_cash
average_credit = credit_card / counter_credit
if command == "End":
    print("Failed to collect required money for charity.")
else:
    print(f"Average CS: {average_cash:.2f}")
    print(f"Average CC: {average_credit:.2f}")


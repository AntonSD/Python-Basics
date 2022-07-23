command = input()
sum = 0
while command != "NoMoreMoney":
    increase = float(command)
    if increase < 0:
        print("Invalid operation!")
        break

    sum += increase
    print(f"Increase: {increase:.2f}")

    command = input()

print(f"Total: {sum:.2f}")
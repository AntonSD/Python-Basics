count_joinery = int(input())
type_joinery = input()
delivery = input()
price = 0
delivery_price = 60
if type_joinery == "90X130":
    price = 110
    if 30 < count_joinery < 60:
        price *= 0.95
    elif count_joinery > 60:
        price *= 0.92
elif type_joinery == "100X150":
    price = 140
    if 40 < count_joinery < 80:
        price *= 0.94
    elif count_joinery > 80:
        price *= 0.9
elif type_joinery == "130X180":
    price = 190
    if 20 < count_joinery < 50:
        price *= 0.93
    elif count_joinery > 50:
        price *= 0.88
elif type_joinery == "200X300":
    price = 250
    if 25 < count_joinery < 50:
        price *= 0.91
    elif count_joinery > 50:
        price *= 0.86
total_price = count_joinery * price
if delivery == "With delivery":
    total_price = total_price + 60
elif delivery == "Without delivery":
    total_price = total_price
if 10 < count_joinery < 99:
    print(f"{total_price:.2f} BGN")
elif count_joinery > 99:
    total_price *= 0.96
    print(f"{total_price:.2f} BGN")
elif count_joinery < 10:
    print("Invalid order")

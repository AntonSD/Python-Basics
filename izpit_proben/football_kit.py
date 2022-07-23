t_shirt = float(input())
winning_sum = float(input())

shorts = 0.75 * t_shirt
socks = 0.2 * shorts
football_shoes = 2 * (t_shirt + shorts)
total = t_shirt + shorts + socks + football_shoes
discount = 0.85 * total
difference = abs(discount - winning_sum)
if discount >= winning_sum:
    print(f"Yes, he will earn the world-cup replica ball!")
    print(f"His sum is {discount:.2f} lv.")
else:
    print(f"No, he will not earn the world-cup replica ball.")
    print(f"He needs {difference:.2f} lv. more.")
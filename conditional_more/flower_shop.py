import math
count_mag = int(input())
count_zum = int(input())
count_roses = int(input())
count_cactus = int(input())
prsent_price = float(input())
mag_price = 3.25 * count_mag
zum_price = 4 * count_zum
rose_price = 3.50 * count_roses
cactus_price = 8 * count_cactus
total_price = mag_price + zum_price + rose_price + cactus_price
taxes = 0.05 * total_price
needed_sum = total_price - taxes
difference = abs(needed_sum - prsent_price)
if needed_sum > prsent_price:
    print(f"She is left with {math.floor(difference)} leva.")
else:
    print(f"She will have to borrow {math.ceil(difference)} leva.")
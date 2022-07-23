price_per_sqm = 7.61
total_sqm = float(input())
total_sum = total_sqm * price_per_sqm
discount = total_sum * 0.18
final_price = total_sum - discount
print(f'The final price is: {final_price} lv.')
print(f'The discount is: {discount} lv.')
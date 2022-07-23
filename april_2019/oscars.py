rent_hall = int(input())
statues = 0.7 * rent_hall
catering = 0.85 * statues
sound = 0.5 * catering
total_sum = rent_hall + statues + catering + sound
print(f"{total_sum:.2f}")
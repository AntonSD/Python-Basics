rent_hall = int(input())

statues = rent_hall - 0.3 * rent_hall
catering = statues - 0.15 * statues
sound = catering - 0.5 * catering

total = rent_hall + statues + catering + sound
print(f"{total:.2f}")
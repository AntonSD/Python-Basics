detergent = int(input())
detergent_ml = detergent * 750
number_dishes = ""
number_of_dishes = 0
number_of_pans = 0
liquid_for_dishes = 0
liquid_for_pan = 0
counter = 0
total = 0
while total < detergent_ml:
    command = input()
    if command == "End":
        break
    counter += 1
    numbers = int(command)
    if counter % 3 == 0:
        number_of_pans += numbers
        liquid_for_pan += numbers * 15
    else:
        number_of_dishes += numbers
        liquid_for_dishes += numbers * 5
    total = liquid_for_dishes + liquid_for_pan
difference = abs(detergent_ml - total)
if total < detergent_ml or command == "End":
    print(f"Detergent was enough!")
    print(f"{number_of_dishes} dishes and {number_of_pans} pots were washed.")
    print(f"Leftover detergent {difference} ml.")
else:
    print(f"Not enough detergent, {difference} ml. more necessary!")


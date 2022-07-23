width = int(input())
length = int(input())
height = int(input())
volume = width * length * height
total_loadings = 0
enough_space = False
while volume >= total_loadings:
    command = input()
    if command == "Done":
        break
    new_package = int(command)
    total_loadings += new_package
difference = abs(total_loadings - volume)
if total_loadings > volume:
    print(f"No more free space! You need {difference} Cubic meters more.")
else:
    print(f"{difference} Cubic meters left.")
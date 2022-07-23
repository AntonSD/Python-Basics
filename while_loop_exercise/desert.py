width = int(input())
length = int(input())
volume = width * length
cake_is_over = True
pieces_left = 0
given_pieces = 0
total_pieces = 0
while volume >= total_pieces:
    command = input()
    if command == "STOP":
        break
    pieces = int(command)
    total_pieces += pieces
difference = abs(total_pieces - volume)
if total_pieces > volume:
    print(f"No more cake left! You need {difference} pieces more.")
else:
    print(f"{difference} pieces are left.")
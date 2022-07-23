title_movie = input()
cinema_hall = input()
sold_tickets = int(input())

ticket = 0
if title_movie == "A Star Is Born":
    if cinema_hall == "normal":
        ticket = 7.50
    elif cinema_hall == "luxury":
        ticket = 10.50
    elif cinema_hall == "ultra luxury":
        ticket = 13.50
elif title_movie == "Bohemian Rhapsody":
    if cinema_hall == "normal":
        ticket = 7.35
    elif cinema_hall == "luxury":
        ticket = 9.45
    elif cinema_hall == "ultra luxury":
        ticket = 12.75
elif title_movie == "Green Book":
    if cinema_hall == "normal":
        ticket = 8.15
    elif cinema_hall == "luxury":
        ticket = 10.25
    elif cinema_hall == "ultra luxury":
        ticket = 13.25
elif title_movie == "The Favourite":
    if cinema_hall == "normal":
        ticket = 8.75
    elif cinema_hall == "luxury":
        ticket = 11.55
    elif cinema_hall == "ultra luxury":
        ticket = 13.95
income = sold_tickets * ticket
print(f"{title_movie} -> {income:.2f} lv.")
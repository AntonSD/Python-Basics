import sys

number_movies = int(input())

highest_rating = 0
lowest_rating = 0
all_ratings = 0
highest_rating_movie = ""
lowest_rating_movie = ""
for number in range (number_movies):
    name_movie = input()
    rating = float(input())
    all_ratings += rating
    if rating > highest_rating:
        rating = highest_rating
        highest_rating_movie = name_movie
    elif rating < highest_rating:
        rating = lowest_rating
        if rating < lowest_rating:
            lowest_rating = rating
        lowest_rating_movie = name_movie
average = all_ratings / number_movies
print(f"{highest_rating_movie} is with highest rating: {highest_rating:.1f}")
print(f"{lowest_rating} is with lowest rating: {lowest_rating_movie:.1f}")
print(f"Average rating: {average:.1f}")


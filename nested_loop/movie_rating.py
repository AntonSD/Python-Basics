import sys

number_of_movies = int(input())
sum_of_ratings = 0
highest_rating = - sys.maxsize
movie_highest_rating = ""
lowest_rating = sys.maxsize
movie_lowest_rating = ""
for movies in range(1, number_of_movies + 1):
    title = input()
    rating = float(input())
    sum_of_ratings += rating
    if rating > highest_rating:
        highest_rating = rating
        movie_highest_rating = title
    if rating < lowest_rating:
        lowest_rating = rating
        movie_lowest_rating = title

average = sum_of_ratings / number_of_movies
print(f"{movie_highest_rating} is with highest rating: {highest_rating:.1f}")
print(f"{movie_lowest_rating} is with lowest rating: {lowest_rating:.1f}")
print(f"Average rating: {average:.1f}")



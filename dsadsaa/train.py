number_of_jury = int(input())
presentation = input()
overall_rating = 0
presentations = 0
while presentation != "Finish":
    rating_per_presentation = 0
    presentations += 1

    for jury in range(1, number_of_jury + 1):
        rating = float(input())
        rating_per_presentation += rating
    average_rating_per_present = rating_per_presentation / number_of_jury
    print(f"{presentation} - {average_rating_per_present:.2f}.")
    overall_rating += average_rating_per_present
    presentation = input()
average = overall_rating / presentations
print(f"Student's final assessment is {average:.2f}.")




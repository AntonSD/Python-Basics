book = input()
books = 0
text = input()
book_is_found =False
while text != "No More Books":
    if text == book:
        book_is_found = True
        break
    books += 1
    text = input()
if book_is_found:
    print(f"You checked {books} books and found it.")
else:
    print("The book you search is not here!")
    print(f"You checked {books} books.")
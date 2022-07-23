username = input()
password = input()

current_pass = input()

while current_pass != password:
    current_pass = input()


print("Welcome " + username + "!")
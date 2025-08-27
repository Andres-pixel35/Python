from datetime import date
import random
from helpers import files, classess
import sys


# exit values: 1: File error, 2: input error

first_time = ""
if files.is_file_empty("users.csv"):
    first_time = True
else:
    first_time = False

today = date.today()

library = classess.Library("Cosmos Library")
list_users = []
if not first_time:
    try:
        dic_users = files.load_users("users.csv")
    except OSError as e:
       print(f"Operating system error occurred: {str(e)}")
       sys.exit(1)

    list_users = [classess.User(**user_data) for user_data in dic_users]

    for user in list_users:
        library.add_user(user)

    library.list_current_users()

options = {1: "Register", 2: "Donate a book", 3: "Search a book", 4: "Search an user", 5: "Borrow a book", 6: "Return a book", 7: "exit"}

print(f"=== Welcome to {library} ===")
print("\nThings you can do here: ")
for i in range(1,7):
    print(f"{i}: {options[i]}")

option = 0
while not option == 7:
    option = input("Please choose your option: ")

    try:
        option = int(option)
    except ValueError as e:
        print(f"Error: {str(e)}")
        sys.exit(2)


    match option:
        case 1: 
            id_random = f"{random.randint(0, 999):03d}"

            register_user = ["Name", "Surname", "Email"]
            values_user = []

            for register in register_user:
                values_user.append(input(f"{register}: "))

            user = classess.User(values_user[0].capitalize(), values_user[1].capitalize(), values_user[2], today, id_random)

            library.add_user(user)
            library.list_current_users()

            files.add_user_csv("users.csv", user, first_time)

book1 = classess.Book("Kusuriya", "Andres", "123-456-789", "Cinema", 2011)

usuario = files.search_by_name(list_users, "Castro")

print(usuario.borrow_book(book1))

usuario.list_borrowed_books()

print(usuario.borrow_book(book1))


"""
id_random = f"{random.randint(0, 999):03d}"

register_user = ["Name", "Surname", "Email"]
values_user = []

for register in register_user:
    values_user.append(input(f"{register}: "))

user1 = classess.User(values_user[0].capitalize(), values_user[1].capitalize(), values_user[2], today, id_random)

library.add_user(user1)
library.list_current_users()

files.add_user_csv("users.csv", user1, first_time)"""

from datetime import date
import random
from helpers import files, classess
import sys

# exit values: 1: File error, 2: input error
# files names:
initial_inventory = "initial_inventory.csv"
inventory = "inventory.csv"
users_csv = "users.csv"

def register_user():
                
    first_user = files.is_file_empty(users_csv)
    id_random = f"{random.randint(0, 999):03d}"
    today = date.today()

    register_user = ["Name", "Surname", "Email"]
    values_user = []

    for register in register_user:
        values_user.append(input(f"{register}: "))

    user = classess.User(values_user[0].title(), values_user[1].title(), values_user[2].lower(), today, id_random)

    library.add_user(user)

    try:
        files.add_user_csv(users_csv, user, first_user)
    except OSError as e:
        print(f"Operating system error occurred: {str(e)}")
        sys.exit(1)

    print(f"The user {user.name + " " + user.surname} has been registered successfully.")

library = classess.Library("Cosmos Library")

first_time = ""
if files.is_file_empty(inventory):
    first_time = True
else:
    first_time = False

if not first_time:
    try:
        dic_users = files.load_information(users_csv)
        dic_books = files.load_information(inventory)
    except OSError as e:
       print(f"Operating system error occurred: {str(e)}")
       sys.exit(1)

    list_users = [classess.User(**user_data) for user_data in dic_users]
    list_books = [classess.Book(**book_data) for book_data in dic_books]

    for user in list_users:
        library.add_user(user)
    
    for book in list_books:
        library.add_books(book)
else:
    try:
        dic_books = files.load_information(initial_inventory)
    except OSError as e:
        print(f"Operating system error occurred: {str(e)}")
        sys.exit(1)

    list_books = [classess.Book(**book_data) for book_data in dic_books]

    try:
        for book in list_books:
            files.add_book_csv(inventory, book, first_time)
            first_time = False
    except OSError as e:
        print(f"Operating system error occurred: {str(e)}")
        sys.exit(1)


options = {1: "Register", 
           2: "Donate a book", 
           3: "Search a book", 
           4: "Search an user", 
           5: "Borrow a book", 
           6: "Return a book", 
           7: "Show availables books",
           8: "Show borrowed books",
           9: "Exit"}

print(f"=== Welcome to {library} ===")
print("\nThings you can do here: ")
for i in range(1,10):
    print(f"{i}: {options[i]}")

option = 0
while not option == 9:
    option = input("\nPlease choose your option: ")

    try:
        option = int(option)
    except ValueError as e:
        print(f"Error: {str(e)}")
        sys.exit(2)

    match option:
        case 1: 
            register_user()

        case 2:
            donate_book = ["Title", "Author", "ISBN", "Genre", "Year (e.g 2010)"]
            values_book = []
            for donate in donate_book:
                values_book.append(input(f"{donate}: "))

            try:
                values_book[-1] = int(values_book[-1])
            except ValueError:
                print(f"You must enter an int for the year of the book. You entered \"{values_book[-1]}\"")
                sys.exit(2)
            
            book = classess.Book(values_book[0].title(), values_book[1].title(), values_book[2], values_book[3].title(), values_book[4])

            library.add_books(book)

            try:
                files.add_book_csv(inventory, book, first_time)
            except OSError as e:
                print(f"Operating system error occurred: {str(e)}")
                sys.exit(1)
            
            print(f"The book \"{book.title}\" has been donated successfully.\nFrom {library.name} we thank you enormously")

        case 3:
            title = input("Please enter the name of the book you want to search: ")
            library.search_book(title)

        case 4:
            name = input("Please enter the name and the surname of the user you want to search and know their current books: ")

            user = library.search_users(name)
            if not user == None:
                user.list_borrowed_books()

        case 5:
            name = input("Please enter your name and surname: ")
            user = library.search_users(name)
            if user == None:
                print(f"The user called {name.title()} is not registered in our library."
                      " Do you want to register now?: ", end="")
                choose = input("(y/n) ")
                match choose.lower():
                    case "y":
                        register_user()
                    case "n":
                        print("User no registered, what do you want to do now?")
                        continue
                    case _:
                        print("Invalid option, closing system.")
                        sys.exit(2)
            
            title = input("\nPlease enter the name of the book you want to borrow: ")

            book = library.search_book(title)
            if not book:
                continue

            print("Are you sure you want to borrow this boook? ", end="")
            choose = input("(y/n) ")
            match choose.lower():
                case "y":
                    print(user.borrow_book(book))
                case "n":
                    continue
                case _:
                    print("Invalid option, closing system.")
                    sys.exit(2)
        
        case 6:
            name = input("Please enter your name and surname: ")
            user = library.search_users(name)
            if user == None:
                print(f"The user called {name.title()} is not registered in our library."
                      " Do you want to register now?: ", end="")
                choose = input("(y/n) ")
                match choose.lower():
                    case "y":
                        register_user()
                        continue
                    case "n":
                        print("User no registered, what do you want to do now?")
                        continue
                    case _:
                        print("Invalid option, closing system.")
                        sys.exit(2)
                
            title = input("\nPlease enter the name of the book you want to return: ")

            book = library.search_book(title)
            if not book:
                continue

            print("Are you sure you want to return this boook? ", end="")
            choose = input("(y/n) ")
            match choose.lower():
                case "y":
                    user.return_book(book)
                case "n":
                    continue
                case _:
                    print("Invalid option, closing system.")
                    sys.exit(2)

        case 7:
            print("\n=== AVAILABLE BOOKS ===")
            library.list_available_books()
        
        case 8:
            print("\n=== BORROWED BOOKS ===")
            library.list_borrowed_books()
        
        case 9:
            continue

        case _:
            print("Invalid option, closing system.")
            sys.exit(2)



from datetime import date
from dateutil.relativedelta import relativedelta

class Book:
    def __init__(self, title, author, isbn, genre, year: int):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.genre = genre
        self.year = year
        self.available = True
        self.borrower = ""
        self.borrow_date = ""
        self.deadline = ""

    def borrow(self):
        if self.available:
            self.available = False
            today = date.today()
            next_month = today + relativedelta(months=1)
            self.borrow_date = today
            self.deadline = next_month
            return True
        else:
            return False
    
    def return_book(self):
        if not self.available:
            self.available =  True
            self.borrow_date = ""
            self.deadline = ""
            return True
        else:
            return False
        
    def check_availability(self):
        if self.available:
            return "Available"
        else:
            return "Not available"
        
    def __str__(self):
        if self.available:
            return f"\"{self.title}\" by {self.author}, release date: {self.year}"
        else:
            return f"\"{self.title}\" by {self.author} was borrowed at {self.borrow_date}. It has to be returned by {self.deadline}"
    
class User:
    def __init__(self, name, surname, email, register_date, user_id,):
        self.name = name
        self.surname = surname
        self.email = email
        self.register_date = register_date
        self.user_id = user_id
        self.books = []

    def borrow_book(self, book):
        if not book.available:
            return f"The book \"{book.title}\" is not available. It's currently under {book.borrower}'s possession.\nDetails: {book}"
        elif len(self.books) == 10:
            return "You cannot borrow more than 10 books at the same time"
    
        book.borrow()
        book.borrower = self

        self.books.append(book)
        return f"The user {self.name} has borrowed the book \"{book.title}\". It has to be returned by {book.deadline}"

    def return_book(self, book):
        try:
            self.books.remove(book)
            book.return_book()
            book.borrower = ""
            print(f"The user {self.name} {self.surname} has returned the book \"{book.title}\"")
        except ValueError:
            print("You can not return a book that you have not borrowed")
    
    def list_borrowed_books(self):
        if not self.books:
            print(f"{self.name} {self.surname} has not borrowed books")
        else:
            for book in self.books:
                print(book)

    def __str__(self):
        return f"{self.name} {self.surname}"
    
class Library:
    def __init__(self, name):
        self.name = name
        self.users = []
        self.books = []

    def add_books(self, book):
        self.books.append(book)

    def add_user(self, user):
        self.users.append(user)

    def list_current_users(self):
        if not self.users:
            print(f"{self.name} has zero registered users.")
        else:
            for user in self.users:
                print(user)

    def search_users(self, name):
        for user in self.users:
            if name.lower() == user.name.lower() + " " + user.surname.lower():
                return user
            
        print(f"The user {name.title()} has not been found.")
        return None
    
    def list_available_books(self):
        if not any(book.available for book in self.books):
            print(f"The {self.name} does not have any book available right now.")
        else:
            for book in self.books:
                if book.available:
                    print(book)

    def list_borrowed_books(self):
        if not any(not book.available for book in self.books):
            print(f"The {self.name} currently has no books lent.")
        else:
            for book in self.books:
                if not book.available:
                    print(book)

    def search_book(self, title):
        for book in self.books:
            if title.lower() == book.title.lower():
                print(book)
                return book
            
        print(f"The book \"{title}\" has not been found. It is not part of our catalog.")
        return False
    
    def __str__(self):
        return f"{self.name.capitalize()}"
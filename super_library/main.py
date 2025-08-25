from datetime import date
from dateutil.relativedelta import relativedelta
import csv

class Book:
    def __init__(self, title, author, ISBN, genre, year: int):
        self.title = title
        self.author = author
        self.isbn = ISBN
        self.year = year
        self.genre = genre
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
            return f"{self.title} by {self.author}"
        else:
            return f"{self.title} by {self.author} borrowed at {self.borrow_date}. It has to be returned by {self.deadline}"
    
class User:
    def __init__(self, name, surname, email, register_date, user_id):
        self.name = name
        self.surname = surname
        self.email = email
        self.register_date = register_date
        self.user_id = user_id
        self.books = []

    def borrow_book(self, book):
        if not book.available:
            return f"The book '{book.title}' is not available"
        elif len(self.books) >= 3:
            return "You cannot borrow more than 3 books at the same time"
    
        book.borrow()
        book.borrower = self

        self.books.append(book)
        return f"The user {self.name} has borrowed the book '{book.title}'"

    
    def return_book(self, book):
        try:
            self.books.remove(book)
            book.return_book()
            book.borrower = ""
            print(f"The user {self.name} {self.surname} has returned the book {book.title}")
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

    def list_current_users(self):
        if not self.users:
            print(f"{self.name} has zero registered user.")
        else:
            for user in self.users:
                print(user)

    def search_users(self, name):
        for user in self.users:
            if name.lower() == user.name.lower() + " " + user.surname.lower():
                print(f"The user {name} has the following books borrowed currently: ")
                user.list_borrowed_books()
                return True
            
        print(f"The user {name} has not been found.")
        return False
    
    def list_available_books(self):
        if not any(book.available for book in self.books):
            print(f"The {self.name} does not have any book available right now.")
        else:
            for book in self.books:
                if book.available:
                    print(book)

    def list_borrowed_books(self):
        if not any(not book.availble for book in self.books):
            print(f"The {self.name} currently has no books lent.")
        else:
            for book in self.books:
                if not book.avalibale:
                    print(book)






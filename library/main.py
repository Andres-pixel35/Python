# EXERCISE: Library Management System
# Create the following classes to manage a library:

# 1. Book Class
class Book:
    def __init__(self, title, author, isbn, available=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available
    
    def borrow(self):
        if self.available:
            self.available = False
            return True
        else:
            return False
    
    def return_book(self):
        if not self.available:
            self.available = True
            return True
        else:
            return False
        
    def check_availability(self):
        if self.available:
            return "Available"
        else:
            return "Not available"
            
    def __str__(self):
        return f"{self.title} by {self.author}"

# 2. User Class
class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.books = []
    
    def borrow_book(self, book):
        if not book.available:
            return f"The book '{book.title}' is not available"
        elif len(self.books) >= 3:
            return "You cannot borrow more than 3 books at the same time"
    
        book.borrow()
        self.books.append(book)
        return f"The user {self.name} has borrowed the book '{book.title}'"

    
    def return_book(self, book):
        try:
            self.books.remove(book)
            book.return_book()
            print(f"The user {self.name} has returned the book {book.title}")
        except ValueError:
            print("You can not return a book that you have not borrowed")
    
    def list_borrowed_books(self):
        if not self.books:
            print(f"{self.name} has not borrowed books")
        else:
            for book in self.books:
                print(f"{book.title} by {book.author}")

# 3. Library Class
class Library:
    def __init__(self, name):
        self.name = name
        self.users = []
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
    
    def register_user(self, user):
        self.users.append(user)
    
    def search_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return f"The book {book.title} by {book.author} has been found and it's {book.check_availability().lower()} to borrow"
        
        return f"The book {title} has not been found"
    
    def list_available_books(self):
        if not any(book.available for book in self.books):
            print(f"The {self.name} does not have any book available right now")
        else:
            for book in self.books:
                if book.available:
                    print(f"{book.title} by {book.author}")

# TEST CODE 

# Create a library
my_library = Library("Central Library")

# Create some books
book1 = Book("One Hundred Years of Solitude", "Gabriel García Márquez", "978-84-376-0494-7")
book2 = Book("1984", "George Orwell", "978-84-376-0495-4")
book4 = Book("Dune","Frank Herbert", "978-044-117-271-9")

# Add books to the library
my_library.add_book(book1)
my_library.add_book(book2)
my_library.add_book(book4)

# Create a user
user1 = User("Anna Garcia", "U001")
my_library.register_user(user1)

# Test functionalities
print("=== AVAILABLE BOOKS ===")
my_library.list_available_books()

print("\n=== BORROWING BOOKS ===")
print(user1.borrow_book(book1))
print(user1.borrow_book(book2))
print(user1.borrow_book(book4))

print("\n=== USER'S BOOKS ===")
user1.list_borrowed_books()

print("\n=== AVAILABLE BOOKS AFTER BORROWING ===")
my_library.list_available_books()
"""
print("\n=== RETURNING BOOKS ===")
user1.return_book(book1)

print("\n=== AVAILABLE BOOKS AFTER RETURNING ===")
my_library.list_available_books()
"""
print("\n=== SEARCH BOOKS ===")
print(my_library.search_book("DUNE"))
print(my_library.search_book("Kusuriya no hitorigoto"))

print("=== PRINT BOOKS ===")
print(book4)

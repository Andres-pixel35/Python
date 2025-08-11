class book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
        self.available = True

    def sell(self):
        if self.available:
            self.available = False
            print(f"The book {self.title} has been sold for {self.price} dollars")
        else:
            print(f"The book {self.title} is no longer under our possession")

class user:
    def __init__(self, name, cash):
        self.name = name
        self.cash = cash
        self.bought_books = []

    def buy(self, book):
        if self.cash >= book.price and book.available:
            book.sell()
            self.cash = self.cash - book.price
            self.bought_books.append(book)
        elif self.cash < book.price:
            print(f"You do not have enough money to buy {book.title}")
        elif not book.available:
            print(f"The book {book.title} is no longer available")

    def myBooks(self):
        if not self.bought_books:
            print("My books are: \nYou do not have books yet.")
        else:
            print("My books are: ")
            for book in self.bought_books:
                print(f"{book.title} by {book.author} bought for {book.price}")

class bookShop:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"The book {book.title} has been added")

    def show_books_available(self):
        print("Available books: ")

        if not self.books:
            print("The book shop does not have more book available")
        else:
            for book in self.books:
                if book.available:
                    print(f"{book.title} by {book.author} for {book.price} dollars")

    def show_books_sold(self):
        print("Books sold: ")

        if not any(not book.available for book in self.books):
            print("The book shop has not sold any book yet")
        else:
            for book in self.books:
                if not book.available:
                    print(f"{book.title} by {book.author} sold for {book.price} dollars")

# books
book1 = book("Kusuriya no Hitorigoto", "Natsu Hyuga", 50)
book2 = book("Adachi to Shimamura", "Hitoma Iruma", 35)
book3 = book("Honzuki no Gekokujou", "Miya Kazuki", 100)
book4 = book("Youjo Senki", "Carlo Zen", 75)

#users
user1 = user("Andres", 50)

#book shop
book_shop = bookShop()
book_shop.add_book(book1)
book_shop.add_book(book2)
book_shop.add_book(book3)
book_shop.add_book(book4)

user1.buy(book3)
user1.buy(book1)
user1.buy(book2)
user1.buy(book4)

user1.myBooks()
book_shop.show_books_available()
book_shop.show_books_sold()






    
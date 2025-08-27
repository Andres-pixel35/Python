import csv
import os

def add_user_csv(filename, user, firs_user):
    desired_fields = {k: v for k, v in vars(user).items() if k != "books"}
    user_data = {field: getattr(user, field) for field in desired_fields}
    with open(filename, mode="a", encoding="utf-8", newline="") as file:
        fieldnames = desired_fields.keys()
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        if firs_user:
            writer.writeheader()

        writer.writerow(user_data)
    
def is_file_empty(filename):
    return os.path.getsize(filename) == 0

def load_information(filename):
    with open(filename, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        list = []
        for x in reader:
            list.append(x)
        return list
    
def add_book_csv(filename, book, first_time):
    desired_fields = ["title", "author", "isbn", "genre", "year"]
    book_data = {field: getattr(book, field) for field in desired_fields}
    with open(filename, mode="a", newline="", encoding="utf-8") as file:
        fieldnames = desired_fields
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        if first_time:
            writer.writeheader()
        
        writer.writerow(book_data)
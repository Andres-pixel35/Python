import csv
import os

def add_user_csv(filename, user, firs_time):
    try:
        with open(filename, mode="a", encoding="utf-8", newline="") as file:
            fieldnames = vars(user).keys()
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            if firs_time:
                writer.writeheader()

            writer.writerow(vars(user))

    except ValueError:
        return ValueError
    
def is_file_empty(filename):
    return os.path.getsize(filename) == 0
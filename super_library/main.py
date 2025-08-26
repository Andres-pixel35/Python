from datetime import date
import random
from helpers import files, classess
    

first_time = ""
if files.is_file_empty("users.csv"):
    first_time = True
else:
    first_time = False

today = date.today()
id_random = f"{random.randint(0, 999):03d}"

register_user = ["Name", "Surname", "Email"]
values_user = []

for register in register_user:
    values_user.append(input(f"{register}: "))


library = classess.Library("Cosmos Library")

user1 = classess.User(values_user[0], values_user[1], values_user[2], today, id_random)

library.add_user(user1)
library.list_current_users()

files.add_user_csv("users.csv", user1, first_time)


print(values_user)

    






"""with open("code_geass_script.txt", "r") as file:
    lines = [line.strip() for line in file]

    print(lines[:11])"""
        
"""newtext = input("What do you want to add: ")
with open("code_geass_script.txt", "a") as file:
    file.write(f"\n\n{newtext}")"""

with open("code_geass_script.txt", "r") as file:
    lines = file.readlines()

    print(len(lines))

    
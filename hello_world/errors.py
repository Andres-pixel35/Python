dollars = input("Changed owed: ")

while True:
    try:
        while float(dollars) < 0:
            print("You must enter a number greater than 0 or 0 itself")
            dollars = input("Changed owed: ")
        break
    except ValueError:
        print("You must enter a positive float or a positive integer")
        dollars = input("Changed owed: ")

numerator = input("Enter a number ")
divisor = input("Enter a number: ")

while True:
    try:
        while float(divisor) == 0:
            print("You must enter a number different to 0")
            divisor = input("Enter a number: ")
        break
    except ValueError:
        print("You must enter a number.")
        divisor = input("Enter a number: ")


print(float(numerator) / float(divisor))
        
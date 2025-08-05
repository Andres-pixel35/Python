for i in range(11):
    i = i * i
    print(i)

print("comprehesion")

squares = [x**2 for x in range(1,11)]
print("Squares =", squares)

print("fahrenheit")
celcius = [0, 10, 20, 30, 40]

fahrenheit = [(temp * 9/5) + 32 for temp in celcius]

print(fahrenheit)

print("even numebers")

evens = [x for x in range(1, 21) if x % 2 == 0]
print(evens)

print("od numbers")

odds = [x for x in range(2, 21) if x % 2 != 0]
print(odds)
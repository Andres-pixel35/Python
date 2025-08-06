add = lambda a, b: a + b

# print(add(10, 20))

numbers = range(11)

squares = list(map(lambda x: x * x, numbers))

#print(squares)

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

#print(even_numbers)

names = ["Andres", "Daniela", "Castro", "Cosmos", "Lelouch", "Ana", "CC"]

short_names = list(filter(lambda x: len(x) < 4, names))

print(short_names)
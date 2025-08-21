import random

random_number = random.randint(1, 10)
print(random_number)

colors = ["azul", "rojo", "amarillo"]
random_color = random.choice(colors)
print(random_color)

cards = ["as", "rey", "reina", "jota", "10"]
random.shuffle(cards)

print(cards)
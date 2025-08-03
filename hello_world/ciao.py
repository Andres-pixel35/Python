a = 5
b = a

print(id(a))
print(id(b))

a = a - 5

print(a)
print(b)

print(id(a))
print(id(b))

i = "Andres"
you = i

print(id(i))
print(id(you))

i = "Andres Felipe"

print(i)
print(you)

print(id(i))
print(id(you))
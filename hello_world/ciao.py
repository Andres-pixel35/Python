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

print("Here starts the list")

names = ["Andres", "Cosmos"]
nombres = names
print(id(names))
print(id(nombres))

names.append("Cosmos")
print(id(names))
print(id(nombres))
print(names)
print(nombres)

print("Here is the new variable")
名字 = names[:]
print(id(names))
print(id(名字))
print(names)
print(名字)

del names[-1]
print(id(names))
print(id(名字))
print(names)
print(名字)



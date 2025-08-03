print("Hello world")

name = "Andres"

print(name[0])
print(name[2:])
print(name[2:-1])
print(name[2:-2])
print(name)

name = "Andres Felipe"
print(name)

names = ["Andres", "Cato"]
print(names)

names.append("Daniela")
print(names)

names.insert(2, "Cosmos")
print(names)
print(names.index("Daniela"))

del names[-1]
print(names)
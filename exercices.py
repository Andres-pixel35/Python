numbers = [1,2,3,4,5]

double = [x * 2 for x in numbers]

# print(double)

words = ["sol", "mar", "montaña", "rio", "estrella"]

filter = [x.upper() for x in words if len(x) > 3]

# print(filter)

keys = ["nombre", "edad", "ocupación"]

values = ["Juan", 30, "Ingeniero"]

dictionari = {keys[i]: values[i] for i in range(len(keys))}
# print(dictionari)

numbers_2 = [1,2,3,4,5,6,7,8,9,10]

double_2 = [x * 2 if x % 2 == 0 else x for x in numbers_2]
print(double_2)



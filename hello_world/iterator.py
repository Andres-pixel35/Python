my_list = [1,2,3,4,5]

it = iter(my_list)

print(next(it))
print(next(it))

def my_generator():
    yield 5
    yield 6
    yield 7

for x in my_generator():
    print(x)

print("Fibonacci")

def fibonacci(limit):
    a, b = 0, 1

    while a < limit:
        yield a
        a, b = b, a + b

for x in fibonacci(100):
    print(x)
def sum_numbers(*args):
    return sum(args)

print(sum_numbers(1,2,3,4,5,6,7,8,9,10))
print(sum_numbers(1,2))
print(sum_numbers(1,2,3,4,5))

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key.capitalize()}: {value}")

print_info(name="Eren Jaeger", age=2000, city="Eldia")


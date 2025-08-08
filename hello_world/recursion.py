print("FACTORIAL:")
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
for x in range(11):
    print(f"The factorial of {x} is: {factorial(x)}")

print("SUM:")
def sum(a):
    if a == 0:
        return 0
    else:
        return a + sum(a - 1)
    
for i in range(11):
    print(f"The sum of {i} is: {sum(i)}")
print("Usage: you must enter your expenses as the following:\nrent: 2000")

income = int(input("What's your monthly income? "))

expenses = {}

for _ in range(5):
    expense = input("Enter expense: ")
    category, amount = expense.split(": ")
    expenses[category] = int(amount)

total = sum(expenses.values())

spare = income - total

print(f"Monthly income: {income}\nExpenses:")

for key, value in expenses.items():
    print(f"- {key}: {value}")

print(f"Total expenses: {total}")
print(f"Remaining balance: {spare}")
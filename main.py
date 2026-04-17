import json

expenses = []

try:
    with open("expenses.json", "r") as f:
        expenses = json.load(f)
except:
    expenses = []

amount = input("Enter amount: ")
category = input("Enter category: ")

amount = float(amount)

expense = {
    "amount": amount,
    "category": category
}

expenses.append(expense)

print("Expense added successfully!")
print(expenses)

# Function Equivalent of the above code

# def add_expense():
#     amount = input("Enter amount: ")
#     category = input("Enter category: ")
#     amount = float(amount)
#     expense = {
#         "amount": amount,
#         "category": category
#     }
#     expenses.append(expense)
#     print("Expense added successfully!")
#     print(expenses)

# To save the expenses to a file

with open("expenses.json", "w") as f:
    json.dump(expenses, f)

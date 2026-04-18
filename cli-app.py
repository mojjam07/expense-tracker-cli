# Function to add expense
def add_expense(expenses):
    try:
        amount = float(input("Enter amount: "))
        category = input("Enter category: ")

        expense = {
            "amount": amount,
            "category": category
        }

        expenses.append(expense)
        save_expenses(expenses)

        print("Expense added successfully!")

    except ValueError:
        print("Invalid amount. Please enter a number.")

# Function to view expenses
def view_expenses(expenses):
    if not expenses:
        print("No expenses found.")
        return

    print("\nAll Expenses:")
    for exp in expenses:
        print(f"{exp['category']}: {exp['amount']}")

    total = sum(exp["amount"] for exp in expenses)
    print(f"\nTotal: {total}")

# Function to save expenses
def save_expenses(expenses):
    import json
    with open("expenses.json", "w") as f:
        json.dump(expenses, f)

# Function to load expenses
def load_expenses():
    import json
    try:
        with open("expenses.json", "r") as f:
            return json.load(f)
    except:
        return []

expenses = load_expenses()

while True:
    print("\nExpense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_expense(expenses)
    elif choice == "2":
        view_expenses(expenses)
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Try again.")
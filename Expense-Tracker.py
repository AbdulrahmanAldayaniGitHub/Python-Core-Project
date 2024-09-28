expenses = []

def add_expense(amount, category):
    expense = {'amount': amount, 'category': category}
    expenses.append(expense)
    print(f"Added: {expense}")

def view_expenses():
    total = sum(item['amount'] for item in expenses)
    print(f"Total expenses: ${total}")
    for expense in expenses:
        print(f"${expense['amount']} - {expense['category']}")

def save_expenses(filename):
    with open(filename, 'w') as f:
        for expense in expenses:
            f.write(f"{expense['amount']},{expense['category']}\n")
    print("Expenses saved to file")

add_expense(100, "Food")
add_expense(50, "Transport")
view_expenses()
save_expenses("expenses.txt")

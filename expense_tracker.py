# expense_tracker.py

transactions = []

def add_transaction(amount, category, type):
    transactions.append({"amount": amount, "category": category, "type": type})

def show_transactions():
    print("\n---- All Transactions ----")
    for t in transactions:
        print(f"{t['type']} - {t['category']} : {t['amount']}")

def get_balance():
    income = sum(t["amount"] for t in transactions if t["type"] == "Income")
    expense = sum(t["amount"] for t in transactions if t["type"] == "Expense")
    return income - expense

while True:
    print("\n===== Expense Tracker =====")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. Show Transactions")
    print("4. Show Balance")
    print("5. Exit")
    choice = int(input("Enter choice: "))
    
    if choice == 1:
        amt = int(input("Enter amount: "))
        cat = input("Enter category: ")
        add_transaction(amt, cat, "Income")
    elif choice == 2:
        amt = int(input("Enter amount: "))
        cat = input("Enter category: ")
        add_transaction(amt, cat, "Expense")
    elif choice == 3:
        show_transactions()
    elif choice == 4:
        print("Current Balance:", get_balance())
    elif choice == 5:
        print("Goodbye! 👋")
        break

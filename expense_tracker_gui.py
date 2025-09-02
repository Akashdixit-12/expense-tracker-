# expense_tracker_gui.py
import tkinter as tk
from tkinter import messagebox

transactions = []

def add_transaction():
    amount = amount_entry.get()
    category = category_entry.get()
    t_type = type_var.get()
    
    if amount.isdigit():
        transactions.append({"amount": int(amount), "category": category, "type": t_type})
        update_listbox()
        amount_entry.delete(0, tk.END)
        category_entry.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Amount must be a number")

def update_listbox():
    listbox.delete(0, tk.END)
    for t in transactions:
        listbox.insert(tk.END, f"{t['type']} - {t['category']} : {t['amount']}")

def show_balance():
    income = sum(t["amount"] for t in transactions if t["type"] == "Income")
    expense = sum(t["amount"] for t in transactions if t["type"] == "Expense")
    balance = income - expense
    messagebox.showinfo("Balance", f"Your Balance: {balance}")

root = tk.Tk()
root.title("Expense Tracker")

tk.Label(root, text="Amount:").grid(row=0, column=0)
amount_entry = tk.Entry(root)
amount_entry.grid(row=0, column=1)

tk.Label(root, text="Category:").grid(row=1, column=0)
category_entry = tk.Entry(root)
category_entry.grid(row=1, column=1)

type_var = tk.StringVar(value="Expense")
tk.Radiobutton(root, text="Income", variable=type_var, value="Income").grid(row=2, column=0)
tk.Radiobutton(root, text="Expense", variable=type_var, value="Expense").grid(row=2, column=1)

tk.Button(root, text="Add Transaction", command=add_transaction).grid(row=3, column=0, columnspan=2)
tk.Button(root, text="Show Balance", command=show_balance).grid(row=4, column=0, columnspan=2)

listbox = tk.Listbox(root, width=40)
listbox.grid(row=5, column=0, columnspan=2)

root.mainloop()

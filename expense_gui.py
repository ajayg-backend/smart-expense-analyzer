import json

def save_data():
    with open("expenses.json", "w") as f:
        json.dump(expenses, f)

def load_data():gi
    global expenses
    try:
        with open("expenses.json", "r") as f:
            expenses = json.load(f)

        for e in expenses:
            expense_list.insert(
                tk.END,
                f'{e["item"]} | {e["amount"]} | {e["category"]}'
            )

    except:
        expenses = []

import tkinter as tk
import matplotlib.pyplot as plt
import csv

root = tk.Tk()
window_width = 400
window_height = 500

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

root.geometry(f"{window_width}x{window_height}+{x}+{y}")
root.title("Expense Tracker - Personal Finance App")
root.geometry("400x450")

expenses = []

tk.Label(root, text="Item").pack()
item_entry = tk.Entry(root)
item_entry.pack()
item_entry.bind("<Return>", lambda event: amount_entry.focus())

tk.Label(root, text="Amount").pack()
amount_entry = tk.Entry(root)
amount_entry.pack()
amount_entry.bind("<Return>", lambda event: category_entry.focus())

tk.Label(root, text="Category").pack()
category_entry = tk.Entry(root)
category_entry.pack()
category_entry.bind("<Return>", lambda event: add_expense())


expense_list = tk.Listbox(root, width=45, height=10)
expense_list.pack(pady=10)

total_label = tk.Label(root, text="Total Expense: 0", font=("Arial", 12, "bold"))
total_label.pack()

def save_data():
    with open("expenses.json", "w") as file:
        json.dump(expenses, file)

def update_total():
    total = sum(e["amount"] for e in expenses)
    total_label.config(text=f"Total Expense: {total}")
                                                             

def add_expense():

    item = item_entry.get()
    amount = int(amount_entry.get())
    category = category_entry.get()

    expense = {
        "item": item,
        "amount": amount,
        "category": category
    }
    expenses.append(expense)
    
    expense_list.insert(tk.END, f"{item} | {amount} | {category}")

    save_data()
    update_total()

def delete_expense():
    selected = expense_list.curselection()

    if selected:
        index = selected[0]
        
        expense_list.delete(index)
        expenses.pop(index)

        update_total()

def show_graph():

    category_totals = {}

    for e in expenses:
        cat = e["category"]
        amt = e["amount"]

        if cat in category_totals:
            category_totals[cat] += amt

        else:
            category_totals[cat] = amt

def show_pie_chart():

    category_totals = {}

    for e in expenses:
        cat = e["category"]
        amt = e["amount"]

        if cat in category_totals:
            category_totals[cat] += amt

        else:
            category_totals[cat] = amt

    plt.pie(
        category_totals.values(),
            labels=category_totals.keys(),
            autopct='%1.1f%%'
    )
    
    plt.title("Expense Distribution")
    plt.show()
    
    plt.bar(category_totals.keys(), category_totals.values())
    plt.title("Expenses by Category")
    plt.xlabel("Category")
    plt.ylabel("Amount")
    plt.show()

def export_csv():

    with open("expenses.csv", "w", newline="") as file:
    
         writer = csv.writer(file)
    
         writer.writerow(["item", "Amount", "Category"])

         for e in expenses:
            writer.writerow([e["item"], e["amount"], e["category"]])

def load_data():

    global expenses

    try:
        with open("expenses.json", "r") as file:
            expenses = json.load(file)

        for e in expenses:
            expense_list.insert(
                tk.END,
                f'{e["item"]} | {e["amount"]} | {e["category"]}'
            )
    
    except:
        expenses = []

def search_expense():

    keyword = search_entry.get().lower()

    expense_list.delete(0, tk.END)

    for e in expenses:
        if keyword in e["item"].lower() or keyword in e["category"].lower():
            expense_list.insert(
                tk.END,
                f'{e["item"]} | {e["amount"]} | {e["category"]}'
            )

tk.Label(root, text="Search").pack()

search_entry = tk.Entry(root, width=25)
search_entry.pack(pady=5)

search_entry.bind("<Return>", lambda e: search_expense())

def show_all_expenses():

    expense_list.delete(0, tk.END)

    for e in expenses:
        expense_list.insert(
            tk.END,
            f'{e["item"]} | {e["amount"]} | {e["category"]}'
        )

tk.Button(root, text="Search Expense", command=search_expense).pack(pady=5)

tk.Button(root, text="Show All Expenses", command=show_all_expenses).pack(pady=5)

tk.Button(root, text="Add Expense", width=20, command=add_expense).pack(pady=5)

tk.Button(root, text="Delete Expense", width=20, command=delete_expense).pack(pady=5) 

tk.Button(root, text="Show Graph", width=20, command=show_graph).pack(pady=5)

tk.Button(root, text="Export CSV", width=20, command=export_csv).pack(pady=5)

tk.Button(root, text="Show Pie Chart", width=20, command=show_pie_chart).pack(pady=5)



load_data()

root.mainloop()
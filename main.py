def add_expenses():
    name = input("expenses name:")
    amount = float(input("amount:"))
    category = input("category:")

    return {
        "name": name,
        "amount": amount,
        "category": category
    }

def show_total(expenses):
    total = sum(item["amount"]for item in expenses)
    print("total expenses:", total)

def show_all(expenses):
    if not expenses:
        print("No expenses added yet.")
        return
    
    print("\nAll expenses:")
    for i, item in enumerate(expenses, start=1):
        print(f"{i}. {item['name']} - {item['amount']} ({item['category']})")

def category_summary(expenses):
    if not expenses:
        print("No expenses added yet.")
        return
    summary = {}

    for item in expenses:
        cat = item["category"]
        summary[cat] = summary.get(cat, 0) + item["amount"]

    print("\nCategory Summary:")
    for cat, total in summary.items():
        print(f"{cat}: {total}")
              

def main():
    expenses = []

    while True:
        print("\n1. Add Expenses")
        print("2. show total")
        print("3. show all expenses")
        print("4. category summary")
        print("5. exit")

        choice = input("choose option:")

        if choice == "1":
            expense = add_expenses()
            expenses.append(expense)

        elif choice == "2":
            show_total(expenses)

        elif choice == "3":
            show_all(expenses)

        elif choice == "4":
            category_summary(expenses)

        elif choice == "5":
            print("exiting...")
            break

        else:
            print("invalid choice")

if __name__ == "__main__":
    main()


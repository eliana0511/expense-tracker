# 💰 Expense Tracker (with Expense Names)
# Author: Ally
# Description: Menu-based expense tracker that records spending by name, category, and date, and saves data to a file.

import os

FILENAME = "expenses.txt"

def load_expenses():
    expenses = []
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            for line in file:
                date, name, category, amount = line.strip().split(",")
                expenses.append({"date": date, "name": name, "category": category, "amount": float(amount)})
    return expenses

def save_expenses(expenses):
    with open(FILENAME, "w") as file:
        for expense in expenses:
            file.write(f"{expense['date']},{expense['name']},{expense['category']},{expense['amount']}\n")

def add_expense(expenses):
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (e.g. Food, Bills, Shopping): ")
    name = input("Enter name/label for this expense (e.g. Starbucks coffee, Gas, Rent): ")
    try:
        amount = float(input("Enter amount spent: $"))
        expenses.append({"date": date, "name": name, "category": category, "amount": amount})
        save_expenses(expenses)
        print(f"✅ Expense '{name}' added successfully!")
    except ValueError:
        print("❌ Invalid amount! Please enter a number.")

def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded yet.")
        return
    print("\n📋 All Expenses:")
    total = 0
    for i, e in enumerate(expenses, 1):
        print(f"{i}. {e['date']} | {e['name']} | {e['category']} | ${e['amount']:.2f}")
        total += e["amount"]
    print(f"\n💵 Total Spent: ${total:.2f}")

def view_by_category(expenses):
    category = input("Enter category to view: ").capitalize()
    filtered = [e for e in expenses if e['category'].capitalize() == category]
    if not filtered:
        print(f"No expenses found for category '{category}'.")
        return
    total = sum(e['amount'] for e in filtered)
    print(f"\n📂 Expenses for {category}:")
    for e in filtered:
        print(f"- {e['date']} | {e['name']} | ${e['amount']:.2f}")
    print(f"Total: ${total:.2f}")

def show_menu():
    print("\n💰 Expense Tracker Menu")
    print("1. Add new expense")
    print("2. View all expenses")
    print("3. View expenses by category")
    print("4. Exit program")

def main():
    expenses = load_expenses()
    while True:
        show_menu()
        choice = input("\nEnter your choice (1-4): ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            view_by_category(expenses)
        elif choice == "4":
            print("\n👋 Goodbye! Keep tracking your spending wisely 💸")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()


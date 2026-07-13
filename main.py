from expense import Expense
from expense_manager import ExpenseManager

print("Welcome To Expense Tracker")

manager = ExpenseManager()

def print_menu() -> None:
    print("\nPlease select an option:")
    print("1. Add expense")
    print("2. Remove expense")
    print("3. View expenses")
    print("Enter 'b' anytime to go back to the main menu.")

def menu():
    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice not in ["1", "2", "3"]:
            print("Invalid choice. Please try again.")
            continue

        if choice == "1":
            category = input("Enter expense category: ")
            if category.lower() == 'b':
                continue
            title = input("Enter expense title: ")
            if title.lower() == 'b':
                continue
            amount = input("Enter expense amount: ")
            if amount.lower() == 'b':
                continue
            try:
                amount = float(amount)
                if amount < 0:
                    print("Amount cannot be negatie.")
                    continue
            except ValueError:
                print("Please enter a valid number")
                continue
            expense = Expense(category, title, amount)
            manager.add_expense(expense)
            print(f"Expense {category} - '{title}' of amount {amount} added successfully.")

        elif choice == "2":
            category = input("Enter expense category: ")
            if category.lower() == 'b':
                continue
            title = input("Enter expense title: ")
            if title.lower() == 'b':
                continue
            expense_to_remove = None
            for expense in manager.expenses:
                if expense.category == category and expense.title == title:
                    expense_to_remove = expense
                    break
            if expense_to_remove:
                manager.remove_expense(expense_to_remove)
                print(f"Expense {category} - '{title}' removed successfully.")
            else:
                print(f"No expense found with category '{category}' and title '{title}'.")

        elif choice == "3":
            manager.print_expenses()

menu()
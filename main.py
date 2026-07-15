from expense import Expense
from expense_manager import ExpenseManager
from data_manager import save_expenses_to_file, load_expenses_from_file

print("\nWelcome To Expense Tracker")

manager = ExpenseManager()
load_expenses_from_file(manager)

def get_valid_input(prompt: str) -> str:
    while True:
        value = input(prompt)
        if value.lower() == 'b':
            return None
        if not value.strip():
            print("\nInput cannot be blank.")
            return None
        else:
            return value.strip()
        
def get_valid_float_input(prompt: str) -> float:
    while True:
        value = input(prompt)
        if value.lower() == 'b':
            return None
        if not value.strip():
            print("\nInput cannot be blank.")
            return None
        try:
            float_value = float(value)
            if float_value < 0:
                print("\nInput cannot be negative.")
                return None
            return float_value
        except ValueError:
            print("\nPlease enter a valid number.")
            return None

def print_menu() -> None:
    print("\nPlease select an option:")
    print("1. Add expense")
    print("2. Remove expense")
    print("3. Edit expense")  
    print("4. View expenses")
    print("5. View expenses by category")
    print("6. View expense totals by category")
    print("7. Quit and save expenses to file")
    print("Enter 'b' anytime to go back to the main menu.")

def menu():
    while True:
        print_menu()
        choice = get_valid_input("\nEnter your choice: ")

        if choice not in ["1", "2", "3", "4", "5", "6", "7"]:
            print("\nInvalid choice. Please try again.")
            continue

        if choice == "1":
            category = get_valid_input("\nEnter expense category: ")
            if category is None:
                continue
            title = get_valid_input("Enter expense title: ")
            if title is None:
                continue
            amount = get_valid_float_input("Enter expense amount: ")
            if amount is None:
                continue
            expense = Expense(category, title, amount)
            manager.add_expense(expense)
            print(f"\nExpense {category} - '{title}' of amount {amount} added successfully.")

        elif choice == "2":
            category = get_valid_input("\nEnter expense category: ")
            if category is None:
                continue
            title = get_valid_input("Enter expense title: ")
            if title is None:
                continue
            expense_to_remove = None
            for expense in manager.expenses:
                if expense.category == category and expense.title == title:
                    expense_to_remove = expense
                    break
            if expense_to_remove:
                manager.remove_expense(expense_to_remove)
                print(f"\nExpense {category} - '{title}' removed successfully.")
            else:
                print(f"\nNo expense found with category '{category}' and title '{title}'.")

        elif choice == "3":
            category = get_valid_input("\nEnter expense category: ")
            if category is None:
                continue
            title = get_valid_input("Enter expense title: ")
            if title is None:
                continue
            amount = get_valid_float_input("Enter expense amount: ")
            if amount is None:
                continue
            old_expense = None
            for expense in manager.expenses:
                if expense.category == category and expense.title == title and expense.amount == amount:
                    old_expense = expense
                    break
            if old_expense:
                new_expense = Expense(category, title, amount)
                manager.edit_expense(old_expense, new_expense)
                print(f"\nExpense {category} - '{title}' edited successfully.")
            else:
                print(f"\nNo expense found with category '{category}' and title '{title}'.")

        elif choice == "4":
                expenses = manager.return_expenses()
                if not expenses:
                    print("\nNo expenses recorded.")
                else:
                    print("\nExpenses:")
                    for expense in expenses:
                        print(expense)

        elif choice == "5":
            category = get_valid_input("\nEnter expense category to view: ")
            if category is None:
                continue
            print(f"\nExpenses in category '{category}':")
            found = False
            for expense in manager.expenses:
                if expense.category == category:
                    print(expense)
                    found = True
            if not found:
                print(f"\nNo expenses found in category '{category}'.")

        elif choice == "6":
            totals = {}
            for expense in manager.expenses:
                if expense.category in totals:
                    totals[expense.category] += expense.amount
                else:
                    totals[expense.category] = expense.amount
            if not totals:
                print("\nNo expenses recorded.")
            else:
                print("\nExpense totals by category:")
                for category, total in totals.items():
                    print(f"{category}: ${total:.2f}")

        elif choice == "7":
            save_expenses_to_file(manager)
            print("\nExpenses saved to file. Exiting the program.\n")
            break

menu()
from expense import Expense

class ExpenseManager:
    def __init__(self) -> None:
        self.expenses = []

    def add_expense(self, expense: Expense) -> None:
        self.expenses.append(expense)

    def remove_expense(self, expense: Expense) -> None:
        if expense in self.expenses:
            self.expenses.remove(expense)

    def print_expenses(self) -> None:
        if not self.expenses:
            print("\nNo expenses recorded.")
            return
        print("\nExpenses:")
        for expense in self.expenses:
            print(expense)
from expense import Expense

class ExpenseManager:
    def __init__(self) -> None:
        self.expenses = []

    def add_expense(self, expense: Expense) -> None:
        self.expenses.append(expense)

    def remove_expense(self, expense: Expense) -> None:
        if expense in self.expenses:
            self.expenses.remove(expense)

    def return_expenses(self):
        return self.expenses
    
    def edit_expense(self, old_expense: Expense, new_expense: Expense) -> None:
        if old_expense in self.expenses:
            index = self.expenses.index(old_expense)
            self.expenses[index] = new_expense
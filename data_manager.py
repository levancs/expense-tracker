import json
import pathlib

from expense import Expense
from expense_manager import ExpenseManager

file_path = pathlib.Path("json_data.json")

def save_expenses_to_file(manager: ExpenseManager) -> None:
    with file_path.open('w') as file:
        data = [expense.to_dict() for expense in manager.expenses]
        json.dump(data, file, indent=2)

def load_expenses_from_file(manager: ExpenseManager) -> None:
    try:
        with file_path.open('r') as file:
            data = json.load(file)
            for expense_data in data:
                expense = Expense.from_dict(expense_data)
                manager.add_expense(expense)
            print("\nLoaded expenses from file successfully")
    except (FileNotFoundError, json.JSONDecodeError):
        print(f"\nNo valid data found in {file_path}. Could not load expenses from file.")
class Expense:
    def __init__(self, category: str, title: str, amount: float) -> None:
        self.category = category
        self.title = title
        self.amount = amount

    def __str__(self) -> str:
        return f"{self.category} - {self.title}: ${self.amount:.2f}"
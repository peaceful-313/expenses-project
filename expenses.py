import uuid
from datetime import datetime, timezone

class ExpenseRecord:
    def __init__(self, title: str, amount: float):
        """
        Create an expense record with a unique identifier, title, amount, and timestamps.
        """
        self.id = str(uuid.uuid4())
        self.title = title
        self.amount = float(amount)
        self.created_at = datetime.now(timezone.utc)
        self.updated_at = self.created_at
    
    def update(self, title=None, amount=None):
        """
        Update the title and/or amount of the expense object and refresh the updated_at timestamp.
        """
        if title:
            self.title = title
        if amount:
            self.amount = float(amount)
        self.updated_at = datetime.now(timezone.utc)
    
    def to_dict(self):
        """
        Return the expense object as a dictionary.
        """
        return {
            "id": self.id,
            "title": self.title,
            "amount": self.amount,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }

class ExpenseDB:
    def __init__(self):
        """
        Initialize an empty list to hold expense records.
        """
        self.expenses = []
    
    def add_expense(self, expense: ExpenseRecord):
        """
        Add an expense record to the manager.
        """
        self.expenses.append(expense)
    
    def remove_expense(self, expense_id: str):
        """
        Remove an expense object from the database by its unique ID.
        """
        self.expenses = [exp for exp in self.expenses if exp.id != expense_id]
    
    def get_expense(self, expense_id: str):
        """
        Retrieve an expense object from the database by its unique ID.
        """
        for exp in self.expenses:
            if exp.id == expense_id:
                return exp
        return None
    
    def get_expense_by_title(self, title: str):
        """
        Retrieve a list of expenses object from the database by its title.
        """
        return [exp.to_dict() for exp in self.expenses if exp.title.lower() == title.lower()]
    
    def to_dict(self):
        """
        Return the database as a list of dictionaries.
        """
        return [exp.to_dict() for exp in self.expenses]

if __name__ == "__main__":
    # Example usage
    manager = ExpenseDB()
    
    # Creating and adding expenses
    exp1 = ExpenseRecord("Dinner", 45.0)
    exp2 = ExpenseRecord("Transport", 20.0)
    manager.add_expense(exp1)
    manager.add_expense(exp2)
    
    # Modifying an expense
    exp1.update(title="Restaurant", amount=50.0)
    
    # Retrieving an expense by ID
    record = manager.get_expense(exp1.id)
    if record:
        print(record.to_dict())
    
    # Finding expenses by title
    matching_records = manager.get_expense_by_title("restaurant")
    for rec in matching_records:
        print(rec)
    
    # Removing an expense
    manager.remove_expense(exp2.id)
    
    # Displaying all stored expenses
    print(manager.to_dict())

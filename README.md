# Expense Manager Project

## Project Description
The **Expense Manager** project is a Python-based application designed to help users track and manage their financial expenses. It follows Object-Oriented Programming (OOP) principles and includes two core classes:

1. **ExpenseRecord Class**: Represents an individual financial expense with attributes such as a unique ID, title, amount, and timestamps.
2. **ExpenseDB Class**: Manages a collection of expenses, allowing users to add, remove, and retrieve expenses.

## Features
- Add new expenses with a unique ID, title, amount, and timestamps.
- Update expenses (title and/or amount) while refreshing the last updated timestamp.
- Retrieve expenses by ID or title.
- Remove expenses from the database.
- Convert expense records into a dictionary format for easy data handling.

## How to Clone the Repository
To get a local copy of the project, follow these steps:

```sh
# Open a terminal and navigate to your desired directory

# Clone the repository
git clone https://github.com/peaceful-313/expenses-project.git

# Change to the project directory
cd expenses-project
```

## How to Run the Code
Ensure you have Python installed (version 3.6 or later recommended). Then, run the following commands:

```sh
# Run the Python script
python expenses.py
```

## Example Usage
Here's an example of how to use the Expense Manager:

```python
from expenses import ExpenseRecord, ExpenseDB

manager = ExpenseDB()

# Create expenses
expense1 = ExpenseRecord("Groceries", 50.25)
expense2 = ExpenseRecord("Transport", 15.00)

# Add expenses to the database
manager.add_expense(expense1)
manager.add_expense(expense2)

# Print all expenses
print(manager.to_dict())
```

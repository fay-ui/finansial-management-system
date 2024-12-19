# financial_management_system.py
import os
from sqlalchemy.orm import sessionmaker
from models import create_db_engine, create_tables, Account, Transaction, Budget

# Initialize database
engine = create_db_engine()
Session = sessionmaker(bind=engine)
session = Session()

# Create tables if not already created
if not os.path.exists('database.db'):
    create_tables(engine)

# Define CRUD operations

# Account Management
def create_account(name, type, description, balance):
    account = Account(name=name, type=type, description=description, balance=balance)
    session.add(account)
    session.commit()
    return account

def view_accounts():
    accounts = session.query(Account).all()
    return accounts

def update_account(account_id, name, type, description, balance):
    account = session.query(Account).filter(Account.account_id == account_id).first()
    if account:
        account.name = name
        account.type = type
        account.description = description
        account.balance = balance
        session.commit()
        return account
    return "Account not found."

def delete_account(account_id):
    account = session.query(Account).filter(Account.account_id == account_id).first()
    if account:
        session.delete(account)
        session.commit()

# Transaction Management
def create_transaction(account_id, type, amount, description, date, budget_id):
    transaction = Transaction(account_id=account_id, type=type, amount=amount, description=description, date=date, budget_id=budget_id)
    session.add(transaction)
    session.commit()
    return transaction

def view_transactions():
    transactions = session.query(Transaction).all()
    return transactions

def update_transaction(transaction_id, amount, description, date):
    transaction = session.query(Transaction).filter(Transaction.transaction_id == transaction_id).first()
    if transaction:
        transaction.amount = amount
        transaction.description = description
        transaction.date = date
        session.commit()
        return transaction
    return "Transaction not found."

def delete_transaction(transaction_id):
    transaction = session.query(Transaction).filter(Transaction.transaction_id == transaction_id).first()
    if transaction:
        session.delete(transaction)
        session.commit()

# Budget Management
def create_budget(name, amount, category):
    budget = Budget(name=name, amount=amount, category=category)
    session.add(budget)
    session.commit()
    return budget

def view_budgets():
    budgets = session.query(Budget).all()
    return budgets

def update_budget(budget_id, name, amount, category):
    budget = session.query(Budget).filter(Budget.budget_id == budget_id).first()
    if budget:
        budget.name = name
        budget.amount = amount
        budget.category = category
        session.commit()
        return budget
    return "Budget not found."

def delete_budget(budget_id):
    budget = session.query(Budget).filter(Budget.budget_id == budget_id).first()
    if budget:
        session.delete(budget)
        session.commit()

# Command-line Interface (CLI)
def main():
    while True:
        print("\nFinancial Management System")
        print("1. Add Account")
        print("2. View Accounts")
        print("3. Update Account")
        print("4. Delete Account")
        print("5. Add Transaction")
        print("6. View Transactions")
        print("7. Update Transaction")
        print("8. Delete Transaction")
        print("9. Add Budget")
        print("10. View Budgets")
        print("11. Update Budget")
        print("12. Delete Budget")
        print("13. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Account Name: ")
            type = input("Account Type: ")
            description = input("Description: ")
            balance = float(input("Balance: "))
            account = create_account(name, type, description, balance)
            print(f"Account added: {account}")

        elif choice == '2':
            accounts = view_accounts()
            for account in accounts:
                print(account)

        elif choice == '3':
            account_id = int(input("Account ID to update: "))
            name = input("New Account Name: ")
            type = input("New Account Type: ")
            description = input("New Description: ")
            balance = float(input("New Balance: "))
            account = update_account(account_id, name, type, description, balance)
            print(f"Account updated: {account}")

        elif choice == '4':
            account_id = int(input("Account ID to delete: "))
            delete_account(account_id)
            print(f"Account ID {account_id} deleted.")

        elif choice == '5':
            account_id = int(input("Account ID: "))
            type = input("Transaction Type (income/expense): ")
            amount = float(input("Amount: "))
            description = input("Description: ")
            date = input("Date (YYYY-MM-DD): ")
            budget_id = int(input("Budget ID (0 if none): "))
            transaction = create_transaction(account_id, type, amount, description, date, budget_id)
            print(f"Transaction added: {transaction}")

        elif choice == '6':
            transactions = view_transactions()
            for transaction in transactions:
                print(transaction)

        elif choice == '7':
            transaction_id = int(input("Transaction ID to update: "))
            amount = float(input("New Amount: "))
            description = input("New Description: ")
            date = input("New Date (YYYY-MM-DD): ")
            transaction = update_transaction(transaction_id, amount, description, date)
            print(f"Transaction updated: {transaction}")

        elif choice == '8':
            transaction_id = int(input("Transaction ID to delete: "))
            delete_transaction(transaction_id)
            print(f"Transaction ID {transaction_id} deleted.")

        elif choice == '9':
            name = input("Budget Name: ")
            amount = float(input("Budget Amount: "))
            category = input("Category: ")
            budget = create_budget(name, amount, category)
            print(f"Budget added: {budget}")

        elif choice == '10':
            budgets = view_budgets()
            for budget in budgets:
                print(budget)

        elif choice == '11':
            budget_id = int(input("Budget ID to update: "))
            name = input("New Budget Name: ")
            amount = float(input("New Budget Amount: "))
            category = input("New Category: ")
            budget = update_budget(budget_id, name, amount, category)
            print(f"Budget updated: {budget}")

        elif choice == '12':
            budget_id = int(input("Budget ID to delete: "))
            delete_budget(budget_id)
            print(f"Budget ID {budget_id} deleted.")

        elif choice == '13':
            print("Exiting system...")
            break

if __name__ == '__main__':
    main()

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, joinedload
from models import Transaction, Account, Budget, Base
import datetime  # Import the datetime module

# Setup for testing
@pytest.fixture(scope="module")
def setup_db():
    
    engine = create_engine('sqlite:///:memory:')
    Session = sessionmaker(bind=engine)

    
    Base.metadata.create_all(engine)

    # Create a session
    session = Session()

    # Setup sample data
    account = Account(name="Test Account", type="Savings", balance=500.0)
    session.add(account)
    session.commit()  # Commit to get account_id

    budget = Budget(name="Test Budget", amount=1000.0, category="Groceries", account_id=account.account_id)
    session.add(budget)
    session.commit()  # Commit to get budget_id

    # Provide session and sample data for the test
    yield session, account, budget

    
    session.close()
    engine.dispose()


def test_transaction_creation(setup_db):
    session, account, budget = setup_db
    
    
    transaction_date = datetime.date(2024, 12, 19)  

    
    transaction = Transaction(amount=100, type="income", date=transaction_date, account_id=account.account_id, budget_id=budget.budget_id)
    session.add(transaction)
    session.commit()  # Commit transaction

    # Fetch the transaction from the database, ensuring relationships are loaded
    fetched_transaction = session.query(Transaction).options(joinedload(Transaction.account), joinedload(Transaction.budget))\
        .filter_by(transaction_id=transaction.transaction_id).first()

    
    assert fetched_transaction.amount == 100
    assert fetched_transaction.type == "income"
    assert fetched_transaction.account == account  
    assert fetched_transaction.budget == budget  

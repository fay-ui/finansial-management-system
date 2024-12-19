from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from db import Base  # Import Base from db.py (which is used for model inheritance)

# Account Model
class Account(Base):
    __tablename__ = 'accounts'
    
    account_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)
    description = Column(String)
    balance = Column(Float, nullable=False)
    
    # Relationships
    transactions = relationship('Transaction', back_populates='account', cascade='all, delete-orphan')
    budgets = relationship('Budget', back_populates='account', cascade='all, delete-orphan')

# Transaction Model
class Transaction(Base):
    __tablename__ = 'transactions'

    transaction_id = Column(Integer, primary_key=True)
    account_id = Column(Integer, ForeignKey('accounts.account_id', ondelete='CASCADE'), nullable=False)
    type = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    description = Column(String)
    date = Column(Date, nullable=False)
    budget_id = Column(Integer, ForeignKey('budgets.budget_id', ondelete='SET NULL'))

    # Relationships
    account = relationship('Account', back_populates='transactions')
    budget = relationship('Budget', back_populates='transactions')

# Budget Model
class Budget(Base):
    __tablename__ = 'budgets'

    budget_id = Column(Integer, primary_key=True)
    account_id = Column(Integer, ForeignKey('accounts.account_id', ondelete='CASCADE'), nullable=False)  # Add this foreign key column
    name = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    category = Column(String)

    # Relationships
    account = relationship('Account', back_populates='budgets')
    transactions = relationship('Transaction', back_populates='budget')

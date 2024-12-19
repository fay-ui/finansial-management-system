import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Create a base class for declarative models
Base = declarative_base()

def create_db_engine():
    """Create and return the database engine."""
    # Use SQLite for simplicity, change for other DBs as needed
    return create_engine('sqlite:///database.db', echo=True)

def create_tables(engine):
    """Create all tables in the database."""
    # Ensure tables are created
    Base.metadata.create_all(engine)

# Create a sessionmaker
def get_db_session(engine):
    """Returns a new session tied to the database engine."""
    Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return Session()


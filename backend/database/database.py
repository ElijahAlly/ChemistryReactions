from sqlalchemy import create_engine, event
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Use PostgreSQL URL from Render or fallback to SQLite for local development
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///./chemreactions.db')

# Handle SQLite vs PostgreSQL
if DATABASE_URL.startswith("sqlite"):
    engine = create_engine(
        DATABASE_URL, 
        connect_args={"check_same_thread": False}
    )
else:
    # Ensure we're using the correct PostgreSQL URL format
    # DATABASE_URL = DATABASE_URL.replace('postgres://', 'postgresql://') # We are
    engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# * Get the production backend env working with the prod db postgresql instance. 
# * And create a clone for local development. 
 
def init_db():
    from .base import Base
    from .elements import ElementModel  # Import your models here
    from .molecules import MoleculeModel
    
    print("Creating database tables...")
    try:
        # Create all tables first
        Base.metadata.create_all(bind=engine, checkfirst=True)
        print("Tables created successfully")
        
        db = SessionLocal()
        try:
            # Now check if we need to seed
            if db.query(ElementModel).first() is None and db.query(MoleculeModel).first() is None:
                print("Seeding database...")
                from scripts.seed_db import seed_db
                seed_db(db)
                print("Database seeded successfully!")
            else:
                print("Database already contains data, skipping seed.")
        finally:
            db.close()
    except Exception as e:
        print(f"Error during database initialization: {e}")
        raise

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
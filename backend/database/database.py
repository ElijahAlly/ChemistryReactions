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
    DATABASE_URL = DATABASE_URL.replace('postgres://', 'postgresql://')
    engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def init_db():
    from .elements import ElementModel  # Import your models here
    from .molecules import MoleculeModel
    
    print("Creating database tables...")
    try:
        # Create all tables first
        Base.metadata.create_all(bind=engine)
        print("Tables created successfully")
        
        db = SessionLocal()
        try:
            # Now check if we need to seed
            if db.query(ElementModel).count() == 0:
                print("Seeding database...")
                from ..scripts.seed_db import seed_db
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
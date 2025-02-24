from .database import Base, engine

def init_db():
    """Initialize the database by creating all tables"""
    try:
        Base.metadata.create_all(bind=engine)
        print("Database initialized successfully!")
    except Exception as e:
        print(f"Error initializing database: {e}")
        raise e

if __name__ == "__main__":
    init_db()
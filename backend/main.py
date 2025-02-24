from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database.init_db import init_db
from scripts.seed_db import seed_db
from api.routes import molecules, elements  # Remove reactions and simulations for now

def setup_database():
    """Initialize and seed the database"""
    try:
        # Initialize database (create tables)
        init_db()
        # Seed database with initial data
        seed_db()
    except Exception as e:
        print(f"Error setting up database: {e}")
        raise e

# Setup database before starting the application
setup_database()

app = FastAPI(
    title="Chemical Reaction Simulator API",
    description="API for simulating and visualizing chemical reactions",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Update this with your frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(molecules.router, prefix="/api/molecules", tags=["molecules"])
app.include_router(elements.router, prefix="/api/elements", tags=["elements"])
# We'll add these back later
# app.include_router(reactions.router, prefix="/api/reactions", tags=["reactions"])
# app.include_router(simulations.router, prefix="/api/simulations", tags=["simulations"])

@app.get("/")
async def root():
    return {"message": "Chemical Reaction Simulator API"}
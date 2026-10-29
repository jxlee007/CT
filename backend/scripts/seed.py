"""Database Seeding Script for Demo Data."""
import sys
from pathlib import Path

# Add project root to path
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

from backend.app.core.database import SessionLocal, engine, Base

def seed_data():
    """Initializes tables and seeds initial demo records."""
    print("Creating all tables in PostgreSQL...")
    Base.metadata.create_all(bind=engine)
    
    db = SessionLocal()
    try:
        print("Database tables verified. Ready for domain seed data.")
        # Specific model seeding will be added during sprint implementation
    finally:
        db.close()

if __name__ == "__main__":
    seed_data()


from database.database import SessionLocal
from database.molecules import MoleculeModel
from database.elements import ElementModel
from .molecules import test_molecules
from .elements import test_elements

def seed_db(db):
    """Seed the database with initial data"""
    try:
        # Check if elements already exist
        existing_elements = db.query(ElementModel).count()
        if existing_elements == 0:
            print("Seeding elements...")
            for element_data in test_elements:
                element = ElementModel(**element_data)
                db.add(element)
            print("Elements seeded successfully!")
        else:
            print("Elements already exist in database, skipping.")

        # Check if molecules already exist
        existing_molecules = db.query(MoleculeModel).count()
        if existing_molecules == 0:
            print("Seeding molecules...")
            for molecule_data in test_molecules:
                molecule = MoleculeModel(**molecule_data)
                db.add(molecule)
            print("Molecules seeded successfully!")
        else:
            print("Molecules already exist in database, skipping.")

        db.commit()

    except Exception as e:
        print(f"Error seeding database: {e}")
        db.rollback()
        raise e
    finally:
        db.close()

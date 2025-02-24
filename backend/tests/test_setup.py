def test_imports():
    try:
        from fastapi import FastAPI
        print("✅ FastAPI imported successfully!")
    except ImportError as e:
        print(f"❌ Failed to import FastAPI: {e}")

    try:
        import rdkit
        print("✅ RDKit imported successfully")
    except ImportError as e:
        print(f"❌ RDKit import failed: {e}")

def test_dependencies():
    dependencies = [
        'fastapi',
        'uvicorn',
        'pydantic',
        'sqlalchemy',
        'rdkit',
    ]
    
    for dep in dependencies:
        try:
            __import__(dep)
            print(f"✅ {dep} imported successfully!")
        except ImportError as e:
            print(f"❌ Failed to import {dep}: {e}")

if __name__ == "__main__":
    print("Testing imports...")
    test_imports()
    print("\nTesting all dependencies...")
    test_dependencies()

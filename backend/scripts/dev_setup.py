import subprocess
import sys
import os
from pathlib import Path

def check_python_version():
    python_version = sys.version_info
    if python_version.major < 3 or (python_version.major == 3 and python_version.minor < 8):
        print("Error: Python 3.8 or higher is required")
        sys.exit(1)

def create_directories():
    directories = [
        "api/models",
        "api/routes",
        "api/services",
        "tests",
        "scripts",
        "database",
    ]
    
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)
        init_file = Path(directory) / "__init__.py"
        init_file.touch()

def install_dependencies():
    subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

def main():
    print("🔧 Setting up development environment...")
    
    print("\n📌 Checking Python version...")
    check_python_version()
    
    print("\n📁 Creating directory structure...")
    create_directories()
    
    print("\n📦 Installing dependencies...")
    install_dependencies()
    
    print("\n✅ Setup complete! You can now start the server with:")
    print("uvicorn main:app --reload --port 8000")

if __name__ == "__main__":
    main()

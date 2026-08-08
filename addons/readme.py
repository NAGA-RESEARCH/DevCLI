import os

def generate(project_name):
    print(f"📝 Generating README.md for '{project_name}'...")

    readme_content = f"""# {project_name.capitalize()}

This project was automatically generated using **DevCLI** (A Custom Developer Automation Tool).

## 🚀 Features Enabled
- Automated Folder Architecture
- VS Code Auto-Configuration
- Virtual Environment Integration (Backend)
- Docker Containerization Support

## 🛠️ How to Run
1. Open the project in your terminal.
2. If it's a Python project, activate the virtual environment (`venv/Scripts/activate`).
3. Install dependencies (`pip install -r requirements.txt`).
4. Run the development server.

Happy Coding! 💻
"""

    try:
        with open(os.path.join(project_name, "README.md"), "w") as f:
            f.write(readme_content)
        print("✅ README.md successfully created!")
    except Exception as e:
        print(f"⚠️ Error creating README.md: {e}")

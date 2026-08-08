import subprocess
import os
import json

def create(project_name):
    print(f"🐍 Creating Virtual Environment (venv) in '{project_name}'...")
    try:
        subprocess.run(["python", "-m", "venv", "venv"], cwd=project_name, check=True)
        print("✅ Virtual Environment created successfully!")

        # --- NAYA LOGIC: VS Code Auto-Activation ---
        # Project ke andar .vscode folder banana
        vscode_dir = os.path.join(project_name, ".vscode")
        os.makedirs(vscode_dir, exist_ok=True)

        # settings.json banana jisse VS Code automatically venv pakad le
        settings_path = os.path.join(vscode_dir, "settings.json")
        settings_content = {
            "python.defaultInterpreterPath": "${workspaceFolder}/venv/Scripts/python.exe",
            "python.terminal.activateEnvironment": True
        }

        with open(settings_path, "w") as f:
            json.dump(settings_content, f, indent=4)

        print("⚙️ VS Code configured to auto-activate venv!")

    except Exception as e:
        print(f"⚠️ Error creating venv: {e}")

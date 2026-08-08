import os
import sys
import subprocess

def check_dependency(command, name):
    try:
        # Dependency check karne ke liye version command run kar rahe hain
        subprocess.run([command, "--version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
        print(f"✅ {name} Found")
    except Exception:
        print(f"⚠️ {name} Not Found (Ya PATH mein set nahi hai)")

def register_command():
    print("\n⚙️ Registering 'devcli' as a global command...")

    # Project ka actual directory path nikal rahe hain
    project_dir = os.path.abspath(os.path.dirname(__file__))

    # Python ke default 'Scripts' folder ka path, jo Windows ke PATH mein pehle se hota hai
    scripts_folder = os.path.join(sys.prefix, "Scripts")
    os.makedirs(scripts_folder, exist_ok=True)

    # .bat file banayenge jisse Windows native command samajh kar run karega
    bat_file = os.path.join(scripts_folder, "devcli.bat")

    # Batch file ka content jo command type karte hi execute hoga
    bat_content = f'''@echo off
set PYTHONPATH={project_dir}
python -m devcli %*
'''

    with open(bat_file, "w") as f:
        f.write(bat_content)

    print(f"✅ Global command successfully registered at: {bat_file}")

if __name__ == "__main__":
    print("🚀 DevCLI Installer Started...\n")

    print("🔍 Checking system dependencies...")
    # Section 16 requirements: Python, Git, aur VS Code check karna[cite: 1]
    check_dependency("python", "Python")
    check_dependency("git", "Git")
    check_dependency("code", "VS Code")

    # Command register karne ka function call karna
    register_command()

    print("\n🎉 DevCLI successfully installed!")
    print("💡 Tip: Apna VS Code ya Terminal ek baar restart karein. Phir seedha 'devcli static final_project' chala kar dekhein!")

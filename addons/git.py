import subprocess

def init(project_name):
    print(f"📦 Initializing Git repository in '{project_name}'...")
    try:
        # Puraane tarike ki jagah subprocess use kar rahe hain taaki command terminal mein directly run ho
        subprocess.run(["git", "init"], cwd=project_name, check=True, stdout=subprocess.DEVNULL)
        print("✅ Git successfully initialized!")
    except FileNotFoundError:
        print("⚠️ Git install nahi hai system par, skip kar rahe hain.")
    except Exception as e:
        print(f"⚠️ Git error: {e}")

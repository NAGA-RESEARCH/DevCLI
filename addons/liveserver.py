import subprocess

def start(project_name):
    print(f"🌐 Opening '{project_name}' in VS Code...")
    try:
        # Windows par 'code' command run karne ke liye shell=True rakha hai
        subprocess.run(["code", project_name], shell=True)
        print("✅ VS Code opened successfully!")
        print("💡 Tip: VS Code mein bottom-right corner par 'Go Live' click karein apna server start karne ke liye.")
    except Exception as e:
        print(f"⚠️ VS Code open karne mein error aayi: {e}")

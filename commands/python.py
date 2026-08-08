import os
from addons import git, liveserver, venv, docker, readme

def create_python_project(project_name, options):
    print(f"\n⚙️ Creating Basic Python Project: '{project_name}'...")

    current_dir = os.path.dirname(os.path.abspath(__file__))
    template_dir = os.path.join(current_dir, "..", "templates", "python")

    # Project folder banana
    os.makedirs(project_name, exist_ok=True)

    try:
        # main.py copy karna (aur project name replace karna)
        with open(os.path.join(template_dir, "main.py"), "r") as f:
            main_content = f.read()
        with open(os.path.join(project_name, "main.py"), "w") as f:
            f.write(main_content.replace("{project_name}", project_name))

        # requirements.txt copy karna
        with open(os.path.join(template_dir, "requirements.txt"), "r") as f:
            req_content = f.read()
        with open(os.path.join(project_name, "requirements.txt"), "w") as f:
            f.write(req_content)

    except FileNotFoundError:
        print(f"⚠️ Error: Python template files missing in {template_dir}")
        return

    print("✅ Python project structure successfully generated!")

    # Addons Handle Karna
    enabled_addons = options.get("enable", [])
    disabled_addons = options.get("disable", [])

    if "env" not in disabled_addons:
        venv.create(project_name)

    if "docker" in enabled_addons:
        docker.add(project_name)

    if "readme" in enabled_addons:
        readme.generate(project_name)

    if "git" in enabled_addons:
        git.init(project_name)

    # VS Code automatically open karna
    liveserver.start(project_name)

    print("\n🎉 Python setup complete! Next steps:")
    if "env" not in disabled_addons:
        print("1. Terminal mein 'venv\\Scripts\\activate' automatically chalega (agar VS Code configured hai).")
        print("2. 'python main.py' run karke apna code test karein.")
    else:
        print("1. 'python main.py' run karke apna code test karein.")

import os
from addons import git, docker, liveserver

def create_flask_project(project_name, options):
    print(f"\n⚙️ Creating Flask API Project: '{project_name}'...")

    current_dir = os.path.dirname(os.path.abspath(__file__))
    template_dir = os.path.join(current_dir, "..", "templates", "flask")

    # Flask ka standard folder structure
    folders = [
        f"{project_name}/static/css",
        f"{project_name}/static/js",
        f"{project_name}/templates",
        f"{project_name}/routes",
        f"{project_name}/models"
    ]

    for folder in folders:
        os.makedirs(folder, exist_ok=True)

    try:
        # app.py read aur write karna
        with open(os.path.join(template_dir, "app.py"), "r") as f:
            app_content = f.read()
        with open(f"{project_name}/app.py", "w") as f:
            f.write(app_content.replace("{project_name}", project_name))

        # requirements.txt read aur write karna
        with open(os.path.join(template_dir, "requirements.txt"), "r") as f:
            req_content = f.read()
        with open(f"{project_name}/requirements.txt", "w") as f:
            f.write(req_content)

    except FileNotFoundError:
        print(f"⚠️ Error: Flask template files missing in {template_dir}")
        return

    print("✅ Flask backend structure successfully generated!")

    # Addons Handle Karna
    enabled_addons = options.get("enable", [])

    if "git" in enabled_addons:
        git.init(project_name)
    if "live" in enabled_addons:
        liveserver.start(project_name)

    print("\n🎉 Backend setup complete! To start server: cd {} && python app.py".format(project_name))

import os
from addons import git, bootstrap, liveserver, docker, readme

def create_static_project(project_name, options):
    print(f"\n⚙️ Creating Static Project: '{project_name}'...")

    # Template folder ka absolute path nikalna (taaki global command se bhi chal sake)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    template_dir = os.path.join(current_dir, "..", "templates", "static")

    # Folders list
    folders = [
        f"{project_name}/css",
        f"{project_name}/js",
        f"{project_name}/assets/images",
        f"{project_name}/assets/icons",
        f"{project_name}/assets/videos",
        f"{project_name}/assets/fonts"
    ]

    for folder in folders:
        os.makedirs(folder, exist_ok=True)

    try:
        # Templates se HTML read karna
        with open(os.path.join(template_dir, "index.html"), "r") as f:
            html_content = f.read()

        # Naye project mein HTML write karna (Name replace karke)
        with open(f"{project_name}/index.html", "w") as f:
            f.write(html_content.replace("{project_name}", project_name))

        # Templates se CSS read/write karna
        with open(os.path.join(template_dir, "style.css"), "r") as f:
            css_content = f.read()
        with open(f"{project_name}/css/style.css", "w") as f:
            f.write(css_content)

        # Responsive CSS khali banani hai
        with open(f"{project_name}/css/responsive.css", "w") as f:
            f.write("/* Responsive structure */\n")

        # Templates se JS read/write karna
        with open(os.path.join(template_dir, "script.js"), "r") as f:
            js_content = f.read()
        with open(f"{project_name}/js/script.js", "w") as f:
            f.write(js_content)

    except FileNotFoundError as e:
        print(f"⚠️ Error: Template files nahi mili. Kya files {template_dir} mein exist karti hain?")
        return

    print("✅ Project structure aur files TEMPLATES se successfully generate ho gayi hain!")

    # Addons logic
    enabled_addons = options.get("enable", [])

    if "git" in enabled_addons:
        git.init(project_name)
    if "bs" in enabled_addons:
        bootstrap.add(project_name)
    # Docker setup karna
    if "docker" in enabled_addons:
        docker.add(project_name)

    # README setup karna
    if "readme" in enabled_addons:
        readme.generate(project_name)


    # Ab VS Code by default open hoga har naye project ke liye
    liveserver.start(project_name)

    print("\n🎉 Project setup complete! Happy Coding!")

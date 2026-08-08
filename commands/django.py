import os
import subprocess
import time
import webbrowser
from addons import git, liveserver, venv, docker, readme

def create_django_project(project_name, options):
    print(f"\n⚙️ Creating Django Project: '{project_name}'...")

    current_dir = os.path.dirname(os.path.abspath(__file__))
    template_dir = os.path.join(current_dir, "..", "templates", "django")

    folders = [
        f"{project_name}/core",
        f"{project_name}/apps",
        f"{project_name}/templates",
        f"{project_name}/static/css",
        f"{project_name}/static/js",
        f"{project_name}/static/images"
    ]

    for folder in folders:
        os.makedirs(folder, exist_ok=True)

    try:
        # Root files copy karna
        for file_name in ["manage.py", "requirements.txt"]:
            with open(os.path.join(template_dir, file_name), "r") as f:
                content = f.read()
            with open(f"{project_name}/{file_name}", "w") as f:
                f.write(content)

        # Core configuration files copy karna
        core_files = ["__init__.py", "settings.py", "urls.py", "wsgi.py", "asgi.py"]
        for file_name in core_files:
            src_path = os.path.join(template_dir, "core", file_name)
            if os.path.exists(src_path):
                with open(src_path, "r") as f:
                    content = f.read()
                with open(f"{project_name}/core/{file_name}", "w") as f:
                    f.write(content)
            else:
                with open(f"{project_name}/core/{file_name}", "w") as f:
                    pass

        # HTML Templates copy karna
        django_template_dir = os.path.join(template_dir, "templates")
        if os.path.exists(django_template_dir):
            for file_name in os.listdir(django_template_dir):
                src_path = os.path.join(django_template_dir, file_name)
                if os.path.isfile(src_path):
                    with open(src_path, "r") as f:
                        content = f.read()
                    with open(f"{project_name}/templates/{file_name}", "w") as f:
                        f.write(content.replace("{project_name}", project_name))

    except Exception as e:
        print(f"⚠️ Error generating Django template: {e}")
        return

    print("✅ Django full project structure and core settings successfully generated!")

    enabled_addons = options.get("enable", [])
    disabled_addons = options.get("disable", [])

    # Venv banana
    if "env" not in disabled_addons:
        venv.create(project_name)

    # Git initialize karna
    if "git" in enabled_addons:
        git.init(project_name)

    # VS Code hamesha open hoga
    liveserver.start(project_name)

    print("\n🎉 Django setup complete!")

    # --- AUTO INSTALL & SERVER LOGIC ---
    if "env" not in disabled_addons:
        print("📦 Installing requirements automatically... (Please wait)")
        try:
            # Background mein packages install karna
            pip_path = os.path.join(project_name, "venv", "Scripts", "pip")
            req_path = os.path.join(project_name, "requirements.txt")
            subprocess.run([pip_path, "install", "-r", req_path], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print("✅ Packages installed successfully!")

            # Agar user ne +live diya hai toh Server aur Browser start hoga
            if "live" in enabled_addons:
                print("🚀 Starting Django Server...")
                # Naya CMD window open karke server chalana
                cmd = f'start cmd /k "cd {project_name} && venv\\Scripts\\activate && python manage.py runserver"'
                subprocess.Popen(cmd, shell=True)

                print("🌐 Opening Browser...")
                time.sleep(3) # Server start hone ka wait karna
                webbrowser.open("http://127.0.0.1:8000")

            # Docker setup karna
            if "docker" in enabled_addons:
                docker.add(project_name)


            # README setup karna
            if "readme" in enabled_addons:
                readme.generate(project_name)

        except Exception as e:
            print(f"⚠️ Error during auto-setup: {e}")
    else:
        print("\nNext steps (Manual):")
        print(f"1. cd {project_name}")
        print("2. python -m venv venv")
        print("3. venv\\Scripts\\activate")
        print("4. pip install -r requirements.txt")
        print("5. python manage.py runserver")

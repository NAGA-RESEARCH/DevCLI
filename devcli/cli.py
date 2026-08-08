import sys
from .parser import parse_arguments
from commands import static, flask, django, python  # Naya import add kiya





def show_help():
    print("\n🚀 DevCLI - Custom Developer Automation Tool")
    print("Usage: devcli <template> <project_name> [options]\n")

    print("🔧 CLI CONVENTIONS:")
    print("  --  : Information check karne ke liye (e.g., --h for help)")
    print("  +   : Addons add karne ke liye (e.g., +git, +docker)")
    print("  -   : Default options hatane ke liye (e.g., -env)\n")

    print("📂 AVAILABLE TEMPLATES:")
    print("  static  : Basic HTML/CSS/JS website structure")
    print("  python  : Clean Python scripting environment")
    print("  flask   : Fully structured Flask web app")
    print("  django  : Full Django project with core settings\n")

    print("➕ ADDONS (Add with '+'):")
    print("  +bs     : Inject Bootstrap 5 CDN (Static/Flask/Django mein)")
    print("  +git    : Initialize empty Git repository")
    print("  +live   : Auto-open VS Code (and start server for backend)")
    print("  +docker : Generate Smart Dockerfile and .dockerignore")
    print("  +readme : Generate project README.md\n")

    print("➖ DISABLE FLAGS (Remove with '-'):")
    print("  -env    : Skip creating Virtual Environment (venv)\n")

    print("📖 EXAMPLES:")
    print("  devcli static portfolio +bs +git +live")
    print("  devcli django backend_api +docker +readme -env")
    print("  devcli --h\n")


def main():
    # 1. Sabse pehle Help Command Check (Success)
    if len(sys.argv) > 1 and sys.argv[1] in ['--h', '--help']:
        show_help()
        return 0

    # 2. Error Handling (Error)
    if len(sys.argv) < 3:
        print("Usage Error: devcli <template> <project_name> [options]")
        print("Example: devcli django portfolio +bs +git -env")
        print("Tip: Type 'devcli --h' for the help menu.")
        return 1

    args, options = parse_arguments(sys.argv[1:])

    print("🚀 DevCLI Initializing...\n")
    print(f"📁 Target Template : {args.template}")
    print(f"📝 Project Name    : {args.project_name}")

    if options["enable"]:
        print(f"✅ Enabled Addons  : {', '.join(options['enable'])}")
    if options["disable"]:
        print(f"❌ Disabled Addons : {', '.join(options['disable'])}")

    # --- YAHAN NAYA LOGIC AAYA HAI ---
    # Template check karke specific command call karna
    if args.template.lower() == 'static':
        static.create_static_project(args.project_name, options)
    elif args.template.lower() == 'flask':
        flask.create_flask_project(args.project_name, options)
    elif args.template.lower() == 'django':
        django.create_django_project(args.project_name, options)
    elif args.template.lower() == 'python':
        python.create_python_project(args.project_name, options)

    else:
        print(f"\n⚠️ Template '{args.template}' abhi develop nahi hua hai.")

    return 0

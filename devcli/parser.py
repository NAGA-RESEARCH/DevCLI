import argparse

def parse_arguments(args=None):
    # Basic command line parser setup
    parser = argparse.ArgumentParser(description="DevCLI: Developer Productivity CLI")

    # Required arguments (Positional)
    parser.add_argument("template", help="Project template type (e.g., static, django, flask)")
    parser.add_argument("project_name", help="Name of your project folder")

    # Default arguments ko parse karo
    parsed_args, remaining_args = parser.parse_known_args(args)

    # Custom dictionary options store karne ke liye
    options = {
        "enable": [],
        "disable": []
    }

    # Shortcuts (+ aur -) ko check karne ke liye loop
    for arg in remaining_args:
        if arg.startswith('+'):
            options["enable"].append(arg[1:])  # '+' hata kar save karega
        elif arg.startswith('-') and not arg.startswith('--'):
            options["disable"].append(arg[1:]) # '-' hata kar save karega

    return parsed_args, options

import os

def add(project_name):
    print(f"🎨 Injecting Bootstrap 5 CDNs in '{project_name}'...")

    # Check karega ki index.html root me hai (Static) ya templates me (Django/Flask)
    possible_paths = [
        f"{project_name}/index.html",
        f"{project_name}/templates/index.html"
    ]

    file_path = None
    for path in possible_paths:
        if os.path.exists(path):
            file_path = path
            break

    if not file_path:
        print("⚠️ Warning: index.html nahi mili. Bootstrap skip kar diya gaya hai.")
        return

    # Agar file mil gayi toh read karke CDN lagayenge
    with open(file_path, "r") as f:
        html = f.read()

    css_cdn = '    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">\n</head>'
    html = html.replace('</head>', css_cdn)

    js_cdn = '    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>\n</body>'
    html = html.replace('</body>', js_cdn)

    with open(file_path, "w") as f:
        f.write(html)

    print("✅ Bootstrap added successfully!")

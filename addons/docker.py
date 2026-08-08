import os

def add(project_name):
    print(f"🐳 Adding Smart Docker configuration to '{project_name}'...")

    # 1. Project type detect karna files ke basis par
    if os.path.exists(os.path.join(project_name, "manage.py")):
        project_type = "django"
    elif os.path.exists(os.path.join(project_name, "app.py")):
        project_type = "flask"
    elif os.path.exists(os.path.join(project_name, "main.py")):
        project_type = "python"
    else:
        project_type = "static"

    # 2. Type ke hisaab se Dockerfile ka content generate karna
    if project_type == "django":
        dockerfile_content = """# Django (Python) Base Image
FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
"""
    elif project_type == "flask":
        dockerfile_content = """# Flask (Python) Base Image
FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
"""
    else:
        dockerfile_content = """# Static Website Base Image (Nginx)
FROM nginx:alpine
# Nginx ke public html folder mein apna static code copy karna
COPY . /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
"""

    # .dockerignore ka content (Sabke liye same)
    dockerignore_content = """venv/
__pycache__/
*.pyc
.env
.vscode/
.git/
"""

    try:
        # Files create karna
        with open(os.path.join(project_name, "Dockerfile"), "w") as f:
            f.write(dockerfile_content)

        with open(os.path.join(project_name, ".dockerignore"), "w") as f:
            f.write(dockerignore_content)

        print(f"✅ {project_type.capitalize()} ke liye Dockerfile aur .dockerignore generate ho gaye!")
    except Exception as e:
        print(f"⚠️ Error creating Docker files: {e}")

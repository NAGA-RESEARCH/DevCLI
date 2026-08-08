import os
from setuptools import setup, find_packages

# Current directory ka exact path nikalna
current_dir = os.path.abspath(os.path.dirname(__file__))
requirements_path = os.path.join(current_dir, 'requirements.txt')

# Ab safely file ko read karna
with open(requirements_path, encoding='utf-8') as f:
    requirements = f.read().splitlines()

setup(
    name="devcli_nagalab",
    version="0.1.2",
    packages=find_packages(),
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'devcli=devcli.cli:main',
        ],
    },
    author="Naga Research",
    description="A command line tool for developers",
    long_description=open(os.path.join(current_dir, 'README.md'), encoding='utf-8').read(),
    long_description_content_type='text/markdown',
)

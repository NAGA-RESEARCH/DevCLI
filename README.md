<div align="center">

# ⚡ DevCLI

**Stop typing boilerplate. Start shipping code.**

*A custom developer automation tool for instant project setup and boilerplate generation.*

[![PyPI version](https://img.shields.io/pypi/v/devcli-nagalab.svg?color=0A66C2)](https://pypi.org/project/devcli-nagalab/)
[![Python Versions](https://img.shields.io/pypi/pyversions/devcli-nagalab.svg?color=0A66C2)](https://pypi.org/project/devcli-nagalab/)
[![License: MIT](https://img.shields.io/badge/License-MIT-teal.svg)](LICENSE)
[![Maintained by NAGA LABS](https://img.shields.io/badge/Maintained%20by-NAGA%20LABS-6a0dad)](https://github.com/NAGA-RESEARCH)

</div>

---

## 🧭 Why DevCLI?

Every new project starts the same way — creating folders, initializing git, setting up a virtual environment, writing a `.gitignore`, adding a README... **DevCLI eliminates that entire ritual.**

Just tell it what you're building, add the features you want with a simple `+`, remove the defaults you don't want with a `-`, and let DevCLI scaffold a clean, ready-to-code project in seconds.

```bash
devcli django backend_api +docker +readme -env
```

That's it. Your Django backend — with Docker support and a README, minus the virtual environment — is ready.

---

## ✨ Features

- 🚀 **One-Command Scaffolding** — Generate complete project structures instantly, no manual folder-clicking required.
- 🧩 **Multiple Templates Out of the Box** — Django, Flask, Python, and Static (HTML/CSS/JS) projects, all pre-configured.
- ➕ **Additive Flag System** — Bolt on `git`, `docker`, `bootstrap`, `readme`, and more using intuitive `+flags`.
- ➖ **Subtractive Flag System** — Skip defaults like virtual environments using `-flags`, keeping setups lean when you need them to be.
- 🛠️ **Sensible Defaults, Full Control** — Ships with opinionated best-practice structures, but never locks you in.
- 🧠 **Predictable, Human-Readable Syntax** — `--`, `+`, and `-` each have one clear job, so commands read like plain English.
- 💻 **Built for Real Dev Workflows** — Designed by a developer, for developers who'd rather build than boilerplate.

---

## 📦 Installation

DevCLI is available on PyPI and installs in seconds:

```bash
pip install devcli-nagalab
```

> Requires **Python 3.8+**. We recommend installing inside a virtual environment or using [`pipx`](https://pypa.github.io/pipx/) for global CLI access.

Verify the installation:

```bash
devcli --h
```

---

## 🚀 Quick Start

### Basic Syntax

```bash
devcli <template> <project_name> [options]
```

| Component        | Description                                          |
|-------------------|------------------------------------------------------|
| `<template>`      | The project type you want to scaffold                |
| `<project_name>`  | The name of your new project / root folder           |
| `[options]`       | Any combination of `+` and `-` flags                 |

### Available Templates

| Template  | Description                              |
|-----------|-------------------------------------------|
| `django`  | Full Django backend setup                 |
| `flask`   | Flask web application setup               |
| `python`  | Basic Python script / project structure   |
| `static`  | HTML/CSS/JS static website boilerplate    |

---

## 🎛️ The Flag System

DevCLI's flag system is built around one idea: **the symbol tells you the intent.**

| Symbol | Meaning     | Purpose                                              | Example        |
|:------:|-------------|-------------------------------------------------------|-----------------|
| `--`   | **Check**   | Query information about DevCLI itself                | `--h`           |
| `+`    | **Enable**  | Add an optional feature/addon to the project          | `+git`, `+docker` |
| `-`    | **Disable** | Remove a default behavior from the setup               | `-env`          |

### Common Addons (`+`)

| Flag       | Effect                                  |
|------------|-------------------------------------------|
| `+git`     | Initializes a Git repository               |
| `+docker`  | Adds a Dockerfile to the project           |
| `+bs`      | Adds Bootstrap for frontend styling        |
| `+readme`  | Auto-generates a project README            |

### Common Removals (`-`)

| Flag     | Effect                              |
|----------|---------------------------------------|
| `-env`   | Skips virtual environment creation    |

### Getting Help

```bash
devcli --h
```

Displays the full custom help menu, listing every template and flag DevCLI currently supports.

---

## 💡 Examples

**1. A dockerized Django backend, without a virtual environment:**

```bash
devcli django backend_api +docker +readme -env
```
Creates a Django project named `backend_api`, adds Docker support and a README, and skips virtual environment creation.

**2. A Django portfolio site with Git and Bootstrap:**

```bash
devcli django portfolio +bs +git -env
```
Creates a Django project named `portfolio`, adds Bootstrap and initializes Git, skipping the virtual environment.

**3. A quick static website:**

```bash
devcli static landing_page +git
```
Scaffolds an HTML/CSS/JS static site named `landing_page` and initializes Git.

**4. A minimal Flask app:**

```bash
devcli flask my_api +docker
```
Creates a Flask project named `my_api` with Docker support included.

---

## 🗺️ Roadmap

- [ ] Additional templates (FastAPI, Node.js, React)
- [ ] Custom user-defined templates and config profiles
- [ ] Interactive setup mode
- [ ] Plugin system for community-built addons

Have an idea? Open an issue — contributions and suggestions are always welcome.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/NAGA-RESEARCH/DevCLI/issues) or submit a pull request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

<div align="center">

Built with focus and caffeine by **[Naga Research](https://github.com/NAGA-RESEARCH)** 🐍

*Part of the **NAGA LABS** ecosystem.*

</div>

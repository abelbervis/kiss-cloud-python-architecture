---
name: python-project-assistant
description: Use this skill when you need to keep requirements.txt clean, structure modules in utils/, manage Dockerfiles and .dockerignore security rules, or update documentation in README.md for Python projects.
---

# Skill: Python Project Assistant

General instructions for managing and maintaining Python projects:

## 1. Managing `requirements.txt`
- NEVER use `pip freeze` blindly to prevent adding secondary or "junk" dependencies.
- Only add the main libraries that the code is actually importing and using.
- Keep versions clean or specified according to project standards.
- Always keep `requirements.txt` in the root of the project.

## 2. Managing Docker Security & Git (`Dockerfile`, `.dockerignore`, `.gitignore`)
- Whenever a new system dependency or configuration is added, ensure the `Dockerfile` is updated accordingly.
- ALWAYS ensure sensitive files (like `.env`), caches (`__pycache__`), and virtual environments (`venv/`) are excluded in `.dockerignore` to prevent leaking secrets into Docker images.
- Ensure sensitive files and local caches are properly excluded in `.gitignore`.

## 3. Managing `README.md`
Whenever a new module is created (e.g., inside `utils/`) or new functionality is added, update or create the `README.md` including:
- Current **project structure**.
- Required **environment variables** (e.g., what goes into `.env`).
- Clear **execution instructions** (how to run locally and via Docker).

## 4. Code Standards & Modularity
- Keep infrastructure logic, connectors, and external clients (APIs, databases) inside the `utils/` folder.
- Keep main execution scripts in the root folder.
- Always handle exceptions clearly with descriptive error messages.

# Phase 02 - Docker Image | Python APP Calculator

## 📌 Overview

This phase demonstrates how to containerize a Python calculator application using Docker.

The project starts from a local Python application and transforms it into a portable Docker image. The application can be executed using a Dockerfile, Docker Compose, and an optional Windows launcher.

The main goal of this phase is to show how a Python application can be packaged, isolated, and executed inside a containerized environment.

This phase is part of a larger portfolio focused on Python, Docker, CI/CD, Cloud Infrastructure, Monitoring, LLM, RAG, and AI-powered Platform Engineering.

---

## 🎯 Objective

The objective of this phase is to demonstrate the complete process of creating and running a Docker image from a Python application.

This phase covers:

- Python application structure
- Separation between business logic and graphical interface
- Docker image creation
- Multi-stage Dockerfile usage
- Docker Compose execution
- GUI execution from a Docker container
- Windows launcher integration
- Basic Docker and repository best practices

---

## 🧱 Project Structure

```text
Phase 02 - Docker Image
│
├── Python-Calculator
│   ├── src
│   │   ├── calculator_logic.py
│   │   ├── calculator_ui.py
│   │   └── main.py
│   │
│   ├── .gitignore
│   └── README.md
│
├── .dockerignore
├── .gitignore
├── Docker-Compose.yaml
├── Dockerfile
├── MiCalculadora.bat
├── MiCalculadora.xlaunch
└── README.md
```

---

## 🧠 Application Design

The application is divided into three main Python files.

### `calculator_logic.py`

This file contains the mathematical logic of the calculator.

It is responsible for:

- Receiving input values
- Performing calculations
- Returning results
- Keeping the business logic separated from the graphical interface

This file does not manage buttons, windows, colors, or visual components.

---

### `calculator_ui.py`

This file contains the graphical user interface using `tkinter`.

It is responsible for:

- Creating the calculator window
- Creating buttons
- Managing the visual layout
- Handling user interactions
- Connecting the graphical interface with the calculator logic

---

### `main.py`

This file is the main entry point of the application.

It detects the execution environment and decides how the calculator should run.

If a graphical display is available, the application opens the graphical calculator.

If no graphical display is available, the application runs in console mode.

This allows the same application to run both locally and inside Docker.

---

## 🐳 Docker Strategy

This project uses Docker to package the calculator application into a portable container image.

The Docker image includes:

- Python runtime
- Required Linux packages
- Tkinter support
- Application source code
- Runtime configuration
- Non-root user execution
- Multi-stage build optimization

The Docker image is not stored in the Git repository.

Instead, the image is generated from the Dockerfile.

---

## ❌ Should the Docker Image Be Uploaded to GitHub?

No.

The Docker image should not be uploaded directly to the repository.

Do not upload files like:

```text
mi-calculadora.tar
mi-calculadora.img
docker-image.zip
```

The correct approach is to upload only the files required to build the image:

```text
Dockerfile
Docker-Compose.yaml
.dockerignore
.gitignore
Python-Calculator/src/
MiCalculadora.bat
MiCalculadora.xlaunch
README.md
```

The image is generated with:

```bash
docker build -t mi-calculadora .
```

If the image needs to be shared in the future, it should be pushed to a container registry such as:

```text
Docker Hub
GitHub Container Registry
Azure Container Registry
Amazon Elastic Container Registry
Google Artifact Registry
```

---

## 🏗️ Multi-Stage Dockerfile

This project uses a multi-stage Dockerfile.

A multi-stage Dockerfile separates the build stage from the runtime stage. This is a professional Docker practice because it helps create cleaner, smaller, and more secure images.

### Benefits of Multi-Stage Builds

- Smaller final image
- Cleaner runtime environment
- Reduced attack surface
- Better separation between build and execution
- More professional containerization workflow

---

## 📄 Dockerfile Purpose

The Dockerfile is responsible for building the calculator image.

Main responsibilities:

- Define the Python base image
- Install required dependencies
- Add support for graphical execution
- Copy the application source code
- Create a non-root user
- Set the working directory
- Start the application

Final execution command:

```dockerfile
CMD ["python", "main.py"]
```

---

## ⚙️ Docker Compose

Docker Compose is used to simplify how the application is executed.

Instead of typing a long `docker run` command, the configuration is stored in `Docker-Compose.yaml`.

The compose file defines:

- The calculator service
- The Docker build context
- The image name
- The environment variables required for GUI execution

Example:

```yaml
services:
  calculadora:
    build: .
    image: mi-calculadora
    environment:
      - DISPLAY=host.docker.internal:0
```

---

## 🖥️ GUI Execution from Docker

The calculator uses `tkinter`, which creates a graphical window.

Docker containers do not have a native graphical desktop by default. Because of this, an external display server is required when running the GUI from Windows.

For this project, the graphical output is handled using **VcXsrv**.

Without VcXsrv, the container may run correctly, but the calculator window may not appear.

---

## 🧩 VcXsrv Requirement

VcXsrv is required to display the graphical interface of the calculator from the Docker container on Windows.

### Step 1: Install VcXsrv

Download and install VcXsrv from:

```text
https://sourceforge.net/projects/vcxsrv/
```

Install it using the default options.

---

### Step 2: Configure XLaunch

Open **XLaunch** and use the following configuration:

```text
Display settings: Multiple windows
Client startup: Start no client
Extra settings: Disable access control
```

Leave the other options as default.

At the end, click:

```text
Save configuration
Finish
```

This repository includes the file:

```text
MiCalculadora.xlaunch
```

This file stores the XLaunch configuration and can be used to start the graphical server faster.

---

## 🚀 How to Run the Project

### Option 1: Build the Docker Image

From the root folder of this phase, run:

```bash
docker build -t mi-calculadora .
```

Verify that the image was created:

```bash
docker images
```

Expected image name:

```text
mi-calculadora
```

---

### Option 2: Run the Container Manually

Run the calculator container with the required display variable:

```bash
docker run --rm -it -e DISPLAY=host.docker.internal:0 mi-calculadora
```

Explanation:

```text
--rm
```

Removes the container after it stops.

```text
-it
```

Runs the container in interactive mode.

```text
-e DISPLAY=host.docker.internal:0
```

Sends the graphical output from the container to the Windows X Server.

```text
mi-calculadora
```

Name of the Docker image.

---

### Option 3: Run with Docker Compose

Run the project using Docker Compose:

```bash
docker compose -f Docker-Compose.yaml up --build
```

Alternative command for older Docker Compose versions:

```bash
docker-compose -f Docker-Compose.yaml up --build
```

Stop the service:

```bash
docker compose -f Docker-Compose.yaml down
```

---

### Option 4: Run with Windows Launcher

This project includes a Windows launcher:

```text
MiCalculadora.bat
```

The launcher automates the execution process.

It performs the following steps:

1. Moves the terminal to the project folder.
2. Starts the XLaunch configuration.
3. Waits a few seconds for the X Server to start.
4. Runs the application using Docker Compose.

Run the file:

```text
MiCalculadora.bat
```

If required, execute it as administrator.

---

##  🦇 the `.bat` File

The `.bat` file 

Recommended version:

```bat
@echo off

cd /d "%~dp0"

echo Iniciando servidor X...
start "" "%~dp0MiCalculadora.xlaunch"

echo Esperando 5 segundos a que XServer arranque...
timeout /t 5

echo Lanzando contenedor con Docker Compose...
docker compose -f Docker-Compose.yaml up --build

pause
```

This makes the launcher portable because it uses the current folder where the `.bat` file is located.

---

## 🧪 Expected Result

When the project runs correctly:

- Docker builds the image.
- Docker Compose starts the container.
- VcXsrv receives the graphical output.
- The calculator window opens on Windows.
- The user can interact with the calculator UI.

If no graphical display is available, the application can run in console mode.

---

## 🛡️ Security and Best Practices

This phase applies several good practices for Docker and repository management.

### Docker Best Practices

- Multi-stage Dockerfile
- Non-root user inside the container
- Clean runtime image
- Docker build context controlled with `.dockerignore`
- Application source code copied only when needed
- Environment variable used for display configuration

### Git Best Practices

- Virtual environments are not committed
- Python cache files are ignored
- IDE folders are ignored
- Environment files are ignored
- Local system files are ignored
- Docker image files are not committed

---

## 📁 `.gitignore`

The `.gitignore` file prevents local and generated files from being uploaded to GitHub.

Ignored examples:

```text
venv/
Lib/
Scripts/
pyvenv.cfg
__pycache__/
*.pyc
.vscode/
.idea/
.env
```

These files should stay local because they are related to the developer environment, not to the project source code.

---

## 📁 `.dockerignore`

The `.dockerignore` file prevents unnecessary files from being copied into the Docker build context.

Ignored examples:

```text
.git
.github
terraform
__pycache__
*.pyc
*.pyo
*.pyd
.Python
venv
.env
.env.*
.vscode
.idea
.DS_Store
tests
```

This helps to:

- Reduce image size
- Speed up Docker builds
- Avoid copying sensitive files
- Keep the image clean
- Improve security

---

## 🧰 Useful Docker Commands

Build the image:

```bash
docker build -t mi-calculadora .
```

Run the image:

```bash
docker run --rm -it -e DISPLAY=host.docker.internal:0 mi-calculadora
```

Run with Docker Compose:

```bash
docker compose -f Docker-Compose.yaml up --build
```

Stop Docker Compose:

```bash
docker compose -f Docker-Compose.yaml down
```

List Docker images:

```bash
docker images
```

List running containers:

```bash
docker ps
```

List all containers:

```bash
docker ps -a
```

Remove the image:

```bash
docker rmi mi-calculadora
```

Clean unused Docker resources:

```bash
docker system prune
```

---

## 🧯 Troubleshooting

### The container runs but the calculator window does not appear

Possible cause:

```text
VcXsrv is not running or DISPLAY is not configured correctly.
```

Solution:


1. Download the official VcXsrv installer directly from[SourceForge](https://sourceforge.net/projects/vcxsrv/).
2. Open XLaunch.
2. Use `Multiple windows`.
3. Select `Start no client`.
4. Enable `Disable access control`.
5. Run Docker Compose again.

---

### Error: Cannot open display

Possible cause:

```text
The container cannot connect to the Windows graphical server.
```

Solution:

Verify that the environment variable is configured:

```bash
-e DISPLAY=host.docker.internal:0
```

Or in Docker Compose:

```yaml
environment:
  - DISPLAY=host.docker.internal:0
```

---

### Docker Compose command does not work

Try the newer Docker Compose command:

```bash
docker compose -f Docker-Compose.yaml up --build
```

Or the older version:

```bash
docker-compose -f Docker-Compose.yaml up --build
```

---

### The image does not rebuild with new changes

Run:

```bash
docker compose -f Docker-Compose.yaml up --build
```

Or rebuild manually:

```bash
docker build --no-cache -t mi-calculadora .
```

---

## 📸 Screenshots

Recommended folder for screenshots:

```text
assets/
```

Suggested screenshots:

```text
assets/calculator-ui.png
assets/docker-build.png
assets/docker-compose-run.png
assets/vcxsrv-config.png
```

Example usage in the README:

```markdown
![Calculator UI](assets/calculator-ui.png)
```

Screenshots can be uploaded to the repository because they document the project.

Docker images should not be uploaded to the repository.

---

## 🔄 Execution Flow

The execution flow of this phase is:

```text
Python Source Code
        ↓
Dockerfile
        ↓
Docker Image
        ↓
Docker Compose
        ↓
VcXsrv / XLaunch
        ↓
Calculator UI on Windows
```

---

## 🧭 Learning Outcomes

By completing this phase, the following skills are demonstrated:

- Creating Docker images
- Writing a Dockerfile
- Using multi-stage Docker builds
- Running Python applications inside containers
- Using Docker Compose
- Managing Docker build context with `.dockerignore`
- Running GUI applications from Docker
- Configuring environment variables in containers
- Applying basic container security practices
- Organizing a project for future CI/CD pipelines

---

## 🔮 Next Steps

Future improvements for this project can include:

- Add automated CI pipeline
- Build the Docker image with GitHub Actions
- Scan the Docker image for vulnerabilities
- Push the image to a container registry
- Add unit tests for the calculator logic
- Add linting with Python tools
- Add version tags for the Docker image
- Deploy the container to a cloud platform
- Add monitoring and observability

---

## 🧱 Portfolio Value

This phase shows that the project is not only a Python application, but also a containerized application ready for modern DevOps and Platform Engineering workflows.

It demonstrates practical knowledge of:

- Docker
- Docker Compose
- Python packaging
- Container execution
- GUI application execution from containers
- Development environment isolation
- Repository hygiene
- Basic security practices

This is a strong foundation for the next phases of the portfolio, where CI/CD, cloud infrastructure, monitoring, and AI automation can be added.

---

## ✅ Phase Status

Status: Completed

This phase successfully demonstrates how to containerize a Python calculator application using Docker, Docker Compose, and a Windows graphical execution setup.
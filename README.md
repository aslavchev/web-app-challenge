# 🚀 DevOps Flask App

A simple Flask-based web application demonstrating core DevOps practices including containerization with Docker, orchestration with Docker Compose, persistent storage with Redis, automated testing with GitHub Actions, and modular development with Git branches and pull requests.

---

## 📚 Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
- [Available Endpoints](#available-endpoints)
- [Docker Usage](#docker-usage)
- [Health Check](#health-check)
- [GitHub Actions CI/CD](#github-actions-cicd)
- [Project Structure](#project-structure)

---

## ✨ Features

- ✅ Welcome page at `/`
- ✅ Visit counter using Redis at `/visit`
- ✅ Health check endpoint at `/health`
- ✅ Fully containerized with Docker
- ✅ Persistent Redis volume
- ✅ Automated testing via GitHub Actions

---

## ⚙️ Tech Stack

- **Python 3.9**
- **Flask**
- **Redis**
- **Docker & Docker Compose**
- **GitHub Actions**

---

## 🚀 Getting Started

### Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd YOUR_REPO
```

### Build and Start the Services

```bash
docker-compose up --build
```

### Access the Application

📍 http://localhost:8000

---

## 📡 Available Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Returns a welcome message |
| `/visit` | GET | Increments and returns visit count |
| `/health` | GET | Returns 200 if Redis is available |

---

## 🐳 Docker Usage

### Build and Start Containers

```bash
docker-compose up --build
```

### Stop Services

```bash
docker-compose down
```

> **Note:** The Redis volume ensures that the visit count persists across container restarts.

---

## ✅ Health Check

The `/health` endpoint checks the connection to Redis:

- ✅ Returns HTTP 200 OK if Redis is reachable
- ❌ Returns HTTP 500 if Redis is unavailable

This endpoint is used in:

- Docker container health check
- GitHub Actions workflow to verify service health

---

## 🔁 GitHub Actions CI/CD

A CI workflow is triggered on pull requests to main. It performs the following:

1. **Starts services in detached mode:**
   ```bash
   docker-compose up --build -d
   ```

2. **Waits for the app to start.**

3. **Sends request to:**
   ```bash
   curl http://localhost:8000/health
   ```

4. **Verifies it returns HTTP 200.**

5. **Cleans up services:**
   ```bash
   docker-compose down
   ```

📁 GitHub Actions workflow is defined in:

```
.github/workflows/test.yml
```

---

## 📁 Project Structure

```
project/
├── app.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .github/
│   └── workflows/
│       └── test.yml
├── .gitignore
├── README.md
└── TASK_CHECKLIST.md
```





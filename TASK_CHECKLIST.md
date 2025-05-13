# ✅ DevOps Flask App – Task Checklist

Track the progress of your project using this structured checklist. Each task is managed in its own Git branch and merged via Pull Requests into the `main` branch.

---

## 📦 Project Setup
- [x] Initialize Git repository
- [x] Create and push initial `main` branch
- [x] Add remote GitHub repository

---

## 🔧 Task 1: Flask Application
Branch: `flask-app`
- [x] Create branch `flask-app`
- [x] Add `app.py` with routes: `/`, `/visit`, and `/health`
- [x] Integrate Redis using environment variables
- [x] Store visit count in Redis
- [x] Create Pull Request to `main`
- [x] Merge PR

---

## 🐳 Task 2: Dockerfile
Branch: `dockerfile`
- [x] Create branch `dockerfile`
- [x] Write `Dockerfile` using `python:3.9-slim`
- [x] Install Python dependencies from `requirements.txt`
- [x] Set Flask as the container entrypoint
- [x] Create Pull Request to `main`
- [x] Merge PR

---

## ⚙️ Task 3: Docker Compose
Branch: `docker-compose`
- [x] Create branch `docker-compose`
- [x] Write `docker-compose.yml` for Flask and Redis
- [x] Set Redis as a dependency of the web app
- [x] Persist Redis data using a volume
- [x] Map ports correctly (`8000:5000`)
- [x] Add a health check for `/health`
- [x] Create Pull Request to `main`
- [x] Merge PR

---

## 🚦 Task 4: GitHub Actions CI
Branch: `github-actions`
- [x] Create branch `github-actions`
- [x] Add `.github/workflows/test.yml`
- [x] Build services with `docker-compose`
- [x] Wait for app readiness
- [x] Check `/health` returns HTTP 200
- [x] Tear down containers
- [x] Create Pull Request to `main`
- [x] Merge PR

---

## 📚 Task 5: Docs and .gitignore
Branch: `docs-and-gitignore`
- [x] Create branch `docs-and-gitignore`
- [x] Add `.gitignore` to exclude unnecessary files
- [x] Write a complete `README.md`
- [x] Include build/run instructions and pipeline explanation
- [x] Create Pull Request to `main`
- [x] Merge PR

---

## 🎉 Final Review
- [x] All branches merged into `main`
- [x] CI passes for all PRs
- [x] App starts successfully with `docker-compose up`
- [x] `/visit` persists visit count via Redis volume
- [x] Public GitHub repository with full documentation

---


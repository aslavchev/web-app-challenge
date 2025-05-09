# web-app-challenge

# DevOps Flask App

This is a simple web application built with Flask and Redis, containerized using Docker and managed with Docker Compose. 
A GitHub Actions pipeline is included to automate testing on pull requests.

## Features

- `/`: Welcome message
- `/visit`: Increments and displays visit count (stored in Redis)
- `/health`: Returns 200 if Redis is reachable, 500 otherwise

## Setup

### Build & Run Locally

```bash
docker-compose up --build


### Stop docker compose Locally

```bash
docker-compose down

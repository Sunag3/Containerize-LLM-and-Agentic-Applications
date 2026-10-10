# QuickBite ETA Service - Docker Deployment Guide

This guide provides instructions on how to pull and run the containerized **QuickBite ETA Prediction Service** from Docker Hub, along with sample test commands.

---

## Prerequisites

Ensure you have the following installed on your machine:
* [Docker Desktop](https://www.docker.com/products/docker-desktop/) (running and active)
* A terminal or command-line interface (Bash, PowerShell, or Zsh)

---

## Step 1: Pull the Docker Image

Pull the pre-built application image from my Docker Hub

```bash
docker pull sunag3/quickbite-eta:v1
```

---

## Step 2: Run the Docker Container

Spin up the container in detached mode (`-d`), mapping port `8000` on your host machine to port `8000` inside the container:

```bash
docker run -d -p 8000:8000 --name eta-service sunag3/quickbite-eta:v1
```

---

## Step 3: Verify Container Status

Check if the container is running smoothly:

```bash
docker ps
```

You should see `eta-service` listed with status `Up` on port `8000`.

---

## Step 4: Test the API Endpoint

You can test the ETA prediction service by sending a `POST` request via `curl` or any API client (like Postman):

```bash
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"distance_km": 4.5, "prep_time_min": 15, "rider_available": 1, "is_raining": 1}'
```

### Expected Response:
```json
{"eta_minutes":40.1,"message":"Your food arrives in 40.1 min 🍔"}
```

---

## Utility Commands

* **View Container Logs:**
  ```bash
  docker logs eta-service
  ```
* **Stop the Service:**
  ```bash
  docker stop eta-service
  ```
* **Remove the Container:**
  ```bash
  docker rm eta-service

## 🚀 Case 1: Create Dockerfile → Build Image → Run Container → Push to Docker Hub

### 1. Create a `Dockerfile`

```Dockerfile
# Use base image
FROM python:3.10

# Set working directory
WORKDIR /app

# Copy files
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Expose port
EXPOSE 8000

# Run application
CMD ["python", "app.py"]
```

---

### 2. Build Docker Image

```bash
docker build -t your_username/image_name:tag .
```

✅ Example:

```bash
docker build -t samiksha/my_app:v1 .
```

---

### 3. Run Container

```bash
docker run -d -p 8000:8000 --name container_name image_name
```

✅ Example:

```bash
docker run -d -p 8000:8000 --name my_container samiksha/my_app:v1
```

---

### 4. Login to Docker Hub

```bash
docker login
```

---

### 5. Push Image to Docker Hub

```bash
docker push your_username/image_name:tag
```

✅ Example:

```bash
docker push samiksha/my_app:v1
```

---

## 📦 Case 2: Pull Image from Docker Hub → Run Container

### 1. Pull Image

```bash
docker pull your_username/image_name:tag
```

✅ Example:

```bash
docker pull samiksha/my_app:v1
```

---

### 2. Run Container from Pulled Image

```bash
docker run -d -p 8000:8000 --name container_name image_name
```

✅ Example:

```bash
docker run -d -p 8000:8000 --name my_container samiksha/my_app:v1
```

---

## 🔧 Useful Docker Commands

### List running containers

```bash
docker ps
```

### List all containers

```bash
docker ps -a
```

### Stop container

```bash
docker stop container_name
```

### Remove container

```bash
docker rm container_name
```

### Remove image

```bash
docker rmi image_name
```

---
* Use `.dockerignore` to avoid unnecessary files
* Keep images lightweight (use slim base images)

---

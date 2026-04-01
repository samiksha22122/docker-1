- Suppose we have build one app created its image of xGBs, again we have added some changes in app in some file so we now need to build the image again then caching will help here
- We will change the Dockerfile instructions
- Now the req.txt file will not rebuild again while we are building another image of same app.
- It will save time and internet

Multi-Stage Builds->

Purpose - to make your docker image of reduced size as compare to single stage builds
<img width="715" height="309" alt="image" src="https://github.com/user-attachments/assets/e28fa462-0e85-48f6-a416-f5081ef4c311" />

---

# 📦 Docker Setup – Calculator App

This project demonstrates:

* Basic Docker build
* Multi-stage Docker build
* Image optimization using caching

---

## 🚀 1. Build Docker Image (Default Dockerfile)

```bash
docker build -t calculator:latest .
```

👉 Uses default `Dockerfile`
👉 Creates image with tag `calculator:latest`

---

## 🚀 2. Build Image Using Custom Dockerfile

```bash
docker build -f Dockerfile_copy -t calculator:v2.0 .
```

👉 `-f` → specify Dockerfile name
👉 `-t` → tag the image

---

## ▶️ 3. Run Container

```bash
docker run -p 5000:5000 calculator:latest
```

or

```bash
docker run -p 5000:5000 calculator:v2.0
```

👉 Maps container port → local port

---

## 📋 4. List Docker Images

```bash
docker images
```

---

## 🛑 5. Stop & Remove Container

```bash
docker stop <container_id>
docker rm <container_id>
```

---

## 🧠 Dockerfiles Used

### 🐳 Dockerfile (Basic)

* Simple build
* Installs dependencies
* Copies full code

---

### 🐳 Dockerfile_copy (Multi-stage Build)

* Uses **multi-stage build**
* Separates dependency installation from final image
* Produces cleaner and optimized image

---

## ⚡ Key Concepts

### 🔹 Docker Caching

* Layers are reused if no changes detected
* Faster rebuilds

👉 Example:

* If only code changes → dependencies not reinstalled

---

### 🔹 Multi-stage Build

* Reduces image size
* Removes unnecessary build files
* Improves performance

---

## 🔍 Observation

* Multi-stage build completed faster ⏱️
* Image size appeared similar due to shared layers
* Only changed layers were rebuilt

---

## 🎯 Conclusion

* Docker ensures consistent environments
* Caching improves build speed
* Multi-stage builds optimize production images

---
```dockerfile
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
```
<img width="557" height="75" alt="image" src="https://github.com/user-attachments/assets/a2dd0872-c94f-45fe-8648-f2cb43743672" />

---

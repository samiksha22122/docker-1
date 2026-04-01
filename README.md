# Docker Commands Guide

## Initial Steps

**Create image**

```
docker build -t image_name:tag
```

====================>

```
docker build -t calculator:latest .
```

**Run container**

```
docker run --name create_name_of_container -p 0000:0000 image_name:tag
```

====================>

```
docker run --name calculator-container -p 8000:8000 calculator:latest
```

---

## Port Issue Fix

The above step of running container will fail if not given port, hence follow below commands:

1. Open terminal
2. `"export PORT=####"` to set port
   → this is how u set env var for your local system / host machine
3. Write `"echo $PORT"` to see port
4. Run `app.py`

---

## Fix Container Port Error

Now image is created, if run the container it will not work (port error)

So next...

1. Delete the created container

2. Create the new container

3. Run with this command:

```
docker run --name calc-container --env PORT=8000 -d -p8000:8000 calculator:latest
```

→ This is how you set an environment variable inside the Docker container at runtime.

```
-p 8000:8000
```

→ maps host port → container port

---

## Run Multiple Containers

Now if you want to run a different docker container do this:

```
docker run --name container_name --env PORT=5000 -d -p5000:5000 calculator:latest
```

-----------now 2 containers are created and running at same time-------------

---

## Default Port in Dockerfile

If wants to add a default port in case the user havent send-add this in dockerfile-->

```
ENV PORT=5000
```

If we have this then no need to give in the docker run command

In case if you still pass the env value, this env value will override the dockerfile default value and will run on it

---

## Using .env File

If want to use .env and mention the port and all there do this:

```
docker run --name calc-container --env-file .env -p 8000:8000 calculator:latest
```

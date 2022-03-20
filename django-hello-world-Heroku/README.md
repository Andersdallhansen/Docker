# Hello, World! Django application inside Docker

Build the docker image

```Dockerfile
docker build -t django-hello-world .
```

Run the image interactively

```Dockerfile
docker run -it -p 8000:8000  django
```

This should the Django application at http://0.0.0.0:8000/.

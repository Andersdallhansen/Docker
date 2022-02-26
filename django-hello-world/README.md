# Hello, World! Django application inside Docker

First build the docker image

```Dockerfile
docker build -t django-hello-world .
```

Then run it interactively
```Dockerfile
docker run -it -p 8000:8000  django
```

This starts the Django appliation at 'http://0.0.0.0:8000/'.

FROM python:3.8

WORKDIR /usr/src/app

#Copy and install requirements for the Django application
COPY ./django-application/requirements.txt requirements.txt
RUN pip install -r requirements.txt

#After environment is set up, copy the rest (this order was suggested on stack)
COPY ./django-application django-application

EXPOSE 8000

#Run the django application
CMD ./django-application/manage.py runserver 0.0.0.0:8000

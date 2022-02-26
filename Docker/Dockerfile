FROM python:3.8

WORKDIR /usr/src/app

#Copy and install requirements for the Django application
COPY ./Django_Application/requirements.txt requirements.txt
RUN pip install -r requirements.txt

#After environment is set up, copy the rest (this order was suggested on stack)
COPY ./Django_Application Django_Application

EXPOSE 8000

#Run the django application
CMD ./Django_Application/manage.py runserver 0.0.0.0:8000

#CMD ["python", "./Django_Application/manage.py", "runserver"]

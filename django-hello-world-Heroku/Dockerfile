FROM python:3.8

WORKDIR /usr/src/app

#Copy and install requirements for the Django application inside app folder
COPY requirements.txt /app/requirements.txt
RUN set -ex \
    && pip install --upgrade pip \
    && pip install --no-cache-dir -r /app/requirements.txt


#Go to app folder
WORKDIR /app

#Add application to the app folder
ADD django-application .

#Expose 8000

#Run application using gunicorn
CMD gunicorn django-application.wsgi:application --bin 0.0.0.0:$PORT

#CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "django-application.wsgi:application"]

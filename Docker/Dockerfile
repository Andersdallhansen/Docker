FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./Django_Application
RUN pip install -r requirements.txt


COPY Django_Application /Django_Application

CMD ["python", "./Django_Application/manage.py"]